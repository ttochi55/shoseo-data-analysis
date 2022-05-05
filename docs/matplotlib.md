
```
import sys

if sys.platform.startswith('darwin'):
    mpl.rc('font', family='AppleGothic')
elif sys.platform.startswith('win32'):
    mpl.rc('font', family='Malgun Gothic')
```

```
import matplotlib.font_manager as fm

# 이용 가능한 폰트 중 '고딕'만 선별 -> 글씨가 굵어야 예뻐서
for font in fm.fontManager.ttflist:
    if 'Gothic' in font.name:
        print(font.name, font.fname)
```