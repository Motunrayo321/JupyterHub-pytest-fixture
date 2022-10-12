# -*- coding: utf-8 -*-

from firstuseauthenticator import FirstUseAuthenticator
import pytest


def pytest_addoption(parser):
    group = parser.getgroup('awesome')
    group.addoption(
        '--foo',
        action='store',
        dest='dest_foo',
        default='2022',
        help='Set the value for the fixture "bar".'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


@pytest.fixture
def bar(request):
    return request.config.option.dest_foo


@pytest.fixture
def test_first_use():
	""" Returns a firstuseauthenticator object with minimum length of 10. """
	
	#Initialize FirstUseAuthenticator object.
	auth = FirstUseAuthenticator()
	
	#Set minimum length to 10.
	auth.min_password_length = 10
	
	return auth
