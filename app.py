from flask import Flask, render_template
import threading
import time
import json
from database import get_all_matches, init_db
from poller import poll_matches
import pytz
from datetime import datetime

# Load config
with open('config.json') as f:
    config = json.load(f)

TEAM_NUMBER = config['TEAM_NUMBER'].replace("frc", "")
EVENT_CODE = config['EVENT_CODE']
HIGHLIGHT_TEAM = config['HIGHLIGHT_TEAM']

app = Flask(__name__)

def datetimeformat(value):
    local_timezone = datetime.now().astimezone().tzinfo  # Detect system timezone
    local_time = datetime.fromtimestamp(value, tz=local_timezone)
    return local_time.strftime('%Y-%m-%d %H:%M')

app.jinja_env.filters['datetimeformat'] = datetimeformat

@app.route('/')
def index():
    matches = get_all_matches()
    return render_template('index.html', 
                           matches=matches, 
                           team=TEAM_NUMBER, 
                           event=EVENT_CODE, 
                           highlight_team=HIGHLIGHT_TEAM)
def run_poller():
    while True:
        poll_matches()
        time.sleep(60)

if __name__ == '__main__':
    init_db()
    poller_thread = threading.Thread(target=run_poller, daemon=True)
    poller_thread.start()
    app.run(host='0.0.0.0', port=5000, debug=True)
