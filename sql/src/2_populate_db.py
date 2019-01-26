from sqlalchemy import create_engine, insert, MetaData, Table
import csv

values_list = []

with open('census.csv','r') as raw:
    csv_reader = csv.reader(raw)
    for row in csv_reader:
        data = {'state': row[0],
                'sex': row[1],
                'age':row[2],
                'pop2000': row[3],
                'pop2008': row[4]}
        values_list.append(data)


# an engine to connect to .sqlite database
connection = create_engine('sqlite:///census.sqlite')
# initialize metadata
metadata = MetaData()
census_copy = Table('census_copy', metadata, autoload=True, autoload_with=connection)

# insert statement
stmt = insert(census_copy)

results = connection.execute(stmt, values_list)
