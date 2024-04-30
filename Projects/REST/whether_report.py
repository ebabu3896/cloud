import requests
import pytest
import json

ENDPOINT="https://todo.pixegami.io"
def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert requests.status_codes == 200

def test_can_create_task():
    payload = {
        'content' : 'my_test content',
        'user_id' : 'test_user',
        'task_id' : 'test_task_id',
        'is_done' : False
    }
    response = requests.put(ENDPOINT + "/create-task", json=payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    data_Str = json.dumps(data, indent=4)
    print(data_Str)


emails = """
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""
import re
pattern = re.compile('[a-zA-Z0-9-]+@[a-zA-Z-]+\.[a-zA-Z-]+')

matches = pattern.finditer(emails)

for mat in matches:
    print(mat)
    print(mat.group(0))

# <re.Match object; span=(1, 25), match='pythonengineer@gmail.com'>
# pythonengineer@gmail.com
# <re.Match object; span=(26, 48), match='Python-engineer@gmx.de'>
# Python-engineer@gmx.de
# <re.Match object; span=(49, 81), match='python-engineer123@my-domain.org'>
# python-engineer123@my-domain.org