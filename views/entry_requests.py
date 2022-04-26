import sqlite3
import json
from models import Entry

def get_all_entries():
    """This function queries all journal entries"""
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id
        FROM entries e
        """)

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            entry = Entry(row['id'], row['concept'], row['entry'],
                            row['date'], row['mood_id'])

            entries.append(entry.__dict__)

    return json.dumps(entries)

def get_single_entry(id):
    """This function queries the database for one journal entry."""
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id
        FROM entries e
        WHERE e.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        entry = Entry(data['id'], data['concept'], data['entry'],
                            data['date'], data['mood_id'])

    return json.dumps(entry.__dict__)
