import pytest
from app import app

@pytest.fixture(autouse=True)
def whitenoise_autorefresh(settings):
    """
    Get rid of whitenoise "No directory at" warning, as it's not helpful when running tests.

    Related:
        - https://github.com/evansd/whitenoise/issues/215
        - https://github.com/evansd/whitenoise/issues/191
        - https://github.com/evansd/whitenoise/commit/4204494d44213f7a51229de8bc224cf6d84c01eb
    """
    settings.WHITENOISE_AUTOREFRESH = True
    
@pytest.fixture
def client():
    tester = app.test_client()
    yield tester


def test_index(client):
    response = client.get("/", content_type="html/text")
    assert response.status_code == 200


def test_projects(client):
    response = client.get("/projects/", content_type="html/text")
    assert response.status_code == 200


def test_contact(client):
    response = client.get("/contact/", content_type="html/text")
    assert response.status_code == 200


def test_resume(client):
    response = client.get("/resume/", content_type="html/text")
    assert response.status_code == 200


def test_404(client):
    response = client.get("/oops/", content_type="html/text")
    assert response.status_code == 404