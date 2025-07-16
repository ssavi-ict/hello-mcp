import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def read_csv_summary(filename: str) -> str:
    file_path = DATA_DIR / filename
    df = pd.read_csv(file_path)
    return f"CSV file '{filename}' has been {len(df)} rows and {len(df.columns)} columns."

def get_csv_headers(filename: str) -> str:
    file_path = DATA_DIR / filename
    df = pd.read_csv(file_path)
    column_names = str(list(df.columns))
    return f"CSV file '{filename}' headers are: {column_names} "

def read_parquet_summary(filename: str) -> str:
    file_path = DATA_DIR / filename
    df = pd.read_parquet(file_path)
    return f"Parquet file '{filename}' has been {len(df)} rows and {len(df.columns)} columns."

def get_columnwise_content(filename: str) -> str:
    file_path = DATA_DIR / filename
    df = pd.read_csv(file_path)
    contents = ""
    for column in df.columns:
        contents += f"Column {column} => "
        contents += ', '.join(df[column].astype(str))
        contents += "\n"
    return f"Below are the columnwise contents:\n{contents}\n"


def get_rowwise_content(filename: str) -> str:
    file_path = DATA_DIR / filename
    df = pd.read_csv(file_path)
    contents = [f"Row {i} : {', '.join(map(str, row))}" for i, row in enumerate(df.values)]
    contents = "\n".join(contents)
    return f"Below are the rowwise contents:\n{contents}\n"


if __name__ == "__main__":
    print(read_csv_summary("sample.csv"))
    print(read_parquet_summary("sample.parquet"))
    print(get_csv_headers("sample.csv"))
    print(get_columnwise_content('sample.csv'))
    print(get_rowwise_content('sample.csv'))