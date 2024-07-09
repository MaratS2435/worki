import pytest
import requests

from tests.src.basic_classes.response import Response


def test_create_delete(create_user, get_user_builder, delete_user_id):
    user = get_user_builder.build()
    print(user)
    resp = Response(create_user(user)).assert_status_code(201).response_json
    print(resp)
    assert resp['firstname'] == user['firstname']
    assert resp['username'] == user['username']
    resp = delete_user_id(resp['id'])
    assert resp.status_code == 204


def test_get_users(get_users, get_user_builder, create_user, delete_user_id):
    user = get_user_builder.build()
    print(user)
    resp = Response(create_user(user)).assert_status_code(201).response_json
    print(resp)
    print(Response(get_users).assert_status_code(200).response_json)
    assert resp['firstname'] == user['firstname']
    assert resp['username'] == user['username']
    resp = delete_user_id(resp['id'])
    assert resp.status_code == 204


def test_get_users2(get_users):
    print(Response(get_users).assert_status_code(200).response_json)
