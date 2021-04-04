import json
import os

# uncomment when run this on spartan - because on spartan it is a superlink
# path1 = os.readlink('./tinyTwitter.json')
# path2 = os.readlink('./bigTwitter.json')

with open('./tinyTwitter.json') as f:
  data = json.load(f)
print(data['metadata'])