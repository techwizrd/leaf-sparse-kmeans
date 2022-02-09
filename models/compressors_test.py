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
        print(Cx)
        assert np.count_nonzero(Cx) == k


def test_top_k_2():
    x = np.array([28, 39, -56, -48, 11, 66, 80, 92, 93, -30])
    actual = compressors.TopKCompressor.compress(x=x, k=8)
    expected = np.array([0, 39, -56, -48, 0, 66, 80, 92, 93, -30])
    np.testing.assert_array_equal(x=actual, y=expected, verbose=True)


def test_top_k_3():
    x = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    actual = compressors.TopKCompressor.compress(x=x, k=8)
    expected = np.array([-5, -4, -3, -2, 0, 0, 2, 3, 4, 5])
    np.testing.assert_array_equal(x=actual, y=expected, verbose=True)


def test_stc():
    x = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    actual = compressors.SparseTernaryCompressor.compress(x=x, k=8)
    expected = np.array([-3.5, -3.5, -3.5, -3.5, 0, 0, 3.5, 3.5, 3.5, 3.5])
    np.testing.assert_array_equal(x=actual, y=expected, verbose=True)
