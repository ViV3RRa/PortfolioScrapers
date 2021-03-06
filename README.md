<img src="platform_icons/brickshare_logo.jpg" alt="alt text" title="BrickShare" height="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="platform_icons/kameo_logo.png" alt="alt text" title="Kameo" height="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="platform_icons/nordnet_logo.png" alt="alt text" title="Nordnet" height="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="platform_icons/saxoinvestor_logo.png" alt="alt text" title="SaxoInvestor" height="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="platform_icons/mintos_logo.png" alt="alt text" title="Mintos" height="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="platform_icons/PeerBerry_logo.jpg" alt="alt text" title="Peerberry" height="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="platform_icons/grupeer_logo.png" alt="alt text" title="Grupeer" height="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="platform_icons/fastinvest_logo.jpg" alt="alt text" title="FastInvest" height="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="platform_icons/crowdestor_logo.png" alt="alt text" title="Crowdestor" height="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="platform_icons/kuetzal_logo.png" alt="alt text" title="Kuetzal" height="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="platform_icons/iuvo_logo.png" alt="alt text" title="Iuvo" height="50">

# PortfolioScrapers
This repository contains Python3 scripts for scraping your account information from different investment platforms.
If a platform consists of individual projects the current value of the project will be found along with the total platform value(as a summation of project values).
Supports email notifications send from a supplied _Gmail_ to a receiver mail if the scraper failes to scrape a platform.

### Currently supportet platforms
* __BrickShare__
* __Kameo__
* __Nordnet__
* __SaxoInvestor__
* ~~__Mintos__ (__NB!__ Only works with Two-factor authentication __Deactivated__)~~ Mintos is sadly not working at the moment due to the introduction of CAPTCHA on their website.
* __Peerberry__
* ~~__Grupeer__~~ Grupeer is sadly not working at the moment due to the introduction of CAPTCHA on their website.
* __FastInvest__ (__NB!__ Only works with Two-factor authentication __Deactivated__)
* __Crowdestor__
* ~~__Kuetzal__~~ (__NB!__ Out of business)
* __Iuvo__

### Prerequisites!
* Python 3
* pip3
* Install Selenium for Python3
* Install a Chrome/Chromium webdriver and supply the absolute path to the webdriver in ```utils/browser.py```
* Install pyvirtualdisplay by running: ```pip3 install pyvirtualdisplay```
* Install xvfb by running: ```apt-get install xvfb```

### Setup scraper
1. Create the file ```config.json``` in the root of the project (alongside portfolio\_scraper.py):
```
{
	"platforms_to_scrape": [
		"brickshare",
		"kameo",
		"nordnet",
		"saxoinvestor",
		"mintos",
		"peerberry",
		"grupeer",
		"fastinvest",
		"crowdestor",
		"kuetzal",
		"iuvo"
	],
	"alert_email": {
		"sender": {
			"usr": "some@gmail.com",
			"pwd": ""
		},
		"receiver": ""
	},
	"path_to_persist_data": "absolute/path/to/persist/data/",
	"accumulated_path": "absolute/path/to/accumulated/data/",
	"brickshare": {
		"usr": "",
		"pwd": "",
		"account": "some_account_id",
		"currency": "dkk",
		"projects": [
			"project-id"
		]
	},
	"kameo": {
		"usr": "",
		"pwd": "",
		"account": "some_account_id",
		"currency": "dkk"
	},
	"nordnet": {
		"usr": "",
		"pwd": "",
		"account": "some_account_id",
		"currency": "dkk"
	},
	"saxoinvestor": {
		"usr": "",
		"pwd": "",
		"account": "some_account_id",
		"currency": "dkk"
	},
	"mintos": {
		"usr": "",
		"pwd": "",
		"account": "mintos9623564",
		"currency": "eur"
	},
	"peerberry": {
		"usr": "",
		"pwd": "",
		"account": "some_account_id",
		"currency": "eur"
	},
	"grupeer": {
		"usr": "",
		"pwd": "",
		"account": "some_account_id",
		"currency": "eur"
	},
	"fastinvest": {
		"usr": "",
		"pwd": "",
		"account": "some_account_id",
		"currency": "eur"
	},
	"crowdestor": {
		"usr": "",
		"pwd": "",
		"account": "some_account_id",
		"currency": "eur"
	},
	"kuetzal": {
		"usr": "",
		"pwd": "",
		"account": "some_account_id",
		"currency": "eur"
	},
	"iuvo": {
		"usr": "",
		"pwd": "",
		"account": "some_account_id",
		"currency": "eur"
	}
}

```
(__NB!__ ```alert_email.sender``` must be a _Gmail_)


### RUN
While at the root of the project, run the following command:
```
python3 portfolio_scraper.py
```

