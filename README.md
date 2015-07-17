# tv-trackers
Tracks TV shows ratings in IMDB.



In order to change preferences -- 
Edit in the parameters.py file

Current preferences set to --
Minimum votes in IMDB - 1,00,000
Minimum rating in IMDB - 8.0




For Setup:

Add a line like this to - /etc/anacrontab
7       20      tv-tracker      /usr/bin/python <path-to-dir>/period_query.py



Run main.py to add and check WatchLists status
