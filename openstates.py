#1. http://openstates.org/api/v1/legislators/?state=mo&chamber=upper&active=true
#2. http://openstates.org/api/v1/bills/?state=mo&search_window=session:2016
#3. http://openstates.org/api/v1/bills/?state=mo&search_window=session:2016&q=Drugs

import json, requests

url = 'http://openstates.org/api/v1/bills/?state=mo&search_window=session:2016&q=Drugs'

r = requests.get(url)

response_data = r.content

data = json.loads(response_data)

http = 'http://openstates.org/api/v1/bills/?state=mo&q=Drugs'

outcome = requests.get(http)
response = r.content

for result in data:
	print result['bill_id']
	print result['title']
	print result['session']
	print result['actions']
	for outcome in result:
		if ('actions' == ''):
		    print outcome['last']
	print outcome
	print '_______________'

