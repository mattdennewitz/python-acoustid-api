from __future__ import unicode_literals


class ApiRequestError(ValueError):
    "Base API error"


class UnknownFormat(ApiRequestError):
    """1 - Raised when requested response serialization format
    is unknown
    """


class MissingParameter(ApiRequestError):
    "2 - Raised when a required parameter is missing"


class InvalidFingerprint(ApiRequestError):
    "3 - Raised when a given fingerprint is invalid"


class InvalidClientKey(ApiRequestError):
    "4 - Raised when an invalid API key is used"


class InternalError(ApiRequestError):
    "5 - Raised when AcoustID throws up"


class InvalidUserApiKey(ApiRequestError):
    "6 - Raised when a given API for certain user is incorrect"


class InvalidUUID(ApiRequestError):
    "7 - Raised when a given track UUID is invalid"


class InvalidDuration(ApiRequestError):
    """8 - Raised when a given duration is signed
    or otherwise invalid
    """


class InvalidBitrate(ApiRequestError):
    """9 - Raised when a given bitrate is signed
    or otherwise invalid
    """


class InvalidForeignID(ApiRequestError):
    """10 - Raised when a given vendor id does not follow
    "vendor:id" format
    """


class InvalidMaxDurationDiff(ApiRequestError):
    """11 - Raised when duration lies outside of
    fingerprint boundaries
    """


class NotAllowed(ApiRequestError):
    "12 - You're not allowed to do that"


class ServiceUnavailable(ApiRequestError):
    "13 - Raised when service is unavailable"


class TooManyRequests(ApiRequestError):
    """14 - Raised when this client or API key is exceeding
    the speed limit
    """
