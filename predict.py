from sklearn.linear_model import LinearRegression
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

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

    return df

def train_model(x: pd.DataFrame, y: pd.Series) -> LinearRegression:
    """
    Treina o modelo de regressão linear.

    Args:
        x (pd.DataFrame): DataFrame do pandas com os dados de entrada.
        y (pd.Series): Série do pandas com os dados de saída.

    Returns:
        LinearRegression: Modelo treinado.
    """
    model = LinearRegression()
    model.fit(x, y)
    print(f"Coeficientes: {model.coef_}")
    return model

def preve_producao_trigo(df: pd.DataFrame) -> None:
    """
    Lê os dados do arquivo CSV, treina um modelo de regressão linear com a produção de trigo
    e faz previsões até 2030.

    Args:
        file_path (str): Caminho para o arquivo CSV com os dados.
    """
    wheat_df = df[(df["item"] == "Wheat") & (df["domain"] == "Production")]

    wheat_df = wheat_df.groupby("year").agg({"value": "sum"}).reset_index()

    x = wheat_df[["year"]]
    y = wheat_df["value"]

    model = train_model(x, y)

    last_year = wheat_df["year"].max()
    future_years = pd.DataFrame({"year": list(range(last_year + 1, 2031))})
    predictions = model.predict(future_years)

    future_years["Predicted_Production"] = predictions

    print("Previsões de produção de trigo (toneladas):")
    print(future_years)

    plt.figure(figsize=(10, 6))
    plt.plot(wheat_df["year"], wheat_df["value"], label="Produção Histórica")
    plt.plot(future_years["year"], future_years["Predicted_Production"], label="Previsão", linestyle="--")
    plt.xlabel("Ano")
    plt.ylabel("Produção de Trigo (toneladas)")
    plt.title("Previsão da Produção Total de Trigo na África")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    db_name = "databases/datawarehouse.db"
    table_name = "trigo"
    df = extract_data(db_name, table_name)
    preve_producao_trigo(df)
