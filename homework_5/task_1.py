import requests
import ujson

base_url = "http://pulse-rest-testing.herokuapp.com/"

payload = {
    'type': 'QA',
    'name': 'Paul'
}

create_user = requests.post(base_url + 'roles/', data=payload)
result = create_user.json()

print(result['id'], result['name'])

id = str(result['id'])
check_user = requests.get(base_url + 'roles/' + id + '/')

if check_user != "0":
    print("User create is done. ID new user: ", id)

check_user_list = ujson.loads(requests.get(base_url + 'roles/').text)
print(check_user_list)

for key in check_user_list:
    if check_user_list["Paul"]: print("New user is in the list")