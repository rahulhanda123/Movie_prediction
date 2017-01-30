import numpy as np
import pandas as pd
from pandas import DataFrame, read_csv 
import urllib
import time
import requests
import csv
import matplotlib.pyplot as plt

def getSearchId(id):
    searchId = 'tt'
    if len(id) == 5 :
        searchId = searchId + '00'+ str(id)
    if len(id) == 6 :
        searchId = searchId + '0'+ str(id)
    if len(id) == 7 :
        searchId = searchId + str(id)
    return searchId
def makeCall_getData(id):
    f = { "i" : id, "tomatoes" : 'true' }             
    html_doc = "http://www.omdbapi.com/?"+urllib.urlencode(f)
    
  
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    try:
        response = opener.open(html_doc)
        if response.getcode() == 200:
            soup = BeautifulSoup(response. read().decode('utf-8'), 'html.parser') 
            soup_json = json.loads(str(soup))
            #soup_dumped_json = json.dumps(json.loads(str(soup)))
            #print "response inside if ",response.getcode()
            print "inside try ",id
            return soup_json
    except :
        print "inside Exception"
        time.sleep(5)
        makeCall_getData(id)
        
#method to get all the values ,input is the csv dataframe
def get_all_data(df):
    for i in range(0,len(df)):
        time.sleep(1)
        id_val = df.imdbId[i]    
        data_json = makeCall_getData(getSearchId(str(df.imdbId[i])))
        #current_df = df.query('imdbId =='+ str(id_val))
        if not data_json == None:
            for key, value in data_json.iteritems():
                df.loc[df['imdbId'] == id_val,key] = value