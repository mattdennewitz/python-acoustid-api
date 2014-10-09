from __future__ import unicode_literals
import os

import pytest


def data_path(filename):
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'data',
        filename
    )


@pytest.fixture(scope='function')
def fingerprint():
    "Query-ready fingerprint"

    return open(data_path('fingerprint-example.txt'), 'r').read()
