from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_url_validation():
    with mock.patch("app.main.valid_google_url") as mock_check_url:
        yield mock_check_url


@pytest.fixture()
def mocked_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_should_access_google_page(mocked_url_validation, mocked_internet_connection) -> None:
    mocked_url_validation.return_value = True
    mocked_internet_connection.return_value = True
    assert can_access_google_page("youtube.com") == "Accessible"


def test_should_not_access_if_url_invalid(mocked_url_validation) -> None:
    mocked_url_validation.return_value = False
    assert can_access_google_page("maate.academy") == "Not accessible"


def test_should_not_access_if_no_connection(mocked_internet_connection) -> None:
    mocked_internet_connection.return_value = False
    assert can_access_google_page("facebook.com") == "Not accessible"
