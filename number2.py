from lxml import html
import requests

page = requests.get('http://www.lovelyanime.com/Cardfight-Vanguard-G-Next/41/')
tree = html.fromstring(page.content)
links = tree.xpath('//div[@class="nav_ver"]/a/@href')

print ("Extracted links: ")
for link in links:
    subpage = requests.get(link)
    branch = html.fromstring(subpage.content)
    videolink = branch.xpath('//div[@class="prw"]/iframe/@src')
    print (videolink[0])
