import socket

from flask import url_for


def test_hello_status(client):
    res = client.get(url_for('hello', name='Juan'))

    assert res.status_code == 200


def test_hello_message(client):
    res = client.get(url_for('hello', name='Juan'))

    assert res.json['message'] == f"Hello Juan from {socket.gethostname()}"
