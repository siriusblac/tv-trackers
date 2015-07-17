import json
from multiprocessing import Pool
import requests

import parameters
from data_manager import ServeData


def query_data(prepare_for_search):
	_r_get = requests.get("http://www.omdbapi.com/?t=%s&type=series&r=json" % (prepare_for_search), timeout = 10)
	return _r_get
	
	
class Period:
	def __init__(self):
		self.data_obj = ServeData()
		self.data_obj.load_data()
		self.series_to_track = self.data_obj.return_list()
		self.series_reached = self.data_obj.return_list(False)
		
	def do_query(self):
		_p_id = Pool(processes=10)
		results = list()
		for series_name in self.series_to_track:
			prepare_name = '+'.join(series_name.split())
			results.append(_p_id.apply_async(query_data, args=(prepare_name, )))
		for result in results:
			returned_result = result.get()
			json_formatted_result = json.loads(returned_result.text)
			no_of_votes = int(json_formatted_result['imdbVotes'].replace(',', ''))
			rating = float(json_formatted_result['imdbRating'])
			if no_of_votes >= parameters.MAX_VOTES_REQD and rating >= parameters.MAX_RATING_REQD:
				self.series_reached.append(json_formatted_result['Title'])
				self.series_to_track.remove(json_formatted_result['Title'])
	
	def push_back(self):
		# Do a clean list check first
		for series_name in self.series_reached:
			if series_name in self.series_to_track:
				self.series_to_track.remove(series_name)
		# Push data back to Data guy
		self.data_obj.receive_data_from_query(self.series_to_track, self.series_reached)
		self.data_obj.save_data()
