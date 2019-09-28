import json

class Config:

	def __init__(self, platform):
		self.config = self.__get_configurations()
		self.platform = platform
		if platform is not None:
			self.username = self.config[platform]['usr']
			self.password = self.config[platform]['pwd']
			self.account = self.config[platform]['account']
			self.currency = self.config[platform]['currency']
			self.projects = self.config[platform].get('projects', [])


	def __get_configurations(self):
		# read json file data from previous run
		with open("config.json") as f_check:
			configurations = json.load(f_check)
		return configurations


	def get_alert_email_sender(self):
		return self.config['alert_email']['sender']['usr']


	def get_alert_email_sender_pwd(self):
		return self.config['alert_email']['sender']['pwd']


	def get_alert_email_receiver(self):
		return self.config['alert_email']['receiver']


	def get_platforms_to_scrape(self):
		return self.config['platforms_to_scrape']


	def get_path_to_persist_data(self):
		return self.config['path_to_persist_data']


	def get_accumulated_path(self):
		return self.config['accumulated_path']


	def has_projects(self):
		return 'projects' in self.config[self.platform]


	def get_projects(self):
		return self.config[self.platform]['projects']
