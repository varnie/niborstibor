from constants import NIBOR_LAST, NIBOR_CSV
from fetchers.base import BaseFetcher


class NiborFetcher(BaseFetcher):

    market = 'NIBOR'
    url = 'https://rates.referanserenter.no/submit.php'
    last_file = NIBOR_LAST
    file_name = NIBOR_CSV
    csv_cols = ['Calculation Date', 'Tenor', 'Fixing Rate', 'DNBB', 'DSKE', 'HAND', 'NORD', 'SEBB', 'SWED']

    def __str__(self):
        return 'Nibor'
