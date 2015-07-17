from data_manager import ServeData


class Viewer:
	def __init__(self):
		self.period_obj = ServeData()
		self.period_obj.load_data()
	
	def looper(self):
		print '\n================ THE PENULTIMATE TV TRACKER ================\n'
		while True:
			try:
				print '1. Add series to watchlist'
				print '2. View watchlist'
				print '3. View series already reached the threshold'
				print '4. Exit'
				choice = raw_input('\nEnter choice: ').strip()
				if choice == '1':
					series_name = raw_input('\nEnter series name : ').strip()
					there = self.period_obj.series_already_in_list(series_name)
					if there:
						print '\nERROR : Series already been added previously'
					else:
						self.period_obj.add_series_to_watchlist(series_name)
				
				elif choice == '2':
					watched_list = self.period_obj.return_list()
					if watched_list:
						print '\nAll series currently being watched : '
						for i, series_name in enumerate(watched_list):
							print ('%d. %s') % ((i+1), series_name)
					else:
						print '\nNo series listed here currently'
				
				elif choice == '3':
					destined_list = self.period_obj.return_list(False)
					if destined_list:
						print '\nSeries which have crossed the threshold : '
						for i, series_name in enumerate(destined_list):
							print ('%d. %s') %((i+1), series_name)	
					else:
						print '\nNo series listed here currently'
				
				elif choice == '4':
					break
		
				else:
					pass
		
				print '\n============================================================\n'
			except Exception,e:
				print 'Exception : %s\n' % (type(e).__name__, )
				break
		self.period_obj.save_data()
