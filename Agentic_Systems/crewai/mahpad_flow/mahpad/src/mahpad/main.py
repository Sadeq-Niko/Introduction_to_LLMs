#!/usr/bin/env python
import os
import json
import re
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from mahpad.crews.nl_to_sql.nl_to_sql import NlToSql
from mahpad.crews.reporter.reporter import Reporter

import psycopg2
from psycopg2.extras import RealDictCursor


class QueryState(BaseModel):
    user_query: str = ""
    sql_query: str = ""
    retrieved_data: list = []
    report: str = ""

def clean_json(text):
    # Regex to capture the first valid JSON object in the text
    match = re.search(r'\{[\s\S]*\}', text)
    if not match:
        raise ValueError("No JSON object found in the text.")
    
    json_str = match.group(0)
    
    # Clean trailing commas that break JSON
    json_str = re.sub(r",\s*]", "]", json_str)  # remove trailing commas in arrays
    json_str = re.sub(r",\s*}", "}", json_str)  # remove trailing commas in objects

    return json.loads(json_str)

def out(input, f):
    with open(f'output/{f}.json','w') as file:
        json.dump(input,file)


class QueryFlow(Flow[QueryState]):

    @start()
    def query_translation(self):
        # self.state.user_query = input("Please Enter the query ...\n\n\n\n")
        queries = ["Show me all orders placed by Alice.","What is the total revenue from shipped orders?","List all orders from February 2025.","How many orders has each customer made?","Show me the most expensive orders, sorted by price descending.","Find all cancelled orders by Bob."]
        self.state.user_query = queries[2]
        result = NlToSql().crew().kickoff(
            inputs={'query': self.state.user_query}
        )
        self.state.sql_query = clean_json(result.raw)
        print(f"User query has been translated to\n{self.state.sql_query}\n########################")

    @listen(query_translation)
    def data_retrieval(self):
        conn = psycopg2.connect(
            dbname='n8n-db',
            user="n8n-user",
            password="123456",
            host="127.0.0.1",
            port="5432",
            cursor_factory=RealDictCursor
        )

        cur = conn.cursor()
        cur.execute(self.state.sql_query['sql_query'])
        rows = cur.fetchall()
        rows = [str(row) for row in rows]
        self.state.retrieved_data = rows
        print(f"Retrieved data after excecution of SQL query:\n{self.state.retrieved_data}\n########################")


    @listen(data_retrieval)
    def reporter(self):
        result = Reporter().crew().kickoff(
            inputs= {"retrieved_data": self.state.retrieved_data}
        )
        self.state.report = result.raw
        out({"user_query":self.state.user_query,"sql_query":self.state.sql_query,"retrieved_data":self.state.retrieved_data,"report":self.state.report},"Final_State")
        print(f'Final Report:\n{self.state.report}\n########################')
        print("End of process!")


def kickoff():
    flow = QueryFlow()
    flow.kickoff()


def plot():
    flow = QueryFlow()
    flow.plot()


if __name__ == "__main__":
    kickoff()
