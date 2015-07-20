import requests
import json
from sys import argv

script, auth = argv
r = requests.get("https://api.vimeo.com/me", headers={"Authorization": "bearer %s" % auth } )
parsed_json = json.loads(r.text)


free_space = (parsed_json['upload_quota']['space']['free'])
file_size = 738737362612182376
if free_space == 0:
  print "Can't upload, quota has been exceeded."
else:
  print "Uploading is fine, now we need to determine if file size exceeds remaining free space"
  if file_size < free_space:
    print "Can start the uploading porcess as we have enough space left."
  else:
    print "Not enough quota for this file, try another file perhaps?"
