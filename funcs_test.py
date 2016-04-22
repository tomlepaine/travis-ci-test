import pytest

import funcs


def test_identity():
    assert funcs.identity(5) == 5


def test_addition():
    assert funcs.addition(1, 1) == 2


def test_import_requests():
    with pytest.raises(ImportError):
        import requests


def test_numpy():
    import numpy
    assert type(numpy.array(0)) == numpy.ndarray
