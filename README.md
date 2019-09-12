<img src="platform_icons/brickshare_logo.jpg" alt="alt text" title="BrickShare" height="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="platform_icons/nordnet_logo.png" alt="alt text" title="Nordnet" height="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="platform_icons/mintos_logo.png" alt="alt text" title="Mintos" height="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="platform_icons/PeerBerry_logo.jpg" alt="alt text" title="Peerberry" height="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="platform_icons/grupeer_logo.png" alt="alt text" title="Grupeer" height="50">&nbsp;&nbsp;&nbsp;&nbsp;<img src="platform_icons/fastinvest_logo.jpg" alt="alt text" title="FastInvest" height="50">

# PortfolioScrapers
This repository contains Python3 scripts for scraping your account information from different investment platforms.
Supports email notifications send from a supplied _Gmail_ to a receiver mail if the scraper failes to scrape a platform.

### Currently supportet platforms
* __BrickShare__ (Only supports scraping one BrickShare Project at the moment.)
* __Nordnet__
* __Mintos__ (__NB!__ Only works with Two-factor authentication __Deactivated__)
* __Peerberry__
* __Grupeer__
* __FastInvest__ (__NB!__ Only works with Two-factor authentication __Deactivated__)

### Prerequisites!
* Python 3
* pip3
* Install Selenium for Python3
* Install a Chrome/Chromium webdriver and supply the absolute path to the webdriver in ```utils/browser.py```

### Setup scraper
* Create the file ```credentials.json``` in the root of the project (alongside portfolio\_scraper.py)
```{
	"alert\_email\_sender": {
		"usr": "",
		"pwd": ""
	},
	"brickshare": {
		"usr": "",
		"pwd": ""
	},
	"nordnet": {
		"usr": "",
		"pwd": ""
	},
	"mintos": {
		"usr": "",
		"pwd": ""
	},
	"peerberry": {
		"usr": "",
		"pwd": ""
	},
	"grupeer": {
		"usr": "",
		"pwd": ""
	},
	"fastinvest": {
		"usr": "",
		"pwd": ""
	}
}```
(__NB!__ ```alert_email_sender``` must be a _Gmail_)
* Choose the platforms to be scraped and the receiver of any notification-mails in ```configure.json```

### RUN
While at the root of the project, run the following command:
```
python3 portfolio_scraper.py
```

