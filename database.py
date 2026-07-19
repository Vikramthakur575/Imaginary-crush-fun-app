import sqlite3
import os
from datetime import datetime

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "love_stories.db")

def init_db():
    """Initializes the database and creates the submissions table if it does not exist."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT,
                crush_name TEXT,
                meet_place TEXT,
                vibe TEXT,
                first_conv TEXT,
                realization TEXT,
                first_date TEXT,
                challenge TEXT,
                compatibility INTEGER,
                timestamp TEXT
            )
        """)
        conn.commit()
        conn.close()
    except Exception as e:
        # Silently catch or print to console so user experience never crashes
        print(f"Database initialization error: {e}")

def log_submission(user_name, crush_name, answers, compatibility):
    """
    Logs the user submission details safely.
    answers: dict containing meet_place, vibe, first_conv, realization, first_date, challenge
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO submissions (
                user_name, crush_name, meet_place, vibe, first_conv, 
                realization, first_date, challenge, compatibility, timestamp
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_name,
            crush_name,
            answers.get("meet_place", ""),
            answers.get("vibe", ""),
            answers.get("first_conv", ""),
            answers.get("realization", ""),
            answers.get("first_date", ""),
            answers.get("challenge", ""),
            compatibility,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Database logging error: {e}")
        return False
