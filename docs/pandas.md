# Pandas

## Index

**reindex**
```
df.index = np.arange(0, len(df))
```

## Glob
```
from glob import glob
raw = []
for f in glob('./data/지역_*.xls'):
    row = pd.read_excel(f, encoding='utf8')
    raw.append(row)
```

## duplicates
```
sidocode = population.drop_duplicates(subset=['시도명', '시도코드'], keep='last')[['시도명', '시도코드']]
sidocode.index = np.arange(0, len(sidocode))
sidocode['시도명'].replace('특별시|광역시|특별자치시|특별자치도', '', regex=True, inplace=True)
sidocode['시도명'].replace('(경기|강원)도', r'\1', regex=True, inplace=True)
sidocode['시도명'].replace('(충|전|경)(?:청|라|상)(북|남)도', r'\1\2', regex=True, inplace=True)
```

## Format

**String**
```
df[column] = pd.to_string(df[column])
```

**Numeric**
```
df[column] = pd.to_numeric(df[column])
```
**Datetime**
```
df['createDt'] = df['createDt'].replace('\.\d+$', '', regex=True)
df['createDt'] = pd.to_datetime(df['createDt'], format='%Y-%m-%d %H:%M:%S')
```

**문자열을 숫자형으로 변환 시 ValueError 를 무시하기**
```
df = df.apply(pd.to_numeric, errors = 'coerce')
```

## Date
```
monthly = df.groupby(pd.Grouper(key='날짜', freq='1M')).count()
monthly.index = seoul_monthly.index.strftime('%Y-%m')
```

```
covid19['날짜'] = '2020.' + covid19['확진일'].replace('\.$', '', regex=True)
covid19['날짜'] = pd.to_datetime(covid19['날짜'], format='%Y.%m.%d')
covid19['년'] = covid19['날짜'].dt.year
covid19['월'] = covid19['날짜'].dt.month
covid19['일'] = covid19['날짜'].dt.day
```

## Image

**Write**
```
plt.savefig('./assets/img/image.png', format='png', dpi=300)
```

**Read**
```
plt.figure(figsize=(20,20))
img = plt.imread('./assets/img/image.png', format='png')
plt.axis('off')
plt.imshow(img)
```

## Replace
```
df = df.replace(',','', regex=True, inplace=True)
df.replace('-', np.nan, regex=True, inplace=True)
df.head()
```

### sort_values
```
df.sort_values(by='인구수', ascending=False).head()
```

