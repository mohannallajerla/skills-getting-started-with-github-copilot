from urllib.parse import quote


async def test_signup_for_activity(client):
    # Arrange
    email = "newstudent@mergington.edu"
    path = f"/activities/{quote('Chess Club')}/signup"

    # Act
    resp = await client.post(path, params={"email": email})

    # Assert
    assert resp.status_code == 200
    resp2 = await client.get("/activities")
    assert email in resp2.json()["Chess Club"]["participants"]


async def test_duplicate_signup_returns_400(client):
    # Arrange
    email = "dupstudent@mergington.edu"
    path = f"/activities/{quote('Programming Class')}/signup"
    await client.post(path, params={"email": email})

    # Act
    resp = await client.post(path, params={"email": email})

    # Assert
    assert resp.status_code == 400


async def test_remove_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "toremove@example.com"
    signup_path = f"/activities/{quote(activity)}/signup"
    await client.post(signup_path, params={"email": email})

    # Act
    resp = await client.delete(f"/activities/{quote(activity)}/participants", params={"email": email})

    # Assert
    assert resp.status_code == 200
    resp2 = await client.get("/activities")
    assert email not in resp2.json()[activity]["participants"]
