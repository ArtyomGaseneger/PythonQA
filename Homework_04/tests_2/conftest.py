import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url", default="https://api.openbrewerydb.org/breweries", help="This is request URL"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")
