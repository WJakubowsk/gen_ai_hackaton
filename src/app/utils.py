import os

import matplotlib.pyplot as plt
import pandas as pd
import pyodbc
from pandasai import SmartDataframe


def create_df(query: str):
    """
    Creates a DataFrame from the SQL query
    Args:
        sql_query (str): The SQL query
    Returns:
        pd.DataFrame: The DataFrame
    """
    result = []
    with pyodbc.connect(os.getenv("DATABASE_CONN_STR")) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            row = cursor.fetchone()
            while row:
                result.append(row)
                row = cursor.fetchone()

    return pd.DataFrame.from_records(result, columns=columns)


def generate_plot(df: pd.DataFrame, user_query: str):
    """
    Generates a plot for the DataFrame
    Args:
        df (pd.DataFrame): The DataFrame
        query (str): User query
    """
    sdf = SmartDataframe(df, config={"open_charts": False})
    plt.ion()
    return sdf.chat(user_query)
