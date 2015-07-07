#!/usr/bin/python env

import util
import base64

def test_sign():
    key = base64.b64encode('abc')
    string_to_sign = '/account/GET200601021504'

    signature = util.sign(string_to_sign, key)
    assert util.verify(
        string_to_sign, key, signature) is True
