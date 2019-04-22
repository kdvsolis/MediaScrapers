from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from lxml import html
import time
import traceback

chrome_options = Options()  
chrome_options.add_argument("--headless") 
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

url = "https://horriblesubs.info/shows/ballroom-e-youkoso/"
driver.get(url)

id = 0
while driver.find_elements_by_class_name("show-more")[0].get_attribute("innerHTML") != "No more results":
    try:
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.ID, str(id)))
        )
        button = driver.find_element_by_id(str(id))
        button.click()
        id = id + 1
        print (driver.find_elements_by_class_name("show-more")[0].get_attribute("innerHTML").encode("UTF-8"))
    except Exception:
        print ("Done loading links")
        
tree = html.fromstring(driver.find_elements_by_class_name("hs-shows")[0].get_attribute("innerHTML").encode("utf-8"))
torrents480p = tree.xpath('//div[@class="rls-info-container"]/div[@class="rls-links-container"]/div[@class="rls-link link-480p"]/span[@class="dl-type hs-torrent-link"]/a/@href')
xdcc480p = tree.xpath('//div[@class="rls-info-container"]/div[@class="rls-links-container"]/div[@class="rls-link link-480p"]/span[@class="dl-type hs-xdcc-link"]/a/@href')
ddl480p = tree.xpath('//div[@class="rls-info-container"]/div[@class="rls-links-container"]/div[@class="rls-link link-480p"]/span[@class="dl-type hs-ddl-link"]/a/@href')

torrents720p = tree.xpath('//div[@class="rls-info-container"]/div[@class="rls-links-container"]/div[@class="rls-link link-720p"]/span[@class="dl-type hs-torrent-link"]/a/@href')
xdcc720p = tree.xpath('//div[@class="rls-info-container"]/div[@class="rls-links-container"]/div[@class="rls-link link-720p"]/span[@class="dl-type hs-xdcc-link"]/a/@href')
ddl720p = tree.xpath('//div[@class="rls-info-container"]/div[@class="rls-links-container"]/div[@class="rls-link link-720p"]/span[@class="dl-type hs-ddl-link"]/a/@href')

torrents1080p = tree.xpath('//div[@class="rls-info-container"]/div[@class="rls-links-container"]/div[@class="rls-link link-1080p"]/span[@class="dl-type hs-torrent-link"]/a/@href')
xdcc1080p = tree.xpath('//div[@class="rls-info-container"]/div[@class="rls-links-container"]/div[@class="rls-link link-1080p"]/span[@class="dl-type hs-xdcc-link"]/a/@href')
ddl1080p = tree.xpath('//div[@class="rls-info-container"]/div[@class="rls-links-container"]/div[@class="rls-link link-1080p"]/span[@class="dl-type hs-ddl-link"]/a/@href')

print ("Extracted Links:")
print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print ("Torrent 480p:")
for torrent480p in torrents480p:
    print (torrent480p)
  
print ("XDCC 480p:")
for xdcc in xdcc480p:
    print (xdcc)
    
print ("DDL 480p:")
for ddl in ddl480p:
    print (ddl)
    
print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")  
print ("Torrent 720p:")
for torrent720p in torrents720p:
    print (torrent720p)
    
print ("XDCC 720p:")
for xdcc in xdcc720p:
    print (xdcc)
    
print ("DDL 720p:")
for ddl in ddl720p:
    print (ddl)
    
print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")  
print ("Torrent 1080p:")
for torrent1080p in torrents1080p:
    print (torrent1080p)
    
print ("XDCC 1080p:")
for xdcc in xdcc1080p:
    print (xdcc)
    
print ("DDL 1080p:")
for ddl in ddl1080p:
    print (ddl)