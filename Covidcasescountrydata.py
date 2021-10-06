# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:35:01 2021

@author: natha
"""
## Here I connected to an API that includes data regarding COVID 19 cases,deaths,
## and recovery numbers by country. I have further pulled the data to reflect
## specific data from the country Colombia, and have created a data frame to 
## better visualize it.

import requests
import pandas as pd

response = requests.get('http://covid-api.mmediagroup.fr/v1/cases')
print(response.status_code)

response.json()

jsonresponse = response.json()

print(jsonresponse)

jsonresponseColombia = jsonresponse['Colombia']
jsonresponseColombiaDf = pd.DataFrame(jsonresponseColombia)