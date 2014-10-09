from __future__ import unicode_literals
import json
import os
import sys
import urlparse

import pytest

# place `cwd` into py.test's line of sight
sys.path.insert(0, os.getcwd())

from acoustid_api import AcoustID, exceptions


DEMO_TRACK = '9e1ea2fc-8b0b-40ac-b98a-126a98752002'


def test_basic_track_search():
    "Tests a simple track search"

    api = AcoustID(os.environ['ACOUSTID_KEY'])
    resp = api.track(DEMO_TRACK)

    assert type(resp) == list


def test_track_search_with_meta():
    "Tests a complex track search"

    api = AcoustID(os.environ['ACOUSTID_KEY'])
    resp = api.track(DEMO_TRACK, meta=('sources', 'recordings'))

    assert type(resp) == list


def test_bad_track_id():
    "Sends a request with a bad track UUID"

    api = AcoustID(os.environ['ACOUSTID_KEY'])

    with pytest.raises(exceptions.InvalidUUID):
        resp = api.track('l-o-l')


def test_basic_fingerprint_search(fingerprint):
    "Tests a simple fingerprint search"

    api = AcoustID(os.environ['ACOUSTID_KEY'])
    resp = api.fingerprint(fingerprint, 291)

    assert type(resp) == list


def test_bad_fingerprint():
    "Sends a request with a bad fingerprint"

    api = AcoustID(os.environ['ACOUSTID_KEY'])

    with pytest.raises(exceptions.InvalidFingerprint):
        api.fingerprint('no-way-this-works', 1337)


def test_fingerprint_search_with_bad_duration(fingerprint):
    """Ensures the failure of a fingerprint request
    with a bad duration
    """

    api = AcoustID(os.environ['ACOUSTID_KEY'])

    with pytest.raises(exceptions.InvalidDuration):
        api.fingerprint(fingerprint, -1)

    with pytest.raises(exceptions.InvalidDuration):
        api.fingerprint(fingerprint, (0x8000))


def test_invalid_client_key():
    "Ensures invalid API keys are properly trapped"

    api = AcoustID('this-should-never-work')

    with pytest.raises(exceptions.InvalidClientKey):
        api.track(DEMO_TRACK)


def test_invalid_format():
    "Ensures API instance cannot be created with an invalid format"

    with pytest.raises(exceptions.UnknownFormat):
        api = AcoustID('bad-api-key', format='bson')
