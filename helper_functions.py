import pandas as pd

def get_table_list(conn):
    query = "select name from sqlite_master where type='table';"
    table_names = [r[0] for r in conn.execute(query).fetchall()]
    return table_names


def load_table(conn, table_name):
    query = f"select * from {table_name}"
    df = pd.read_sql(query, conn)
    return df



def convert_dollars_to_int(df, col):
    df[col] = df[col].str.replace("$", "").str.replace(",", "").astype('int')
    return df
