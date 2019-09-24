from utils.utils import *
from utils.config import Config
import datetime


class PortfolioScraper:
	def __init__(self):
		self.config = Config(None)

	def scrape(self):
		config = Config(None)
		print('{date:%Y-%m-%d-%H:%M:%S}'.format(date=datetime.datetime.now()))
		for platform_to_scrape in self.config.get_platforms_to_scrape():
			try:
				platform = get_platform(platform_to_scrape)
				if platform is not None:
					platform_name = platform.__class__.__name__
					platform.login()
					total_account_value = str(platform.get_account_value()).replace('.', '')
					available_funds = str(platform.get_available_funds()).replace('.', '')
					platform.quit()
					data = '{},{},{},{},{}'.format(get_current_time_in_milliseconds(), total_account_value, available_funds, platform.get_account(), platform.get_currency())
					persist_data_in_file(platform_name, data)
					print(platform_name + ': ' + data)
			except Exception as e:
				print(e)
				platform.send_alert_email(platform_name, e)
				platform.quit()


		print('-----------------------------------------------')


portfolio_scraper = PortfolioScraper()
portfolio_scraper.scrape()
