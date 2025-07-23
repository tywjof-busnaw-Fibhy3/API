import requests

access_token = 'EAAPath96o9ABPDZBDx4HbZBCo71AQHn01rU5kTBY69mlUSBuZCnRDfZBfrGL7xHxT8LRyWehlWh37fRktMG9rsnv4b0EAW53IYIisz8ZAl2Vsx1ZAwtCkAoMkGeokSr99L4iKpWWg40jMeidDcR3eVg9ZC5H3kavNiNQTgKjYMqZB9ulQsSrVUEXA7qY3ZC0pJbDzFgtSMtO4roMDUw4pmPAby49zcrQv6HuU6Kg63PZCv2PCWO20l'
url = 'https://graph.facebook.com/v23.0/me'
params = {
    'fields': 'id,name',
    'access_token': access_token
}

response = requests.get(url, params=params)
print(response.json())
# ตรวจสอบสถานะการตอบกลับ
if response.status_code == 200:
    data = response.json()
    print(f"ID: {data['id']}, Name: {data['name']}")
else:
    print(f"Error: {response.status_code}, {response.text}")
