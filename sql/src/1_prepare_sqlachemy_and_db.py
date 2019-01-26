from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer

# an engine to connect to .sqlite database
engine = create_engine('sqlite:///census.sqlite')

# initialize metadata
metadata = MetaData()

# check out table names
tables = engine.table_names()
print('tables in census.sqlite: {}'.format(tables))

# check out features (columns) from every table in db
for table in tables:
    census = Table(table, metadata, autoload=True, autoload_with=engine)
    print(repr(census))

# Build a copycat table of census table (already stored in census.sqlite db)
census_copy = Table('census_copy', metadata,
               Column('state', String(30)),
               Column('sex', String(1)),
                Column('age', Integer()),
                Column('pop2000', Integer()),
                Column('pop2008', Integer()))

# Create the table in the database
metadata.create_all(engine)

# check out table names again
tables = engine.table_names()
print('tables in census.sqlite: {}'.format(tables))
success = 0 # successfulness of creation flag
for table in tables:
    if(table == 'census_copy'):
        success = 1
    else: pass
if (success == 1):
    print('census_copy table successfully created')
else:
    print('census_copy table unsuccessfully created')
