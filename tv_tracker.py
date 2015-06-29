import os
import pickle
import requests
import xml.etree.ElementTree as ET

import parameters


class Period:
	def __init__(self):
		self.series_to_track = list()
		self.series_to_not_track = list()
		
	def load_data(self):
		if os.path.isfile(parameters.PATH_STT):
			self.series_to_track = pickle.load(open(parameters.PATH_STT, 'rb'))
		if os.path.isfile(parameters.PATH_STNT):
			self.series_to_not_track = pickle.load(open(parameters.PATH_STNT, 'rb'))
	
	def save_data(self):
		pickle.dump(self.series_to_track, open(parameters.PATH_STT, 'wb'))
		pickle.dump(self.series_to_not_track, open(parameters.PATH_STNT, 'wb'))
		
	def check_out(self):
		for series_name in self.series_to_track:
			prepare_name = '+'.join(series_name.split())
			_r_get = requests.get("http://www.omdbapi.com/?t=%s&type=series&r=xml" % (_prepare_for_search))
