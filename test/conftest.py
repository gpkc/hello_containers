import pytest

import app as flask_app


@pytest.fixture
def app():
    flask_app.app.testing = True
    app_ = flask_app.app
    return app_