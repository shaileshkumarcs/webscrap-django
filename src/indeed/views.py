import json
import math
import re
import tempfile
from bs4 import BeautifulSoup
import threading
import time

import requests
from django.contrib import messages
from django.core import files
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from selenium import webdriver


class ScrapIndeed(TemplateView):
    def get(self, request, *args, **kwargs):
        # browser = webdriver.PhantomJS()
        browser = webdriver.Chrome()
        # browser.get('https://stackoverflow.com/')
        browser.get('https://www.indeed.co.in/jobs?q=php&l=Bengaluru%2C%20Karnataka&vjk=f1adbfff100cbb6d')
        html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')
        # for link in soup.findAll('h2'):
        # print(soup.find('div',{'id':'left-sidebar'}).findAll('a')[2].text)
        summ = soup.find('div', {'id': 'vjs-desc'})
        for su in summ.findAll('p'):
            print(su.text)
        # print(soup.find('div',{'id':'vjs-desc'}))

        return HttpResponse('Hello1')