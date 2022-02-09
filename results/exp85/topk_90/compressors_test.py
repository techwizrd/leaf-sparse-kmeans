#!/usr/bin/env python

import pytest
import compressors
import numpy as np


@pytest.fixture
def numbers():
    return np.random.randint(-100, 100, 10)


def test_rand_k(numbers):
    for k in range(len(numbers)):
        Cx = compressors.RandKCompressor.compress(x=numbers, k=k)
        assert np.count_nonzero(Cx) == k


def test_top_k(numbers):
    for k in range(len(numbers)):
        Cx = compressors.TopKCompressor.compress(x=numbers, k=k)
        assert np.count_nonzero(Cx) == k
