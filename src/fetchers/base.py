import datetime
import time
from abc import ABC

import utils


class BaseFetcher(ABC):

    market: str
    url: str
    last_file: str
    file_name: str
    csv_cols: dict

    def initial_import(self):

        traced_date = utils.load_last_date(self.last_file)

        if traced_date is None:
            start_date = datetime.datetime.now() - datetime.timedelta(days=90)
        else:
            start_date = traced_date + datetime.timedelta(days=1)

        status = True
        i = 0

        # retrieve max. 90 records, if possible
        while status and (i < 90):
            print("date processing", start_date.strftime("%d-%m-%Y"), "...")

            # skip Saturday and Sunday
            if not utils.is_weekend(start_date):
                date_str = start_date.strftime("%d-%m-%Y")
                import_details = utils.retrieve_reports(url=self.url,
                                                        market=self.market,
                                                        dst_file=self.file_name,
                                                        date_val=date_str,
                                                        cols=self.csv_cols)
                status = import_details.status
                utils.save_last_date(self.last_file, date_str)

                # random sleep intervals (it is good to have some to avoid banning)
                time.sleep(utils.generate_sleep_val())

                i += 1

            start_date = start_date + datetime.timedelta(days=1)

    def try_fetch(self):
        cur_date = datetime.datetime.now()
        traced_date = utils.load_last_date(self.last_file)

        # skip Saturday and Sunday
        if not utils.is_weekend(cur_date) and \
                (traced_date is None or cur_date.date() > traced_date.date()):
            date_str = cur_date.strftime("%d-%m-%Y")
            _ = utils.retrieve_reports(url=self.url,
                                       market=self.market,
                                       dst_file=self.file_name,
                                       date_val=date_str,
                                       cols=self.csv_cols)
            utils.save_last_date(self.last_file, date_str)
