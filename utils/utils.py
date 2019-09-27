import json
import time
from datetime import datetime
from utils.config import Config
from platforms.brickshare import BrickShare
from platforms.nordnet import Nordnet
from platforms.mintos import Mintos
from platforms.peerberry import Peerberry
from platforms.grupeer import Grupeer
from platforms.fastinvest import Fastinvest
from platforms.crowdestor import Crowdestor


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
	elif platform_name == 'crowdestor':
		return Crowdestor()
	else:
		return None


def get_current_date_as_string():
	now = datetime.now() # current date and time
	return now.strftime("%Y-%m-%d")

def get_current_time_in_milliseconds():
	return int(round(time.time() * 1000))


def persist_data_in_file(platform_name, data):
	with open('{}{}.csv'.format(Config(None).get_path_to_persist_data(), platform_name.lower()), 'a') as fd:
		fd.write(data + '\n')


def persist_data_in_one_file(data):
	with open('{}account_values.csv'.format(Config(None).get_accumulated_path()), 'a') as fd:
		fd.write(data + '\n')
