'''
Script for scraping dota 2 patch notes
'''
from bs4 import BeautifulSoup
import requests


url = 'http://www.dota2.com/patches/7.27d'
response = requests.get(url)

if response.status_code != 200:
    print('something went wrong')
    quit()

raw_html = response.text
soup = BeautifulSoup(raw_html, 'html.parser')

body = soup.body
main_contents = body.find('div', attrs={'class': 'MainContents'})

items_section = main_contents.find('div', attrs={'id': 'ItemsSection'})

items_header = items_section.find('p', attrs={'class': 'SectionHeader'})
print(items_header.string)

item_notes = items_section.find_all('div', attrs={'class': 'ItemNotes'})
for item_note in item_notes:
    item_name = item_note.find('div', attrs={'class': 'ItemName'})
    print(item_name.string)

    patch_notes = item_note.find_all('li', attrs={'class': 'PatchNote'})
    for patch_note in patch_notes:
        print(patch_note.string.replace('\n', ''))

print()

heroes_section = main_contents.find('div', attrs={'id': 'HeroesSection'})

heroes_header = heroes_section.find('p', attrs={'class': 'SectionHeader'})
print(heroes_header.string)
