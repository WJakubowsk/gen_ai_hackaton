from langchain.prompts import PromptTemplate

PROMPT_SUFFIX = """Only use the following tables:
{table_info}
Previous Conversation:
{history}
Question: {input}"""


_DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer. Unless the user specifies in his question a specific number of examples he wishes to obtain, always limit your query to at most {top_k} results. You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for a the few relevant columns given the question.
Under no circumstances should you create query thath would ALTER, CREATE, DROP, INSERT, UPDATE, DELETE, or TRUNCATE the database. You should only SELECT data from the database. That's really important.
Pay attention to use only the column names that you can see in the schema description. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Use the following format:
Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here
"""

PROMPT = PromptTemplate.from_template(
    _DEFAULT_TEMPLATE + PROMPT_SUFFIX,
)
