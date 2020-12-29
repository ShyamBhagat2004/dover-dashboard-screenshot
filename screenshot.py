from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
options = Options()
options.add_argument('--headless')

# take screenshot
driver = webdriver.Firefox(options=options)
driver.set_window_size(1920,1080)
driver.get('https://share.geckoboard.com/dashboards/WDXKP2FYXSALD5CM')
time.sleep(8)

driver.save_screenshot("pageImage.png")
"""
# crop image
x = location['x'];
y = location['y'];
width = location['x']+size['width'];
height = location['y']+size['height'];
im = Image.open('pageImage.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save('element.png')
"""
driver.quit()