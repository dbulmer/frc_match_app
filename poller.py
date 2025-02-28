import requests
import json
from database import store_match

# Load configuration
with open('config.json') as f:
    config = json.load(f)

TBA_API_KEY = config['TBA_API_KEY']
TEAM = config['TEAM_NUMBER']
EVENT = config['EVENT_CODE']

URL = f"https://www.thebluealliance.com/api/v3/team/{TEAM}/event/{EVENT}/matches"

HEADERS = {
    'X-TBA-Auth-Key': TBA_API_KEY
}

def poll_matches():
    print(f"Polling data for {TEAM} at {EVENT}...")
    response = requests.get(URL, headers=HEADERS)

    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        return

    matches = response.json()

    for match in matches:
        store_match(match)

    print(f"Stored {len(matches)} matches.")
