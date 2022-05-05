# import modules.fs as fs
# importlib.reload(fs)
# fs.read_csv(path='./data/example.csv')

import json
import pandas as pd
import matplotlib.pyplot as plt


def main():
    pass


def read_txt(path):
    with open(path, 'r') as f:
        return f.read().strip()


def read_csv(path, sep=',', encoding='utf-8', **kwargs):
    return pd.read_csv(path, sep=sep, encoding=encoding, **kwargs)


def to_csv(df, path, sep=',', index=False, encoding='utf-8', **kwargs):
    df.to_csv(path, sep=sep, index=index, encoding=encoding, **kwargs)


def read_tsv(path, sep='\t', thousands=',', encoding='utf-8', **kwargs):
    return pd.read_csv(path, sep=sep, thousands=thousands, encoding=encoding, **kwargs)


def to_tsv(df, path, sep='\t', index=False, encoding='utf-8', **kwargs):
    df.to_csv(path, sep=sep, index=index, encoding=encoding, **kwargs)


def read_excel(path, thousands=',', **kwargs):
    return pd.read_excel(path, thousands=thousands, **kwargs)


def to_excel(df, path, **kwargs):
    df.to_excel(path, **kwargs)


def read_parquet(path, **kwargs):
    return pd.read_parquet(path, **kwargs)


def to_parquet(df, path, engine='pyarrow', compression='snappy', **kwargs):
    df.to_parquet(path, engine=engine, compression=compression, **kwargs)


def json_load(path, encoding='utf-8', **kwargs):
    return json.load(open(path, encoding=encoding, **kwargs))


def imshow(path, figsize=(20, 20), format='png'):
    plt.figure(figsize=figsize)
    img = plt.imread(path, format=format)
    plt.axis('off')
    plt.imshow(img)


if __name__ == "__main__":
    main()
