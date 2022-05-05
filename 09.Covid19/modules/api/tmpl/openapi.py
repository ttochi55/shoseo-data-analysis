from ...bin import fs as fs

import os
import math
import numpy as np
import pandas as pd

from datetime import datetime

# A Fast, Extensible Progress Bar for Python and CLI
from tqdm import tqdm

# A simple, yet elegant HTTP library.
import requests

# Python HTTP library with thread-safe connection pooling, file post support, user friendly, and more.
from urllib import parse

# Beautiful Soup is a Python library for pulling data out of HTML and XML files.
from bs4 import BeautifulSoup


API_KEY = fs.read_txt('./config/openapirestapikey.txt')


def main(endpoint, **kwargs):

    basename = os.path.basename(endpoint)
    endpoint = endpoint + '?ServiceKey=' + API_KEY

    params = {
        'pageNo': 1,
        'numOfRows': 10,
        'startCreateDt': '20200410',
        'endCreateDt': '20200410',
    }

    for k, v in kwargs.items():
        params.update({k: v})

    response = requests.get(endpoint, params=params)
    soup = BeautifulSoup(response.text, 'xml')
    dataset = []

    # paging
    num_of_rows = int(soup.select_one('numOfRows').get_text(strip=True))
    total_count = int(soup.select_one('totalCount').get_text(strip=True))
    total_page = math.ceil(total_count / num_of_rows)

    # dating
    startDate = datetime.strptime(params['startCreateDt'], '%Y%m%d')
    endDate = datetime.strptime(params['endCreateDt'], '%Y%m%d')
    periods = pd.date_range(startDate, endDate, freq='M').notna().sum()
    drange = pd.date_range(startDate, periods=periods, freq='M')

    for dtime in drange:

        try:
            monthly = []
            periodCreateDt = dtime.strftime('%Y%m')
            startCreateDt = periodCreateDt + '01'
            endCreateDt = dtime.strftime('%Y%m%d')

            params.update({'startCreateDt': startCreateDt})
            params.update({'endCreateDt': endCreateDt})

            for page_no in tqdm(np.arange(1, total_page+1)):

                try:
                    params.update({'pageNo': page_no})

                    r = requests.get(endpoint, params=params)

                    # parsing
                    soup = BeautifulSoup(r.text, 'xml')
                    item = soup.select('item')

                    for row in item:
                        daily = {}
                        for col in row:
                            daily.update({col.name: col.get_text(strip=True)})
                        monthly.append(daily)
                        dataset.append(daily)

                except Exception as e:
                    print(page_no, e)

            fs.to_csv(pd.DataFrame(monthly),
                      './data/{}_{}.csv'.format(basename, dtime))

        except Exception as e:
            print(dtime, e)

    return pd.DataFrame(dataset)


if __name__ == "__main__":
    main()
