import copy
import pytest
import httpx
from httpx import ASGITransport
import src.app as app_module


_ORIG_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activities dict around each test."""
    backup = copy.deepcopy(_ORIG_ACTIVITIES)
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(backup))
    yield
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(backup))


@pytest.fixture
async def client():
    transport = ASGITransport(app=app_module.app)
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        yield client
