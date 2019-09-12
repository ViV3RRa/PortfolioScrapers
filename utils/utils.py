import json
from datetime import datetime
from platforms.brickshare import BrickShare
from platforms.nordnet import Nordnet
from platforms.mintos import Mintos
from platforms.peerberry import Peerberry
from platforms.grupeer import Grupeer
from platforms.fastinvest import Fastinvest


def get_platform(platform_name):
	platform_name = platform_name.lower()
	if platform_name == 'brickshare':
		return BrickShare()
	elif platform_name == 'nordnet':
		return Nordnet()
	elif platform_name == 'mintos':
		return Mintos()
	elif platform_name == 'peerberry':
		return Peerberry()
	elif platform_name == 'grupeer':
		return Grupeer()
	elif platform_name == 'fastinvest':
		return Fastinvest()
	else:
		return None


def __get_from_configure_file(configure_object):
	with open("configure.json") as f_check:
		platforms = json.load(f_check)[configure_object]
	return platforms


def get_platforms_to_scrape():
	return __get_from_configure_file('platforms_to_scrape')


def get_receiver_email():
	return __get_from_configure_file('alert_email_receiver')


def __get_path_to_persist_data():
	return __get_from_configure_file('path_to_persist_data')


def get_current_date_as_string():
	now = datetime.now() # current date and time
	return now.strftime("%Y-%m-%d")


def persist_data_in_file(platform_name, data):
	with open('{}{}.csv'.format(__get_path_to_persist_data(), platform_name.lower()), 'a') as fd:
		fd.write(data + '\n')

