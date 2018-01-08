# -*- coding: utf-8 -*-
import requests
from lxml import html
import sys
from bs4 import BeautifulSoup

print sys.getdefaultencoding()

head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
douban_url = "http://m.didiaokan.com/d/js/js/1458573304.js"

content = requests.get(douban_url, headers=head)
content.encoding = 'utf-8'
html_source = content.content
html_source = html_source.replace("\\", "")

selector = html.fromstring(html_source)

soup = BeautifulSoup(html_source, 'lxml')
items = soup.find_all('li', class_='game-item ')
for item in items:
    div_desc = item.a.find_all('div', class_='desc')
    print "标题:", div_desc[0].text
    print "详情页:", item.a.get('href')
    div_time_short = item.a.find_all('div', class_='time short')
    print "开始时间:", div_time_short[0].text
    team_host = item.a.find_all('div', class_='team')[0]
    team_guest = item.a.find_all('div', class_='right')[0]
    print "主队名字", team_host.span.text
    print "客队名字", team_guest.span.text
    print "主队logo", team_host.img.get('src')
    print "客队logo", team_guest.img.get('src')
    print "\n"
