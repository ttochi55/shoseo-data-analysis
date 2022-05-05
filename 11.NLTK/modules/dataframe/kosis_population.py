import numpy as np
import pandas as pd


def main():
    filepath = './data/kosis.kr/2019/행정구역_시군구_별__성별_인구수_20201202115401.csv'

    df = pd.read_csv(filepath,
                     sep=',',
                     encoding='euc-kr',
                     names=['시도', '시군구', '인구수', '남자수', '여자수'],
                     skiprows=[0, 1, 2]
                     )

    df = df[df['시군구'] != '소계']

    tmp = df['시도'].str.split(' ', n=1, expand=True)
    df['시도코드'] = tmp[0]
    df['시도명'] = tmp[1]

    tmp = df['시군구'].str.split(' ', n=1, expand=True)
    df['시군구코드'] = tmp[0]
    df['시군구명'] = tmp[1]

    df = df[['시도명', '시도코드', '시군구명', '시군구코드', '인구수', '남자수', '여자수']]

    df.to_csv('./data/kosis.kr/population-202010.csv',
              sep=',', encoding='utf-8', index=False)
    df.head()


if __name__ == "__main__":
    main()
