#!/usr/bin/env python

import requests
import util
import datetime


CRONALLY_HOST='https://api.cronally.com'
HEADER_DATETIME_FORMAT='%Y%m%d%H%M'
CONTENT_TYPE='application/x-www-form-urlencoded'

"""
Base class for API requests

"""
class APIRequest(object):
    """
    Initialize APIRequest with api_key and secret

    """
    def __init__(self, api_key=None, secret_key=None):
        self.api_key = api_key
        self.secret_key = secret_key

        # Initialize extra_headers
        self.extra_headers = {
            'Content-Type': CONTENT_TYPE
        }

        # Initialize payload
        self.payload = {}

    def set_payload(self, payload):
        self.payload = payload
        return self

    """
    Build URI from host and path components

    """
    def build_uri(self):
        return '{}{}'.format(CRONALLY_HOST, self.endpoint)


    """
    Handle request

    """
    def request(self):
        # Check if signature is required
        if self.signed:
            self.sign_request()

        if self.verb == 'POST':
            r = requests.post(self.build_uri(), data=self.payload,
                              headers=self.extra_headers)

        if self.verb == 'DELETE':
            url = self.build_uri().format(**self.payload)
            r = requests.delete(url, headers=self.extra_headers)

        if self.verb == 'GET':
            r = requests.get(self.build_uri(), headers=self.extra_headers)

        return r.status_code, r.json()

    """
    Handle request signature generation
    """
    def sign_request(self):
        utcnow = datetime.datetime.utcnow()
        string_to_sign = '{}{}{}'.format(
            self.endpoint.format(**self.payload),
            self.verb,
            utcnow.strftime(HEADER_DATETIME_FORMAT))

        self.extra_headers = {
            'X-Cron-Key': self.api_key,
            'X-Cron-Date': utcnow.strftime(HEADER_DATETIME_FORMAT),
            'X-Cron-Signature': util.sign(string_to_sign, self.secret_key)
        }

"""
Functionality for signup requests

"""
class Signup(APIRequest):

    # Does not require a signed request
    signed = False

    # Endpoint
    endpoint = '/account/'

    # Verb
    verb = 'POST'

    def __init__(self):
        super(Signup, self).__init__()

"""
Functionality for info requests

"""
class Info(APIRequest):

    # Requires a signed request
    signed = True

    # Endpoint
    endpoint = '/account/'

    # Verb
    verb = 'GET'

    def __init__(self, api_key, secret_key):
        super(Info, self).__init__(api_key, secret_key)


"""
Functionality for add cron job requests

"""
class AddCronjob(APIRequest):

    # Requires a signed request
    signed = True

    # Endpoint
    endpoint = '/cronjob/'

    # Verb
    verb = 'POST'

    def __init__(self, api_key, secret_key):
        super(AddCronjob, self).__init__(api_key, secret_key)


"""
Functionality for list cron jobs requests

"""
class ListCronjobs(APIRequest):

    # Requires a signed request
    signed = True

    # Endpoint
    endpoint = '/cronjobs/'

    # Verb
    verb = 'GET'

    def __init__(self, api_key, secret_key):
        super(ListCronjobs, self).__init__(api_key, secret_key)


"""
Functionality for delete cron jobs requests

"""
class DeleteCronjob(APIRequest):

    # Requires a signed request
    signed = True

    # Endpoint
    endpoint = '/cronjob/{cronjob_id}/'

    # Verb
    verb = 'DELETE'

    def __init__(self, api_key, secret_key):
        super(DeleteCronjob, self).__init__(api_key, secret_key)


