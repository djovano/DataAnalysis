import pandas as pd
import sqlite3

def read_sqlite(db_name: str, table_name: str) -> pd.DataFrame:
    """
    Lê os dados de uma tabela em um banco de dados SQLite e retorna um DataFrame do pandas.

    Args:
        db_name (str): Nome do banco de dados.
        table_name (str): Nome da tabela.

    Returns:
        pd.DataFrame: DataFrame do pandas com os dados lidos.
    """
    conn = sqlite3.connect(db_name)

    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

    conn.close()

    return df

def analyze_data(df: pd.DataFrame) -> None:
    """
    Análise inicial dos dados para entender a estrutura e o conteúdo.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados.
    """
    yoy_columns = [col for col in df.columns if "yoy" in col.lower()]
    null_yoy = df[yoy_columns].isnull().sum()
    null_yoy = null_yoy[null_yoy > 0]
    if not null_yoy.empty:
        print("\nColunas 'yoy' com valores nulos:")
        print(null_yoy)        
    else:
        print("\nNenhuma coluna 'yoy' com valores nulos.")

def yoy_null_para_zero(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preenche com zero os valores nulos nas colunas que contêm 'yoy' no nome.

    Args:
        df (pd.DataFrame): DataFrame original.

    Returns:
        pd.DataFrame: DataFrame com os valores nulos das colunas 'yoy' preenchidos com zero.
    """
    yoy_columns = [col for col in df.columns if "yoy" in col.lower()]
    df[yoy_columns] = df[yoy_columns].fillna(0)
    return df        