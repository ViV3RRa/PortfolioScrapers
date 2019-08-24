import json

class Credentials:

	def __init__(self, platform):
		credentials = self.get_credentials(platform)
		self.username = credentials['usr']
		self.password = credentials['pwd']


	def get_credentials(self, platform):
		# read json file data from previous run
		with open("credentials.json") as f_check:
			credentials = json.load(f_check)[platform]
		return credentials
