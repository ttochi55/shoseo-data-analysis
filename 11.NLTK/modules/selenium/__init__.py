
def main(theme, **kwargs):
    if (theme == 'naver'):
        from .tmpl import naver
        return naver.main(**kwargs)
    elif (theme == 'lotteria'):
        from .tmpl import lotteria
        return lotteria.main(**kwargs)


if __name__ == "__main__":
    main()
