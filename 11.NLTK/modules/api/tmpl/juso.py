# A simple, yet elegant HTTP library.
import requests

# Get API Key
with open('./config/jusoapikey.txt', 'r') as f:
    API_KEY = f.read().strip()


def main():
    pass


def get_requests(keyword=''):
    if keyword:
        url = 'https://www.juso.go.kr/addrlink/addrLinkApi.do'
        params = {
            'confmKey': API_KEY,
            'currentPage': 1,
            'countPerPage': 1,
            'keyword': keyword,
            'resultType': 'json',
        }
        return requests.get(url, params=params).json()
    return ''


def get_juso(keyword=''):
    if keyword:
        r = get_requests(keyword)
        return r['results']['juso'][0]
    return ''


def get_roadAddr(keyword=''):
    if keyword:
        r = get_juso(keyword)
        return r['roadAddr']
    return ''


def get_jibunAddr(keyword=''):
    if keyword:
        r = get_juso(keyword)
        return r['jibunAddr']
    return ''


if __name__ == "__main__":
    main()
