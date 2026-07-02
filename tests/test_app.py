async def test_get_activities(client):
    # Arrange
    # Act
    resp = await client.get("/activities")
    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


async def test_root_redirect(client):
    # Arrange
    # Act
    resp = await client.get("/", follow_redirects=False)
    # Assert
    assert resp.status_code in (301, 302, 307, 308)
    assert resp.headers.get("location") == "/static/index.html"
