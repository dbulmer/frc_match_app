
# FRC Match Data App

This application automatically fetches **match data** for a configured FRC team from [The Blue Alliance](https://www.thebluealliance.com/) and displays the data in a live-updating web dashboard.

---

## ⚙️ Features

✅ Configurable **Team Number** and **Event Code** (via `config.json`)  
✅ Polls for new data every **60 seconds**  
✅ Stores data in **SQLite database** (`matches.db`)  
✅ Displays match data in a clean **web table**  
✅ Highlights a configurable "focus team" (e.g., alliance partner or scouting target)  
✅ Tracks **win/loss** for the focus team  
✅ Automatically displays time in **local timezone**  
✅ Works on **Windows 11** and **Raspberry Pi**  

---

## 📁 Folder Structure

```
frc_match_app/
├── app.py                  # Main Flask app
├── database.py              # SQLite handler
├── poller.py                 # Data fetcher
├── config.json               # Stores team/event/api key
├── requirements.txt          # Python dependencies
├── templates/
│   └── index.html            # HTML for the table display
└── README.md                  # This file!
```

---

## ⚙️ Prerequisites

- Python 3.9+ recommended
- Works on both **Windows** and **Raspberry Pi**
- Required Python packages (see `requirements.txt`):
    ```
    flask
    requests
    pytz
    ```

---

## 📦 Installation

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/frc_match_app.git
cd frc_match_app
```

---

### 2️⃣ Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Raspberry Pi:
source venv/bin/activate
```

---

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure `config.json`

Edit `config.json` with your own **TBA API Key**, **Team Number**, **Event Code**, and the **Highlight Team** you want to track:

```json
{
    "TBA_API_KEY": "your_tba_api_key_here",
    "TEAM_NUMBER": "frc1023",
    "EVENT_CODE": "2025mimil",
    "HIGHLIGHT_TEAM": "frc6570"
}
```

---

### 5️⃣ Run the App

```bash
python app.py
```

---

### 6️⃣ Open the Dashboard

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📊 What You’ll See

| Match # | Red Teams | Blue Teams | Blue Score | Red Score | Win/Loss (6570) | Time (Local) |
|---|---|---|---|---|---|---|
| 1 | 6570, 1023 | 3542, 548 | 120 | 110 | Win | 2025-03-21 12:35 |
| 2 | ... | ... | ... | ... | ... | ... |

---

## 🔄 Automatic Updates

- Every 60 seconds, the app fetches new data from TBA.
- The page auto-refreshes every 60 seconds to show fresh data.
- Matches are sorted by **match number** (ascending).

---

## 🚀 Deployment (optional)

- To run this automatically on a Raspberry Pi, add to `cron` or `systemd`.
- You can also run it in the background using:
    ```
    nohup python app.py &
    ```

---

## 💡 Future Ideas

✅ Add charting to visualize team performance  
✅ Add filters to select specific matches  
✅ Add export to CSV/Excel  

---

## 📧 Questions?

Feel free to reach out if you need help setting this up on your robot shop laptop, scouting station, or field-side Pi!

---

## 🎉 Happy Scouting!
