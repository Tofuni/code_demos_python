import logging
import datetime as dt

# params: (filename) a string, (message) a string, (type) string value of "info", "warning", "error", or "critical"
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