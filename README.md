<img src="platform_icons/brickshare_logo.jpg" alt="alt text" title="BrickShare" width="75" height="75">
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
* Install Selenium for Python3
* Install a Chrome/Chromium webdriver and supply the absolute path to the webdriver in ```utils/browser.py```

### Setup scraper
* Fill in ```credentials.json``` (__NB!__ ```alert_email_sender``` must be a _Gmail_)
* Choose the platforms to be scraped and the receiver of any notification-mails in ```configure.json```

### RUN
While at the root of the project, run the following command:
```
python3 portfolio_scraper.py
```

