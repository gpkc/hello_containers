import pytest

import hello_containers


@pytest.fixture
def app():
    hello_containers.app.testing = True
    app_ = hello_containers.app
    return app_