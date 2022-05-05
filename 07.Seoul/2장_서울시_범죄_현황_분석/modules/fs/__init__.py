# import modules.fs as fs
# importlib.reload(fs)
# fs.read_csv(path='./data/example.csv')

import pandas as pd


def main():
    pass


def read_csv(path='', sep=',', header='infer', index_col=None, encoding='utf-8'):
    return pd.read_csv(path, sep=sep, header=header, index_col=index_col, encoding=encoding)


def to_csv(df, path='', sep=',', index=True, encoding='utf-8'):
    df.to_csv(path, sep=sep, index=index, encoding=encoding)


def read_tsv(path='', sep='\t', thousands=',', encoding='utf-8'):
    return pd.read_csv(path, sep=sep, thousands=thousands, encoding=encoding)


def to_tsv(df, path='', sep='\t', index=True, encoding='utf-8'):
    df.to_csv(path, sep=sep, index=index, encoding=encoding)


def read_excel(path='', thousands=','):
    return pd.read_excel(path, thousands=thousands)


def read_parquet(path=''):
    return pd.read_parquet(path)


def to_parquet(df, path='', engine='pyarrow', compression='snappy'):
    df.to_parquet(path, engine=engine, compression=compression)


if __name__ == "__main__":
    main()
