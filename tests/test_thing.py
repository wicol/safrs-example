from tests.factories import ThingFactory, SubThingFactory


def test_thing_get_by_name(client):
    thing = ThingFactory(name="something")

    res = client.get("/thing/get_by_name?name=something")
    assert res.status_code == 200
    assert res.get_json()["data"]["id"] == thing.id
    assert res.get_json()["data"]["attributes"]["name"] == thing.name


def test_subthing_include_parent(client):
    subthing = SubThingFactory(name="subsomething")

    res = client.get(f"/subthing/{subthing.id}?include=thing")
    assert res.status_code == 200
    response_data = res.get_json()
    assert response_data["data"]["id"] == subthing.id
    assert response_data["data"]["attributes"]["name"] == subthing.name
    assert response_data["included"][0]["id"] == subthing.thing.id
