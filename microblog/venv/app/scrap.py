#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart

chromedriver_path = 'C:/{YOUR PATH HERE}/chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(executable_path = chromedriver_path)
sleep(2)