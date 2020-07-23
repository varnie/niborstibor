import argparse
import atexit
import time

from apscheduler.schedulers.background import BackgroundScheduler

from fetchers.nibor import NiborFetcher
from fetchers.stibor import StiborFetcher

parser = argparse.ArgumentParser()

parser.add_argument('--name', required=True, choices=['nibor', 'stibor'])
parser.add_argument('--action', required=True, choices=['initial_import', 'daemon'])


def go(fetcher):
    print("Attempting to retrieve data...")
    fetcher.try_fetch()


if __name__ == "__main__":
    args = parser.parse_args()
    name = args.name
    action = args.action

    fetcher = NiborFetcher() if name == 'nibor' else StiborFetcher()
    print(fetcher, action, 'started')

    if action == 'initial_import':
        fetcher.initial_import()
    else:
        scheduler = BackgroundScheduler(daemon=True)
        # specify suitable interval if needed, like "minutes=30" or "hours=1" instead of "minutes=60"
        scheduler.add_job(go,
                          trigger='interval',
                          args=[fetcher],
                          minutes=60)
        scheduler.start()
        atexit.register(lambda: scheduler.shutdown(wait=False))
        while True:
            time.sleep(10)

