# import modules.fs as fs
# importlib.reload(fs)
# fs.read_csv(path='./data/example.csv')

import pandas as pd


def main():
    pass


def read_csv(path='', sep=',', encoding='utf-8', **kwargs):
    return pd.read_csv(path, sep=sep, encoding=encoding, **kwargs)


def to_csv(df, path='', sep=',', index=True, encoding='utf-8', **kwargs):
    df.to_csv(path, sep=sep, index=index, encoding=encoding, **kwargs)


def read_tsv(path='', sep='\t', thousands=',', encoding='utf-8', **kwargs):
    return pd.read_csv(path, sep=sep, thousands=thousands, encoding=encoding, **kwargs)


def to_tsv(df, path='', sep='\t', index=True, encoding='utf-8', **kwargs):
    df.to_csv(path, sep=sep, index=index, encoding=encoding, **kwargs)


def read_excel(path='', thousands=',', **kwargs):
    return pd.read_excel(path, thousands=thousands, **kwargs)


def to_excel(df, path='', **kwargs):
    df.to_excel(path, **kwargs)


def read_parquet(path='', **kwargs):
    return pd.read_parquet(path, **kwargs)


def to_parquet(df, path='', engine='pyarrow', compression='snappy', **kwargs):
    df.to_parquet(path, engine=engine, compression=compression, **kwargs)


if __name__ == "__main__":
    main()
