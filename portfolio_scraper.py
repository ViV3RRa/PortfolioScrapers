from utils.utils import *


for platform_to_scrape in get_platforms_to_scrape():
	try:
		platform = get_platform(platform_to_scrape)
		if platform is not None:
			platform_name = platform.__class__.__name__
			platform.login()
			total_account_value = str(platform.get_account_value()).replace('.', ',')
			available_funds = str(platform.get_available_funds()).replace('.', ',')
			print('{} - Total Account Value:	{} {}'.format(platform_name, total_account_value, 'kr' if isinstance(platform, Nordnet) else '€'))
			print('{} -    Available Founds:	{} {}'.format(platform_name, available_funds, 'kr' if isinstance(platform, Nordnet) else '€'))
			platform.quit()
			data = '{};{};{}'.format(get_current_date_as_string(), total_account_value, available_funds)
			persist_data_in_file(platform_name, data)
			print(data)
			print('-----------------------------------------------')
	except Exception as e:
		print(e)
		platform.send_alert_email(platform_name, e)
		platform.quit()

