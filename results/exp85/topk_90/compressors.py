#!/usr/bin/env python

"""Sparsified k-means for client-adaptive federated learning."""

from typing import Union, Callable
import numpy as np


def mse(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Calculate MSE between two ndarrays A and B."""
    return (np.linalg.norm(A - B) ** 2) / len(A)


def baseline(g: np.ndarray) -> np.ndarray:
    """Return vector withot compression."""
    return g


def topk(x: np.ndarray, k: int = 1) -> np.ndarray:
    assert 0 < k < len(x)
    topk_idxs = np.abs(x).argpartition(k)[k:]
    newx = np.zeros_like(x)
    newx[topk_idxs] = x[topk_idxs]
    return newx


#def rand_k(g: np.ndarray, k: int, rng: np.random.Generator = None) -> np.ndarray:
def rand_k(g: np.ndarray, k: int, rng = None) -> np.ndarray:
    """Biased random sparsification.

    Retain k randomly-selected (without replacement) elements of g."""
    assert 0 < k < len(g)

    # From numpy 1.17. Improves performance by preventing copy of input under the hood.
    if rng is None:
        rng = np.random.default_rng()
    res = rng.choice(g.size, size=k + 1, replace=False)

    Cg = np.zeros_like(g)
    Cg[res] = g[res]
    return Cg


def unbiased_rand_k(
    #g: np.ndarray, k: int, rng: np.random.Generator = None
    g: np.ndarray, k: int, rng=None
) -> np.ndarray:
    """Unbiased random sparsification.

    Retain k randomly-selected (without replacement) elements of g, unbiased by d/k where d = len(g)."""
    assert 0 < k < len(g)

    d = g.size
    return d / k * rand_k(g=g, k=k, rng=rng)


def calc_cluster_means(
    centroids: np.ndarray, cluster_assignments: np.ndarray, data: np.ndarray
) -> np.ndarray:
    """Calculate cluster means given the cluster assignments and data."""
    new_centroids = centroids.copy()
    for cluster_id in range(len(centroids)):
        cluster_members = np.argwhere(cluster_assignments == cluster_id)
        if cluster_members.size == 0:  # Handle emptied clusters
            new_centroids[cluster_id] = 0
        else:
            new_centroids[cluster_id] = data[cluster_members].mean()

    return new_centroids


def compress_b(
    g: np.ndarray,
    b: int,
    budget: int = None,
    n_iters: int = 10,
    tol: float = 1e-8,
    enforce_constraint: bool = True,
    dist_fn: Callable[[np.ndarray, np.ndarray], np.ndarray] = None,
) -> Union[np.float64, np.ndarray, np.ndarray]:
    """
    Compress the gradient vector g to using a bit-depth b.
    """
    assert budget is not None and budget > 0, "budget must be an integer greater than 0"
    assert b > 0, "must have positive number of bits b"
    k = 2 ** b  # Number of clusters

    # distance measure
    # dist = lambda x: np.sqrt(np.square(x))  # alternative
    if dist_fn is None:
        dist_fn = lambda x: np.square(np.abs(x))

    bottomk = lambda A, k: np.argpartition(A, k)[:k]

    # Step 1: Initialize centroids
    # Initialize centroids roughly evenly across the range
    # Make sure to start at zero because we need a centroid
    # at zero that we do not update to act as a sparsifier.
    # TODO: What if this is randomly sampled rather than evenly spread?
    theta = np.linspace(start=0, stop=np.max(g), num=k)

    for i in range(n_iters):
        # Step 2: Compute cluster assignments
        # Calculate distance between every point and every centroid, and assign the
        # point to the cluster with the closest centroid
        distances = dist_fn(g - theta).copy()
        l = np.argmin(distances, axis=1)  # cluster assignment
        d2 = np.min(distances, axis=1)
        delta2 = dist_fn(g.flatten())
        xi2 = np.fmax(delta2 - d2, 0)

        # Step 3: Check sparsity constraint
        # n_j(b): Number of entries not mapped to 0
        # B_j: budget for client j
        # n_j(b) <= B_j/b
        # If constraint is not fulfilled, change labels l_i to zero
        # for which xi^2_i is smallest until constraint not fulfilled.
        # NOTE: This can delete a cluster!
        n_j = np.count_nonzero(l)
        if n_j > budget / b and enforce_constraint:  # constraint not fulfilled
            num_exceeded = int(np.ceil(n_j - (budget / b)))
            # Indexes of smallest, nonzero values in xi2. The fmax means theta_new
            # smallest_xi2 value in xi2 is almost always guaranteed to be zero, but
            # that does us no good.
            # TODO: Figure out if this modification is sensible.
            smallest_xi2 = bottomk(xi2[np.nonzero(xi2)], num_exceeded + 1)
            l[smallest_xi2] = 0
            n_j = np.count_nonzero(l)
        assert n_j <= budget / b, "sparsity constrain violated"

        # Step 4: Update cluster means
        theta_new = calc_cluster_means(centroids=theta, cluster_assignments=l, data=g)
        if enforce_constraint:
            theta_new[0] = 0  # Retain zero as a centroid for sparsification

        # Stopping criteria is run for n_iters or whenever cluster means stop changing.
        # This stopping criteria is cheaper than checking whether the cluster
        # assignments keep changing.
        if mse(theta_new, theta) < tol:
            theta = theta_new
            break
        theta = theta_new

    #print(f"Clustered for {b=} in {i=} iters, {np.count_nonzero(l)=}")
    objective = np.min(dist_fn(g - theta), axis=1).sum()

    return objective, l, theta


def sparse_kmeans(
    gradient: np.ndarray, budget: int = None, enforce_constraint: bool = True
) -> np.ndarray:
    """Find optimal number of bits to compress gradient vector."""
    previous_objective = None
    for b in range(1, 3):
        inner_objective, cluster_assignments, centroids = compress_b(
            gradient, b, budget, enforce_constraint=enforce_constraint
        )
        #print(f"{b=}, {inner_objective=}")

        if previous_objective is None or inner_objective < previous_objective:
            previous_objective = inner_objective
        else:
            break

    # Construct compressed gradient
    compressed_gradient = gradient.copy()
    for i, centroid in enumerate(centroids):
        compressed_gradient[cluster_assignments == i] = centroid

    compression_error = mse(gradient, compressed_gradient)

    return compressed_gradient, compression_error


if __name__ == "__main__":
    print("Import these functions as a module. This is not meant to be run directly.")
