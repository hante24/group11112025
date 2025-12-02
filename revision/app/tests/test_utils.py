import pytest
from revision.app.utils import uah_to_usd, is_valid_email, avg


def test_uah_to_usd_basic():
    assert uah_to_usd(4000, 40) == 100.00


def test_uah_to_usd_default_rate():
    assert uah_to_usd(800) == 20.00


def test_uah_to_usd_invalid_amount():
    with pytest.raises(ValueError):
        uah_to_usd(-10)


def test_uah_to_usd_invalid_rate():
    with pytest.raises(ValueError):
        uah_to_usd(100, 0)


def test_valid_email():
    assert is_valid_email("user@example.com") is True


def test_invalid_email_no_at():
    assert is_valid_email("userexample.com") is False


def test_invalid_email_no_dot():
    assert is_valid_email("user@example") is False


def test_invalid_email_empty_local():
    assert is_valid_email("@gmail.com") is False


def test_invalid_email_non_string():
    assert is_valid_email(123) is False


def test_avg_basic():
    assert avg([1, 2, 3]) == 2


def test_avg_float():
    assert avg([1.0, 2.0, 3.0]) == 2.0


def test_avg_empty():
    with pytest.raises(ValueError):
        avg([])


def test_avg_invalid_type():
    with pytest.raises(ValueError):
        avg([1, "x", 3])