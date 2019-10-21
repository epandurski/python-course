import requests
import sys
from json.decoder import JSONDecodeError

r = requests.get('http://localhost:8000/demo.json')

r.raise_for_status()
# if r.status_code != 200:
#     print(f'Error {r.status_code}')
#     sys.exit(2)

print(r.headers)
try:
    obj = r.json()
except JSONDecodeError:
    print('This is not a valid JSON!')
    sys.exit(2)

print(obj)
customers = obj['customers']
customers_by_id = {c['id']: c for c in customers}
print(customers_by_id)
if 2 in customers_by_id:
    print('===== Customer 2 =====')
    print(customers_by_id[2])
else:
    print('Can not find customer 2')
