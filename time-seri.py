import sys
import datetime
import time
import twitter
def get_time_series_data(api_func, mongo_db_name, mongo_db_coll,
 secs_per_interval=60, max_intervals=15, **mongo_conn_kw):
    interval = 0

    while True:

    # A timestamp of the form "2013-06-14 12:52:07"
    now = str(datetime.datetime.now()).split(".")[0]

    ids = save_to_mongo(api_func(), mongo_db_name, mongo_db_coll + "-" + now)

    print >> sys.stderr, "Write {0} trends".format(len(ids))
    print >> sys.stderr, "Zzz..."
    print >> sys.stderr.flush()

    time.sleep(secs_per_interval)  # seconds
    interval += 1

    if interval >= 15:
        break

    # Sample usage


get_time_series_data(twitter_world_trends, 'time-series', 'twitter_world_trends')
