import json
from platforms.mintos import Mintos
from platforms.nordnet import Nordnet
from platforms.peerberry import Peerberry
from platforms.grupeer import Grupeer
from platforms.fastinvest import Fastinvest


def get_platform(platform_name):
	if platform_name == 'Nordnet':
		return Nordnet()
	elif platform_name == 'Mintos':
		return Mintos()
	elif platform_name == 'Peerberry':
		return Peerberry()
	elif platform_name == 'Grupeer':
		return Grupeer()
	elif platform_name == 'Fastinvest':
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

