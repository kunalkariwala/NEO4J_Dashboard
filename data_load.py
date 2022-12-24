from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Mobile@11"))
session=driver.session()
 
q1="""
call apoc.periodic.iterate('call apoc.load.csv("/Users/kunal/Desktop/SOP/neo4j/NEO4J_DASHBOARD/results.csv")
yield map as row return row
','
merge(c:Country{Name:row.country})
merge(ci:City{Name:row.city})
merge(m:Game{Name:row.tournament,played_on:row.date,home_team:row.home_team,away_team:row.away_team,home_score:row.home_score,away_score:row.away_score})
merge(c)-[:HAS]->(ci)
merge(m)-[:PLAYED_ON]->(ci)
', 
{batchSize:1000,iterateList:true,parallel:true,retries:20})
""" 
q1="""
call apoc.load.csv("file:///station_vs_trains.csv")
yield lineNo,map,list
"""
results=session.run(q1).data()
for row in results:
    print(row)
# session.run(q1)