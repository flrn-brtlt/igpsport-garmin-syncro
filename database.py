import sqlite3

DB = "sync_history.db"

def create_db():
    conn = sqlite3.connect(DB)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS synced(
            ride_id TEXT PRIMARY KEY
        )
    """)

    conn.commit()
    conn.close()


def already_synced(ride_id):

    conn = sqlite3.connect(DB)

    result = conn.execute(
        "SELECT ride_id FROM synced WHERE ride_id=?",
        (str(ride_id),)
    ).fetchone()

    conn.close()

    return result is not None


def mark_synced(ride_id):

    conn = sqlite3.connect(DB)

    conn.execute(
        "INSERT OR IGNORE INTO synced VALUES (?)",
        (str(ride_id),)
    )

    conn.commit()
    conn.close()