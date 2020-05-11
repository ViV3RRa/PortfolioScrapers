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
from platforms.kuetzal import Kuetzal
from platforms.iuvo import Iuvo
from platforms.saxoinvestor import SaxoInvestor
from platforms.kameo import Kameo


def get_platform(platform_name):
	platform_name = platform_name.lower()
	if platform_name == 'brickshare':
		return BrickShare()
	elif platform_name == 'kameo':
		return Kameo()
	elif platform_name == 'nordnet':
		return Nordnet()
	elif platform_name == 'saxoinvestor':
		return SaxoInvestor()
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
	elif platform_name == 'kuetzal':
		return Kuetzal()
	elif platform_name == 'iuvo':
		return Iuvo()
	else:
		return None


def get_value_in_cents(value):
	return str(int(float(value) * 100))


def get_current_date_as_string():
	now = datetime.now() # current date and time
	return now.strftime("%Y-%m-%d")

def get_current_time_in_milliseconds():
	return int(round(time.time() * 1000))


def persist_data_in_file(platform_name, data):
	with open('{}{}.csv'.format(Config(None).get_path_to_persist_data(), platform_name.lower()), 'a') as fd:
		fd.write(data + '\n')


def persist_account_value(data):
	with open('{}account_values.csv'.format(Config(None).get_accumulated_path()), 'a') as fd:
		fd.write(data + '\n')


def persist_project_value(data):
	with open('{}project_values.csv'.format(Config(None).get_accumulated_path()), 'a') as fd:
		fd.write(data + '\n')
