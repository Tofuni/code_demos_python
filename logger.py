import logging
import datetime as dt

def logfile(filename, message, type):
	filename += '_' + dt.datetime.now().strftime('%d-%m-%Y')
	logging.basicConfig(filename=filename+'.log', level=logging.DEBUG)
	message = dt.datetime.now().strftime('%d-%m-%Y_%I:%M:%S:%f') + ' ' + message
	options = {
		'info': logging.info,
		'warning': logging.warning,
		'error': logging.error,
		'critical': logging.critical
	}
	options[type](message)
	return

logfile('hello','worlds','info')