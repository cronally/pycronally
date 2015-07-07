#!/usr/bin/env python
import hashlib
import hmac
import base64



def ct_compare(a, b):
    """
    ** From Django source **

    Run a constant time comparison against two strings

    Returns true if a and b are equal.

    a and b must both be the same length, or False is
    returned immediately
    """
    if len(a) != len(b):
        return False

    result = 0
    for ch_a, ch_b in zip(a, b):
        result |= ord(ch_a) ^ ord(ch_b)
    return result == 0

"""
Generate HMAC for string_to_sign using SHA256 hash, returning a base64-encoded
digest. Key should be base64-encoded

"""
def sign(string_to_sign, key):
    h = hmac.new(base64.b64decode(key), string_to_sign, hashlib.sha256)
    return base64.b64encode(h.digest())

"""
Verify provided signature matches calculated signature. Signature should be
provided as base64 encoded string

"""
def verify(string_to_sign, key, signature):
    decoded_sig = base64.b64decode(signature)

    # We have to decode the signed string because we're re-using the signing
    # function above which returns an encoded string
    calculated_sig = base64.b64decode(sign(string_to_sign, key))

    return ct_compare(calculated_sig, decoded_sig)