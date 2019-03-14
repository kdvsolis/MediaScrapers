from lxml import html
import requests

page = requests.get('http://jpmanga.space/?p=4830')
tree = html.fromstring(page.content)
ptags = tree.xpath('//div[@id="kt-transition"]/div[@id="kt-article"]/p[.//a/@href]')

print ("Extracted links: ")
for ptag in ptags:
    for gchildren in ptag:
        url = gchildren.get("href")
        if(url is not None):
            print(url)