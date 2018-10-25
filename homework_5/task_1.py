import requests

base_url = "http://pulse-rest-testing.herokuapp.com/"

payload = {
    'type': 'QA',
    'name': 'Paul'
}

create_user = requests.post(base_url+'roles/', data=payload)
result = create_user.json()
print(result)
print(result['id'], result['name'])
