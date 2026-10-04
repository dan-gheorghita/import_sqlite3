# import sqlite3.py

**Database Population Script**

This Python script is designed to populate a SQLite database with sample vaccination records for cats. The script assumes the existence of a `cats` table and creates a new `vaccinations` table with foreign key constraints.

### Functionality Overview

The script performs the following tasks:

1. **Database Connection**: Establishes a connection to a SQLite database named `sweigartcats.db`.
2. **Table Creation**: Creates a `vaccinations` table with columns for vaccine type, date administered, administered by, and cat ID, as well as a foreign key constraint referencing the `cats` table.
3. **Cat ID Retrieval**: Retrieves all unique cat IDs from the `cats` table.
4. **Vaccine Simulation**: For each cat ID, generates a random number of vaccination records between 0 and 3. Each record consists of:
	* A random vaccine type (rabies, FeLV, or FVRCP).
	* A date