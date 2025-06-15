import pandas as pd
import sqlite3
import transform

def create_database(db_name: str) -> None:
    """
    Cria um banco de dados SQLite.

    Args:
        db_name (str): Nome do banco de dados.
    """
    conn = sqlite3.connect(db_name)
    conn.close()
    print(f"Database {db_name} created")   

def create_table(db_name: str, table_name: str) -> None:
    """
    Cria uma tabela no banco de dados SQLite.

    Args:
        db_name (str): Nome do banco de dados.
        table_name (str): Nome da tabela.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            year INTEGER,
            value INTEGER,
            unit TEXT,
            flag TEXT,
            country TEXT,
            item TEXT,
            domain TEXT,
            metric TEXT,
            yoy FLOAT,
            UNIQUE(year, flag, country)
        )
    """)
    conn.commit()
    conn.close()
    print(f"Table {table_name} created in {db_name}")

def insert_data(df: pd.DataFrame, db_name: str, table_name: str) -> None:
    """
    Insere dados em uma tabela do banco de dados SQLite.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados.
        db_name (str): Nome do banco de dados.
        table_name (str): Nome da tabela.
    """
    conn = sqlite3.connect(db_name)
    sql: str = f"""
        INSERT OR REPLACE INTO {table_name} (year, value, unit, flag, country, item, domain, metric, yoy)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    for _, row in df.iterrows():
        conn.execute(sql, (row["year"], row["value"], row["unit"], row["flag"], row["country"], row["item"], row["domain"], row["metric"], row["yoy"]))
    conn.commit()
    print(f"Inserted {len(df)} rows into {table_name}")
    conn.close()
    print(f"Data inserted into {table_name} in {db_name}")

def extract_data(db_name: str, table_name: str) -> pd.DataFrame:
    """
    Extrai os dadados do Data Warehouse.

    Args:
        db_name (str): Nome do banco de dados.
        table_name (str): Nome da tabela.
    Returns:
        pd.DataFrame: DataFrame do pandas com os dados lidos.
    """
    conn = sqlite3.connect(db_name)
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)    

if __name__ == "__main__":
    db_name = "databases/stage.db"
    table_name = "trigo"

    df = transform.read_sqlite(db_name, table_name)
    transform.analyze_data(df)
    df = transform.yoy_null_para_zero(df)

    db_name2 = "databases/datawarehouse.db"

    create_database(db_name2)
    create_table(db_name2, table_name)
    insert_data(df, db_name2, table_name)
