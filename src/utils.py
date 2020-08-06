import csv
import json
import os
import random
from collections import namedtuple
from datetime import datetime
import headers
import requests

from logger import app_logger

DownloadDetails = namedtuple('DownloadDetails', ['skipped', 'status'])


def is_weekend(cur_date: datetime) -> bool:
    return cur_date.weekday() in [5, 6]


def load_last_date(fname):
    try:
        with open(fname) as f:
            val = f.readline().strip()
            return datetime.strptime(val, "%d-%m-%Y")
    except Exception as e:
        app_logger.info(e, exc_info=True)
        return None


def save_last_date(fname, val: str):
    try:
        with open(fname, "w") as f:
            f.write("%s\n" % val)
    except Exception as e:
        app_logger.error(e, exc_info=True)


def save_to_file(dst_csv_file_name, csv_cols, data: dict):
    file_exists = os.path.isfile(dst_csv_file_name)

    try:
        with open(dst_csv_file_name, 'a') as f:
            dict_writer = csv.DictWriter(f, fieldnames=csv_cols)

            if not file_exists:
                dict_writer.writeheader()

            for val in data:
                dict_writer.writerow(val)

            return True
    except IOError as e:
        app_logger.error(e, exc_info=True)
        return False


def generate_sleep_val(start=3, end=10):
    return random.randint(start, end)


def retrieve_reports(url, market, dst_file, date_val, cols) -> DownloadDetails:
    request_data = dict(market=market,
                        date=date_val)

    response = requests.post(url=url,
                             headers=headers.get_random_headers(),
                             data=request_data)

    if response.status_code == requests.codes.ok:
        text = response.text
        try:
            json_val = json.loads(text)
            results = json_val['results']
        except (ValueError, KeyError) as e:
            app_logger.error(e, exc_info=True)
        else:
            app_logger.info("Downloaded entries for date %s OK" % date_val)
            # save if there's some non-empty data
            if results:
                if save_to_file(dst_csv_file_name=dst_file, csv_cols=cols, data=results):
                    app_logger.info("Saved entries for date %s OK" % date_val)
                    return DownloadDetails(skipped=False, status=True)
            else:
                app_logger.warning("Skipped empty entries for date %s" % date_val)
                return DownloadDetails(skipped=True, status=True)
    else:
        app_logger.error("Data for %s is not available, request returned %d status" % (date_val, response.status_code))

    return DownloadDetails(skipped=False, status=False)
