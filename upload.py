import requests
import json
from sys import argv

script, auth = argv
r = requests.get("https://api.vimeo.com/me", headers={"Authorization": "bearer %s" % auth } )
parsed_json = json.loads(r.text)
print(parsed_json['upload_quota']['space']['free'])

