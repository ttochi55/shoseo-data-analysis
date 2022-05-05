# Relative imports cannot be used with "import .a" form; use "from . import a" instead
from .bin import fs


def main(theme, df, **kwargs):
    if (theme == 'covid19_seoul'):
        from .tmpl import covid19_seoul
        return covid19_seoul.main(df, **kwargs)
    elif (theme == 'covid19_korea'):
        from .tmpl import covid19_korea
        return covid19_korea.main(df, **kwargs)


if __name__ == "__main__":
    main()
