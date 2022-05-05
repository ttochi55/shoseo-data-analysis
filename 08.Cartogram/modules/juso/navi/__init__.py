import numpy as np
import pandas as pd

# Unix style pathname pattern expansion
from glob import glob

# A Fast, Extensible Progress Bar for Python and CLI
from tqdm import tqdm

# 국가기초구역번호 중심좌표 구하기
# https://www.juso.go.kr/addrlink/addrlinkJusoDBUse.do?menu=navi
# https://www.juso.go.kr/addrlink/addressBuildDevNew.do?menu=navi

# 주소관할읍면동코드(0) 문자: 시군구코드(5) + 읍면동코드(3) + 00
# 건물중심점_x좌표(23) 숫자: GRS80 UTM-K 좌표계
# 건물중심점_y좌표(24) 숫자: GRS80 UTM-K 좌표계


def main():
    tmp_raw = []

    for filepath in tqdm(glob('./data/juso.go.kr/navi/202010/match_build_*.txt')):
        try:
            tmp_df = pd.read_csv(filepath, sep='|', header=None, usecols=[0, 23, 24], dtype={
                                 0: object, 23: float, 24: float}, engine='python')
            tmp_df.rename(
                columns={0: '시군구코드', 23: '시군구_x', 24: '시군구_y'}, inplace=True)
            tmp_df['시군구코드'] = tmp_df['시군구코드'].str.slice(0, 5)
            tmp_raw.append(tmp_df)
        except Exception as e:
            print(filepath, e)

    df = pd.concat(tmp_raw)
    df.index = np.arange(0, len(df))

    result = df.groupby(['시군구코드'])['시군구_x', '시군구_y'].mean()
    result.to_csv('./data/juso.go.kr/navi-202010.csv', sep=',', float_format='%.6f',
                  encoding='utf-8', index=True)


if __name__ == "__main__":
    main()
