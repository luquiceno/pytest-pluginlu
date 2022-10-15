# -*- coding: utf-8 -*-

import pytest
from firstuseauthenticator import FirstUseAuthenticator

@pytest.fixture
def test_auth_minPassword():
    auth = FirstUseAuthenticator()
    auth.min_password_length = 10
    return auth