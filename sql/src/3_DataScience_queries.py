from sqlalchemy import *

connection = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
census_copy = Table('census_copy', metadata, autoload=True, autoload_with=connection)

########################################################################################
# query 1
########################################################################################
# calculate weighted average age for 2008 population then group by sex
stmt = select([census_copy.columns.sex,
               (func.sum(census_copy.columns.age * census_copy.columns.pop2008) /
                func.sum(census_copy.columns.pop2008)).label('average_age')
               ])
stmt = stmt.group_by(census_copy.columns.sex)

results = connection.execute(stmt).fetchall()
print('RESULTS1:')
for result in results:
    print(result.sex, result.average_age)

########################################################################################
# query 2
########################################################################################
# calculate the percentage of females in 2000 and then group by state
stmt = select([census_copy.columns.state,
    (func.sum(
        case([
            (census_copy.columns.sex == 'F', census_copy.columns.pop2000)
        ], else_=0)) /
     cast(func.sum(census_copy.columns.pop2000), Float) * 100).label('percent_female')
])
stmt = stmt.group_by(census_copy.columns.state)

results = connection.execute(stmt).fetchall()
print('\n\nRESULTS2:')
for result in results:
    print(result.state, result.percent_female)

########################################################################################
# query 3
########################################################################################
# return state name and population difference from 2008 to 2000 then group by state
stmt = select([census.columns.state,
     (census.columns.pop2008-census.columns.pop2000).label('pop_change')
])
stmt = stmt.group_by(census.columns.state)

# order by population change
stmt = stmt.order_by(desc('pop_change'))
# limit to top 10
stmt = stmt.limit(10)
results = connection.execute(stmt).fetchall()
print('\n\nRESULTS3:')
for result in results:
    print('{}:{}'.format(result.state, result.pop_change))
