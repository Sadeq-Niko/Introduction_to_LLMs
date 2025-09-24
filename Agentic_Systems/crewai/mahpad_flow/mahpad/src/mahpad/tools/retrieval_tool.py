from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json
import psycopg2
from psycopg2.extras import RealDictCursor


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    sql_query: str = Field(..., description="An SQL query to be executed on a database")

class Retrieve_From_Database(BaseTool):
    name: str = "Retrieve From Database"
    description: str = (
        "Execute a query on database"
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, sql_query: str) -> str:
        
        conn = psycopg2.connect(
            dbname='n8n-db',
            user="n8n-user",
            password="123456",
            host="127.0.0.1",
            port="5432",
            cursor_factory=RealDictCursor
        )

        cur = conn.cursor()
        cur.execute(f"""{sql_query}""")
        rows = cur.fetchall()
        rows = [str(row) for row in rows]

        with open('output/retrieved.json','w') as file:
            json.dump(rows,file)

        return rows

if __name__=="__main__":
    print(Retrieve_From_Database()._run(sql_query="select * from employees;"))