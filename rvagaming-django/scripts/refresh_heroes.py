#!/usr/bin/env python
from lxml import etree
from PIL import Image
import csv
import StringIO
import sys
import os
import re
import requests
import urllib
import urllib2

import pprint

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rvagaming-django.settings")

from main.models import Hero

# Create a urllib2 opener object that uses a Chrome user-agent, to avoid
# getting rate-limited by using the default Python urllib2 user-agent.
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]

# use the opener to get the dotabuff main hero page html as a string
html = opener.open('http://www.dotabuff.com/heroes').read()

# instantiate an HTML parser and feed the hero page into it to make a tree
parser = etree.HTMLParser()
tree = etree.parse(StringIO.StringIO(html), parser)

# xpath to all the hero names on the page
heroes_xpath = '//*[@id="page-content"]/section[2]/footer/div/a/div/div[1]/text()'

# create list of all the hero names from the tree
heroes = tree.xpath(heroes_xpath)

# heroes = [
#     'Abaddon',
#     'Alchemist',
#     'Ancient Apparition',
#     'Anti-Mage',
#     'Axe',
#     'Bane',
#     'Batrider',
#     'Beastmaster',
#     'Bloodseeker',
#     'Bounty Hunter',
#     'Brewmaster',
#     'Bristleback',
#     'Broodmother',
#     'Centaur Warrunner',
#     'Chaos Knight',
#     'Chen',
#     'Clinkz',
#     'Clockwerk',
#     'Crystal Maiden',
#     'Dark Seer',
#     'Dazzle',
#     'Death Prophet',
#     'Disruptor',
#     'Doom',
#     'Dragon Knight',
#     'Drow Ranger',
#     'Earth Spirit',
#     'Earthshaker',
#     'Elder Titan',
#     'Ember Spirit',
#     'Enchantress',
#     'Enigma',
#     'Faceless Void',
#     'Gyrocopter',
#     'Huskar',
#     'Invoker',
#     'Io',
#     'Jakiro',
#     'Juggernaut',
#     'Keeper of the Light',
#     'Kunkka',
#     'Legion Commander',
#     'Leshrac',
#     'Lich',
#     'Lifestealer',
#     'Lina',
#     'Lion',
#     'Lone Druid',
#     'Luna',
#     'Lycan',
#     'Magnus',
#     'Medusa',
#     'Meepo',
#     'Mirana',
#     'Morphling',
#     'Naga Siren',
#     "Nature's Prophet",
#     'Necrophos',
#     'Night Stalker',
#     'Nyx Assassin',
#     'Ogre Magi',
#     'Omniknight',
#     'Oracle',
#     'Outworld Devourer',
#     'Phantom Assassin',
#     'Phantom Lancer',
#     'Phoenix',
#     'Puck',
#     'Pudge',
#     'Pugna',
#     'Queen of Pain',
#     'Razor',
#     'Riki',
#     'Rubick',
#     'Sand King',
#     'Shadow Demon',
#     'Shadow Fiend',
#     'Shadow Shaman',
#     'Silencer',
#     'Skywrath Mage',
#     'Slardar',
#     'Slark',
#     'Sniper',
#     'Spectre',
#     'Spirit Breaker',
#     'Storm Spirit',
#     'Sven',
#     'Techies',
#     'Templar Assassin',
#     'Terrorblade',
#     'Tidehunter',
#     'Timbersaw',
#     'Tinker',
#     'Tiny',
#     'Treant Protector',
#     'Troll Warlord',
#     'Tusk',
#     'Undying',
#     'Ursa',
#     'Vengeful Spirit',
#     'Venomancer',
#     'Viper',
#     'Visage',
#     'Warlock',
#     'Weaver',
#     'Windranger',
#     'Winter Wyvern',
#     'Witch Doctor',
#     'Wraith King',
#     'Zeus']

for hero in heroes:
    new_hero, created = Hero.objects.get_or_create(name=hero)
    new_hero.save()