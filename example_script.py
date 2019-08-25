from utils.utils import *


for platform_to_scrape in get_platforms_to_scrape():
	try:
		platform = get_platform(platform_to_scrape)
		if platform is not None:
			platform_name = platform.__class__.__name__
			platform.login()
			print('{}:	{} {}'.format(platform_name, str(platform.get_account_value()), 'kr' if isinstance(platform, Nordnet) else '€'))
			platform.quit()
	except Exception as e:
		print(e)
		platform.send_alert_email(platform_name, e)
		platform.quit()

