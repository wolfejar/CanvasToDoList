import sys
import requests
from dateutil import parser
import pytz

API_URL = "https://k-state.instructure.com/api/v1/courses"

API_KEY = sys.argv[2]

req_str = requests.get("https://k-state.instructure.com/api/v1/users/self/todo?access_token=" + API_KEY)

json_obj = req_str.json()
errors = False
f = open(sys.argv[1], "w")

for assignment in json_obj:
    due_date = parser.parse(assignment['assignment']['due_at']).astimezone(pytz.timezone("US/Central"))
    f.write(assignment['assignment']['name']
            + " due " + due_date.strftime("%A %b %d")
            + " at " + due_date.strftime("%-I")
            + ":" + due_date.strftime("%M %p") + "\n\n")
