def test_hello_world(test_client):
    res = test_client.get("/api/city")
    assert res.status_code == 200
    assert res.json['body'] == ""
