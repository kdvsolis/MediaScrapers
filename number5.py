from lxml import html
import requests
import cfscrape

scraper = cfscrape.create_scraper()
page = scraper.get("http://www.mangago.me/read-manga/pendulum_kemonohito_omegaverse/").content
tree = html.fromstring(page)
pics = tree.xpath('//div[@id="page"]/div[@class="people-panel w600"]/div[@class="article"]/div[@id="information"]/div/div[@class="left cover"]/img/@src')

print ("Extracted link: ")
if (pics is not None):
    print (pics[0])