import os
import sqlite3
import logging
import json
import time
from datetime import datetime

#Konfigurējam žurnālu ierakstīšanu ar norādītu formātu un līmeni.

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("migration_logger")

#Ielādējam datubāzes ceļu no konfigurācijas faila.

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

DATABASE_PATH = config["database_path"]

#Izveido un atgriež savienojumu ar SQLite datubāzi, izmantojot norādīto ceļu.

def create_connection():
    return sqlite3.connect(DATABASE_PATH)

#Nodrošina, ka pastāv 'migrations' tabula, kurā tiek glabāti piemēroto migrāciju dati.

def ensure_migrations_table_exists(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS migrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            exec_ts INTEGER,
            exec_dt TEXT
        )
    ''')
    conn.commit()

#Pārbauda, vai norādītā migrācija jau ir piemērota, izmantojot tās nosaukumu.

def is_migration_applied(conn, migration_name):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM migrations WHERE name = ?", (migration_name,))
    return cursor.fetchone()[0] > 0

#Piemēro norādīto migrāciju, izpildot SQL skriptu un reģistrējot tās piemērošanas datus tabulā.

def apply_migration(conn, migration_name, migration_sql):
    try:
        cursor = conn.cursor()
        cursor.executescript(migration_sql)
        timestamp = int(time.time())
        exec_date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("INSERT INTO migrations (name, exec_ts, exec_dt) VALUES (?, ?, ?)",
                       (migration_name, timestamp, exec_date))
        conn.commit()
        logger.info(f"Migration {migration_name} applied successfully.")
    except sqlite3.Error as e:
        logger.error(f"Failed to apply migration {migration_name}: {e}")
        conn.rollback()

#Atrod un izpilda visas nepielietotās migrācijas no norādītās mapes.

def run_migrations():
    conn = create_connection()
    ensure_migrations_table_exists(conn)

#Norāda migrāciju failu mapi.

    migrations_path = "./migrations"
    migration_files = sorted([f for f in os.listdir(migrations_path) if f.endswith('.sql')])


    for migration_file in migration_files:
        if not is_migration_applied(conn, migration_file):
            with open(os.path.join(migrations_path, migration_file), 'r') as file:
                migration_sql = file.read()
                logger.info(f"Applying migration: {migration_file}")
                apply_migration(conn, migration_file, migration_sql)
        else:
            logger.info(f"Migration {migration_file} already applied.")

    conn.close()
    logger.info("All migrations complete.")

if __name__ == "__main__":
    run_migrations()
