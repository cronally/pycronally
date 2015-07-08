# pycronally
Cronally Python API

#### Create a cron job
```
import pycronally.api

api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

cronjob_cfg = {
	'name': 'my hourly cronjob',
	'cron': '0 * * * *',
	'sns_topic': 'YOUR_SNS_TOPIC',
	'sns_message': 'Hello from pycronally',
	'sns_region': 'YOUR_SNS_REGION',
	'sns_access_key_id': 'YOUR_SNS_ACCESS_KEY_ID',
	'sns_secret_access_key': 'YOUR_SNS_SECRET_ACCESS_KEY'
}

response = pycronally.api.AddCronjob(
	api_key, api_secret).set_payload(cronjob_cfg).request()
```

#### List cron jobs
```
import pycronally.api

api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

response = pycronally.api.ListCronjobs(api_key, api_secret).request()
```

#### Delete cron job
```
import pycronally.api

api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

response = pycronally.api.DeleteCronjob(api_key, api_secret).set_payload({
  'cronjob_id': 'CRONJOB_ID'
}).request()
```
