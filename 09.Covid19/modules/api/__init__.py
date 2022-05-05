def main(theme, endpoint, **kwargs):
    if (theme == 'juso'):
        from .tmpl import juso
        return juso.main(endpoint, **kwargs)
    elif (theme == 'kakaomap'):
        from .tmpl import kakaomap
        return kakaomap.main(endpoint, **kwargs)
    elif (theme == 'openapi'):
        from .tmpl import openapi
        return openapi.main(endpoint, **kwargs)


if __name__ == "__main__":
    main()
