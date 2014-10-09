"""Talks to AcoustID server, answers questions about your tracks.
"""

from __future__ import unicode_literals
import urlparse

import requests

from . import consts, exceptions


class AcoustID(object):
    """Simple API wrapper for AcoustID.

    For more information about the API,
    check out http://acoustid.org/webservice.
    """

    LOOKUP_PATH = '/v2/lookup'

    def __init__(self, client_key, host=None, format='json'):
        self.client_key = client_key
        self.host = host or consts.DEFAULT_HOST

        if not format in consts.FORMATS:
            raise exceptions.UnknownFormat('"format" must be one of {%s}' %
                                           ', '.join(consts.FORMATS))
        self.format = format

        self._session = None

    def _dispatch(self, method, path, params=None, data=None,
                  return_key='results'):
        "Internal request processor"

        if not self._session:
            self._session = requests.Session()

        url = urlparse.urljoin(self.host, path)
        req = requests.Request(method, url, params=params, data=data)
        req = req.prepare()

        print req.url

        resp = self._session.send(req)
        resp_body = resp.json()

        if resp_body['status'][0] == 'e':
            self._handle_error(resp_body['error'])

        # send back the results
        return resp_body[return_key]

    def _handle_error(self, error):
        "Spins a raw error code into a useful exception"

        msg = error.get('message', 'Unknown error')

        if error['code'] in consts.ERRORS:
            raise consts.ERRORS[error['code']](msg)

        # what returned was unexpected
        raise exceptions.ApiRequestError(msg)

    def _get_params(self, extra=None):
        params = {
            'format': self.format,
            'client': self.client_key,
        }

        if extra is not None:
            params.update(extra)

        # flatten "meta" list
        if ('meta' in params
            and isinstance(params['meta'], (list, set, tuple))):
            params['meta'] = ' '.join(params['meta'])

        return params

    def track(self, track_id, meta=None):
        "Returns results for lookup via single track id"

        params = self._get_params(extra={
            'trackid': track_id,
            'meta': meta,
        })

        return self._dispatch('GET', self.LOOKUP_PATH, params=params)

    def fingerprint(self, fingerprint, duration, meta=None):
        "Returns results for fingerprint-based lookup"

        if duration <= 0 or duration > 0x7fff:
            raise exceptions.InvalidDuration('Duration %s is invalid' %
                                             duration)

        params = self._get_params(extra={
            'fingerprint': fingerprint,
            'duration': duration,
            'meta': meta,
        })

        return self._dispatch('GET', self.LOOKUP_PATH, params=params)

    def acoustids_for_mbid(self, mbid=None):
        "Returns AcoustIDs for a single MusicBrainz id"

        # batch implementation will be availble when
        # multi-mbid responses aren't 500'ing
        params = self._get_params(extra={
            'batch': 0,
            'mbid': mbid,
        })

        return self._dispatch('GET', '/v2/track/list_by_mbid', params=params,
                              return_key='tracks')
