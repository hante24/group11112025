import pytest
from revision.utils import is_valid_email, avg, uah_to_usd



def test_valid_email():
    assert is_valid_email("user@example.com") is True


def test_invalid_multiple_at():
    assert is_valid_email("a@b@c.com") is False


def test_no_dot_in_domain():
    assert is_valid_email("user@example") is False


def test_empty_string():
    assert is_valid_email("") is False



def test_avg_normal_list():
    assert avg([1, 2, 3]) == 2


def test_avg_single_element():
    assert avg([10]) == 10


def test_avg_negative_numbers():
    assert avg([-2, -4, -6]) == -4


def test_avg_empty_list():
    with pytest.raises(ValueError):
        avg([])



def test_uah_to_usd_normal_case():
    assert uah_to_usd(1000, 40) == 25


def test_uah_to_usd_invalid_rate():
    with pytest.raises(ValueError):
        uah_to_usd(1000, 0)


def test_uah_to_usd_invalid_amount():
    with pytest.raises(ValueError):
        uah_to_usd(0, 40)


def test_uah_to_usd_large_values():
    assert uah_to_usd(10_000_000, 40) == 250000


def test_uah_to_usd_float_precision():
    result = uah_to_usd(99.99, 36.6)
    assert pytest.approx(result, 0.0001) == 99.99 / 36.6