import pandas as pd 
from sqlalchemy import create_engine
from config import username, password

engine = create_engine(f'postgresql://{username}:{password}@10.80.3.51:5432/epace')

from sqlalchemy import inspect
inspector = inspect(engine)


# Given a table name, return the columns associated with it
def return_column_names_from_table(table_name):

    print(f"TABLE SCHEMA FOR {table_name}:")
    print("-----------------")

    for column in inspector.get_columns(table_name):
        print("Column: %s" % column['name'])

# Grab a table from the DB and save as a dataframe
def grab_table_as_dataframe(table_name):
    connection = engine.connect()
    table = pd.read_sql(f"SELECT ccmasterid FROM {table_name}", connection)
    print(table['jobproject'].value_counts())


# Run Statements
table_name = "job"

#return_column_names_from_table(table_name)
#grab_table_as_dataframe(table_name)
#print(engine.table_names())






