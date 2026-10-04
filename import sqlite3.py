import sqlite3
import random
from datetime import datetime, timedelta

# Connect to the database
conn = sqlite3.connect('sweigartcats.db', isolation_level=None)

# Create the vaccinations table
conn.execute('''
    CREATE TABLE IF NOT EXISTS vaccinations (
        vaccine TEXT,
        date_administered TEXT,
        administered_by TEXT,
        cat_id INTEGER,
        FOREIGN KEY(cat_id) REFERENCES cats(rowid)
    ) STRICT
''')

# Get all cat IDs from the cats table
cat_ids = [row[0] for row in conn.execute('SELECT rowid FROM cats').fetchall()]

vaccine_types = ['rabies', 'FeLV', 'FVRCP']
vets = ['Dr. Echo', 'Dr. Luna', 'Dr. Felix', 'Dr. Whiskers']

for cat_id in cat_ids:
    num_vaccines = random.randint(0, 3)
    vaccines_given = random.sample(vaccine_types, k=num_vaccines)
    for vaccine in vaccines_given:
        # Generate a random date in the last 3 years
        days_ago = random.randint(0, 3 * 365)
        date_administered = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d')
        administered_by = random.choice(vets)
        conn.execute(
            'INSERT INTO vaccinations VALUES (?, ?, ?, ?)',
            (vaccine, date_administered, administered_by, cat_id)
        )