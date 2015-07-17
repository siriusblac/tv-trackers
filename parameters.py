import os

LOCAL_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(LOCAL_PATH, 'data')
PATH_STT = os.path.join(DATA_PATH, 'series_to_track.pkl')
PATH_SARD = os.path.join(DATA_PATH, 'series_already_destined.pkl')

# ------------------------------ Don't edit above ------------------------------------

MAX_VOTES_REQD = 100000
MAX_RATING_REQD = 8.0
