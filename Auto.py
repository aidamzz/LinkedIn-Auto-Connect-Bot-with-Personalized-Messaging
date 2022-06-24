from collections import UserDict
from distutils.command.config import config
import os,random, sys, time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('D:/Algorithm/linkedin/LinkedIn-Auto-Connect-Bot-with-Personalized-Messaging/Driver/chromedriver.exe')

browser.get('https://www.linkedin.com/uas/login')

file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]

elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()

visitingProfileID = '/in/aida-mohaghegh-zade/'
fulllink = 'https://www.linkedin.com/' + visitingProfileID
browser.get(fulllink)

visitedProfiles = []
profilesQueued = []

def getNewProfileIDs(soup, profilesQueued):
    profilesID = []
    pav = soup.find('section', {'class': 'artdeco-card ember-view mt2'})
    pav = pav.find('section', {'class':'pt4 pb3 ph4'})
    all_links = pav.findAll('a', {'class': 'ember-view display-flex link-without-hover-visited'})
    for link in all_links:

        userID = link.get('href')
        if ((userID not in profilesQueued) and (userID not in visitedProfiles)):
            profilesID.append(userID)
    return profilesID


profilesQueued = getNewProfileIDs(BeautifulSoup(browser.page_source,features="html.parser"), profilesQueued)

while profilesQueued:

    visitingProfileID = profilesQueued.pop()
    visitedProfiles.append(visitingProfileID)
    fulllink = 'https://www.linkedin.com/' + visitingProfileID
    browser.get(fulllink)
    bt = browser.find_element(by=By.CLASS_NAME, value='artdeco-button')
    bt.click()
    browser.find_element_by_class_name('artdeco-button artdeco-button--2 artdeco-button--primary ember-view ml1').click()




























