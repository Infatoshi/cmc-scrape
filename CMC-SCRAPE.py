
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

PATH = "C:\\Program Files (x86)\\chromedriver.exe"

option = Options()

option.add_argument("--disable-infobars")
# option.add_argument("start-maximized")
# option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)

driver = webdriver.Chrome(
    chrome_options=option, executable_path=PATH
)

driver.get("https://coinmarketcap.com/")






WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.cmc-cookie-policy-banner__close"))).click()

def find_btc_price():
    btc_priceEl = driver.find_elements_by_xpath("//div[@class='sc-131di3y-0 cLgOOr']/a[@class='cmc-link']/span")
    for elem in btc_priceEl:

        print(elem.text)
        price_1 = elem.text[1:3]


        price_2 = elem.text[4:len(elem.text)]

       
        btc_numerical_price_value = price_1 + price_2
        
        
        break
    return float(btc_numerical_price_value)
# print(btc_priceEl)



    





timeCount = 0
# plot
fig, ax = plt.subplots()
xpoints = np.array([])
ypoints = np.array([])
# active = True
while timeCount != 183:
    time.sleep(61)
    
    x = timeCount
    y = find_btc_price()
    xpoints = np.append(xpoints, x)
    ypoints = np.append(ypoints, y)
    timeCount += 61

        
    plt.plot(xpoints, ypoints, linewidth=2.0)
   


#lim = (lowest amount displayed, maximum amount displayed)
#np.arrange = (tick start position on set axis, tick end position on set axis, numeric value that the ticks takes between each other)
ax.set(xlim=(0, 600), xticks=np.arange(0, 601, 120),
       ylim=(21000, 23000), yticks=np.arange(21000, 23000, 50))

plt.show()