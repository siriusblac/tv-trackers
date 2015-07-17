import os
import pickle

import parameters

		
class ServeData:
	def __init__(self):
		self.series_to_track = list()
		self.series_already_destined = list()
	
	def load_data(self):
		if os.path.isfile(parameters.PATH_STT):
			self.series_to_track = pickle.load(open(parameters.PATH_STT, 'rb'))
		if os.path.isfile(parameters.PATH_SARD):
			self.series_already_destined = pickle.load(open(parameters.PATH_SARD, 'rb'))
	
	def save_data(self):
		pickle.dump(self.series_to_track, open(parameters.PATH_STT, 'wb'))
		pickle.dump(self.series_already_destined, open(parameters.PATH_SARD, 'wb'))
	
	def series_already_in_list(self, series_name):
		is_it_so = series_name in self.series_to_track
		if not is_it_so:
			is_it_so = series_name in self.series_already_destined
		return is_it_so

	def add_series_to_watchlist(self, series_name):
		self.series_to_track.append(series_name)

	def return_list(self, watch = True):
		if watch:
			return self.series_to_track
		else:
			return self.series_already_destined
			
	def receive_data_from_query(self, series_to_track, series_already_destined):
		self.series_to_track = series_to_track
		self.series_already_destined = series_already_destined
