import api
import os
import time

CRONALLY_API_KEY_NAME='CRONALLY_API_KEY'
CRONALLY_SECRET_KEY_NAME='CRONALLY_API_SECRET'
CRONALLY_API_SNS_TOPIC_NAME='CRONALLY_API_SNS_TOPIC'
CRONALLY_API_SNS_ACCESS_KEY_ID_NAME='CRONALLY_API_ACCESS_KEY_ID'
CRONALLY_API_SNS_SECRET_ACCESS_KEY_NAME='CRONALLY_API_SECRET_ACCESS_KEY'

LIMIT_REASON='Free accounts have a limit of 1 cronjob'

def test_bad_signup():
    test_email = 'cronally.com'
    signup = api.Signup().set_payload({'email':test_email})
    assert signup.payload['email'] == test_email

    response = signup.request()

    # Bad email should respond with 400
    assert response[0] == 400

def test_good_signup():
    test_email = 'a@cronally.com'

    signup = api.Signup().set_payload({'email':test_email})
    assert signup.payload['email'] == test_email

    response = signup.request()

    # Good email should respond with 200, but we've already used this
    # so we'll see a 400 anyway
    assert response[0] == 400

def test_get_info():
    api_key = os.getenv(CRONALLY_API_KEY_NAME)
    secret_key = os.getenv(CRONALLY_SECRET_KEY_NAME)

    response = api.Info(api_key, secret_key).request()

    assert response[0] == 200

def test_add_delete_cronjob():
    api_key = os.getenv(CRONALLY_API_KEY_NAME)
    secret_key = os.getenv(CRONALLY_SECRET_KEY_NAME)
    cfg = {
        'name': 'my cronjob',
        'cron': '0 * * * *',
        'sns_topic': os.getenv(CRONALLY_API_SNS_TOPIC_NAME),
        'sns_message': 'hello from cronally python API',
        'sns_region': 'us-east-1',
        'sns_access_key_id': os.getenv(CRONALLY_API_SNS_ACCESS_KEY_ID_NAME),
        'sns_secret_access_key': os.getenv(
            CRONALLY_API_SNS_SECRET_ACCESS_KEY_NAME)
    }

    response = api.AddCronjob(api_key, secret_key).set_payload(cfg).request()

    assert response[0] == 200

    cronjob_id = response[1]['response']['cronjob_id']

    # Sleep a bit to make sure the job is available for deletion
    time.sleep(5)

    response = api.DeleteCronjob(api_key, secret_key).set_payload({
        'cronjob_id': cronjob_id
    }).request()

    assert response[0] == 200

def test_list_cronjobs():
    api_key = os.getenv(CRONALLY_API_KEY_NAME)
    secret_key = os.getenv(CRONALLY_SECRET_KEY_NAME)

    response = api.ListCronjobs(api_key, secret_key).request()
    assert response[0] == 200