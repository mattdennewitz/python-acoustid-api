from __future__ import unicode_literals

from . import exceptions


DEFAULT_HOST = 'http://api.acoustid.org/'

FORMATS = ('json', 'jsonp', 'xml')

META = (
    'recordings', 'recordingids', 'releases', 'releaseids',
    'releasegroups', 'releasegroupids', 'tracks', 'compress',
    'usermeta', 'sources'
)

ERRORS = {
    1: exceptions.UnknownFormat,
    2: exceptions.MissingParameter,
    3: exceptions.InvalidFingerprint,
    4: exceptions.InvalidClientKey,
    5: exceptions.InternalError,
    6: exceptions.InvalidUserApiKey,
    7: exceptions.InvalidUUID,
    8: exceptions.InvalidDuration,
    9: exceptions.InvalidBitrate,
    10: exceptions.InvalidForeignID,
    11: exceptions.InvalidMaxDurationDiff,
    12: exceptions.NotAllowed,
    13: exceptions.ServiceUnavailable,
    14: exceptions.TooManyRequests,
}
