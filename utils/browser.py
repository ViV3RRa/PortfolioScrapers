import time
import codecs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display


class Browser:

	def __init__(self):
		self.options = webdriver.ChromeOptions()
		self.display = Display(visible=0, size=(1024, 768))
		self.display.start()
		self.options.add_argument('--no-sandbox')
		self.options.add_argument('--disable-setuid-sandbox')
		self.options.add_argument('--disable-dev-shm-usage')
		self.browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options = self.options)
		self.wait = WebDriverWait(self.browser, timeout = 10) # seconds


	def get(self, host):
		self.browser.get(host)



	def getElement(self, by, name):
		try:
			return self.wait.until(EC.presence_of_element_located((by, name)))
		except:
			raise


	def quit(self):
		self.browser.quit()
		self.display.stop()


