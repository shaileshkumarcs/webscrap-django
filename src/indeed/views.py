import json
import math
import re
import tempfile
from bs4 import BeautifulSoup
import threading
import time
import csv
import datetime

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
        browser.get('https://www.indeed.co.in/jobs?q=php%20developer&l=Bengaluru%2C%20Karnataka&vjk=81ac24c72ac8aad6')
        html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')

        name = 'ttt'#datetime.datetime.now().strftime("%d%m%y%H%I%p")
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename= "Details.csv"'

        writer = csv.writer(response)
        writer.writerow(['Job Title', 'Company Name', 'City', 'State','Job Details','Experience','Education'])

        jobdetails = ''
        summ = soup.find('div', {'id': 'vjs-desc'})
        for su in summ.findAll('p'):
            jobdetails += ' '+su.findChildren('b').text
            ul = summ.find('ul')
            if ul:
                for li in ul.findAll('li'):
                    jobdetails += ' ' + (li.text)
            jobdetails += ' '+ (su.text) #.encode('utf-8').strip()

        data = (soup.find('span', {'id': 'vjs-loc'}).text).split(',')


        writer.writerow(
            [soup.find('div',{'id':'vjs-jobtitle'}).text,
             soup.find('span',{'id':'vjs-cn'}).text,
             data[0],
             data[1],
             jobdetails,
             'Experience',
             'Education'])



        # print(soup.find('div',{'id':'vjs-jobtitle'}).text)
        # print(soup.find('span',{'id':'vjs-cn'}).text)
        # print(soup.find('span',{'id':'vjs-loc'}).text)
        # summ = soup.find('div', {'id': 'vjs-desc'})
        # for su in summ.findAll('p'):
        #     ul = summ.find('ul')
        #     for li in ul.findAll('li'):
        #         print((li.text).encode('utf-8').strip())
        #     print((su.text).encode('utf-8').strip())
        #
        #
        # return HttpResponse("HELLO")
        return response


class ExportCsv(TemplateView):
    def get(self, request, *args, **kwargs):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        writer = csv.writer(response)
        writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
        writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

        return response