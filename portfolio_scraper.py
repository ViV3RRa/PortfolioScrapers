from utils.utils import *
from utils.config import Config
import datetime


class PortfolioScraper:
	def __init__(self):
		self.config = Config(None)


	def scrape_account(self, platform):
		platform_name = platform.get_name()
		platform.login()
		total_account_value = get_value_in_cents(platform.get_account_value())
		available_funds = get_value_in_cents(platform.get_available_funds())
		platform.quit()
		data = '{},{},{},{},{}'.format(get_current_time_in_milliseconds(), total_account_value, available_funds, platform.get_account(), platform.get_currency())
		persist_data_in_file(platform_name, data)
		persist_account_value(data)
		print(platform_name + ': ' + data)
		return


	def scrape_projects(self, platform):
		platform_name = platform.get_name()
		platform.login()

		total_account_value = 0
		available_funds = get_value_in_cents(platform.get_available_funds())

		for project in platform.get_projects():
			project_value = platform.get_project_value(project)
			total_account_value += project_value
			project_value_cents = get_value_in_cents(project_value)
			project_data = '{},{},{},{}'.format(get_current_time_in_milliseconds(), project_value_cents, project, platform.get_account())
			persist_project_value(project_data)


		total_account_value_cents = get_value_in_cents(total_account_value)
		account_data = '{},{},{},{},{}'.format(get_current_time_in_milliseconds(), total_account_value_cents, available_funds, platform.get_account(), platform.get_currency())
		persist_data_in_file(platform_name, account_data)
		persist_account_value(account_data)
		print(platform_name + ': ' + account_data)
		return


	def scrape(self):
		config = Config(None)
		print('{date:%Y-%m-%d-%H:%M:%S}'.format(date=datetime.datetime.now()))
		for platform_to_scrape in self.config.get_platforms_to_scrape():
			try:
				platform = get_platform(platform_to_scrape)
				if platform is not None:
					if platform.has_projects():
						self.scrape_projects(platform)
					else:
						self.scrape_account(platform)
			except Exception as e:
				print(e)
				platform.send_alert_email(platform.get_name(), e)
				platform.quit()


		print('-----------------------------------------------')



portfolio_scraper = PortfolioScraper()
portfolio_scraper.scrape()
