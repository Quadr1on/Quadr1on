from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# set download directory for Chrome
options = Options()
options.add_experimental_option("prefs", {
  "download.default_directory": "C:\Users\georg\Downloads\Amma SAS",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

# start Chrome in headless mode
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

# open WhatsApp Web
browser.get('https://web.whatsapp.com/')

# wait for QR code scan
time.sleep(15)

# find and click on PDF file attachment
pdf_attachment = browser.find_element_by_xpath('//*[contains(@data-filename, ".pdf")]')
pdf_attachment.click()

# wait for download to complete
time.sleep(5)

# close the browser
browser.quit()
