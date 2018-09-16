import sys
import requests
from dateutil import parser

API_URL = "https://k-state.instructure.com/api/v1/courses"

API_KEY = sys.argv[2]

req_str = requests.get("https://k-state.instructure.com/api/v1/users/self/todo?access_token=" + API_KEY)

json_obj = req_str.json()
errors = False

f = open(sys.argv[1], "w")

for assignment in json_obj:
    f.write(assignment['assignment']['name']
            + ", " + parser.parse(assignment['assignment']['due_at']).strftime("%a %b %d")
            + "\n\n")
