import psycopg2
from decouple import config

def insert_entries(table_name):
    with open(f'data/{table_name}.csv', 'r') as file:
        lines = [ i.strip().split(',') for i in file.readlines() ]

        # Format the values by type and insert them into the values list
        for line in lines:
            values = ""

            # Add quotes only if a string
            for i in line:
                try:
                    int(i)
                    values += f", {i}"
                except ValueError:
                    # Format correctly if date
                    if '/' in i:
                        date = i.replace('/', '')
                        values += f", '{date[4:]}/{date[2:4]}/{date[:2]}'"
                    else:
                        values += f", '{i}'"

            # Execute the query when all values areaadded
            cur.execute(f"INSERT INTO {table_name} VALUES({values[2:]})")
            con.commit()


# Database connection options
dbname   = config('DATABASE_NAME')
user     = config('USER')
password = config('PASSWORD')

# Connect the database
con = psycopg2.connect(dbname=dbname, user=user, password=password)
cur = con.cursor()

# Insert entries for each table
table_names = ['author', 'client', 'book', 'borrower']
for i in table_names:
    insert_entries(i)
