import sqlite3

DB_FILE = 'matches.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            match_key TEXT PRIMARY KEY,
            comp_level TEXT,
            match_number INTEGER,
            blue_score INTEGER,
            red_score INTEGER,
            blue_teams TEXT,
            red_teams TEXT,
            time INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def store_match(match):
    if match['comp_level'] != 'qm':
        return  # Skip non-qualification matches

    blue_teams = ','.join(match['alliances']['blue']['team_keys'])
    red_teams = ','.join(match['alliances']['red']['team_keys'])

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT OR REPLACE INTO matches (
            match_key, comp_level, match_number, 
            blue_score, red_score, 
            blue_teams, red_teams, 
            time
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        match['key'],
        match['comp_level'],
        match['match_number'],
        match['alliances']['blue']['score'],
        match['alliances']['red']['score'],
        blue_teams,
        red_teams,
        match['time']
    ))
    conn.commit()
    conn.close()

def get_all_matches():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        SELECT match_key, comp_level, match_number, 
               blue_score, red_score, 
               blue_teams, red_teams, 
               time
        FROM matches
        WHERE comp_level = 'qm'
        ORDER BY match_number ASC
    ''')
    matches = c.fetchall()
    conn.close()
    return matches
