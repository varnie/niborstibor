from constants import STIBOR_LAST, STIBOR_CSV
from fetchers.base import BaseFetcher


class StiborFetcher(BaseFetcher):

    market = 'STIBOR'
    url = 'https://rates.swfbf.se/submit.php'
    last_file = STIBOR_LAST
    file_name = STIBOR_CSV
    csv_cols = ['Calculation Date', 'Tenor', 'Fixing Rate', 'DSKE', 'HAND', 'LFKR', 'NORD', 'SBAB', 'SEBB', 'SWED']

    def __str__(self):
        return 'Stibor'
