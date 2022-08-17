# import
import requests
import time
from datadog import initialize, api
from bs4 import BeautifulSoup
import os

# get variable from env
try:
    datadog_api_key = os.environ['DD_API_KEY']
    datadog_api_host = os.environ['DD_SITE']
    yggtorrent_profil_url = os.environ['YGGTORRENT_PROFILE_URL']
except Exception as e:
    print(e)

# set env for datadog
options = {
    'api_key': datadog_api_key,
    'api_host': datadog_api_host,
}
initialize(**options)

# yggtorrent url profile
yggtorrent_url = yggtorrent_profil_url

# Function
## Function send fata to datadog
def sentDataToDatadog(name_metric,metric,user):
    try:
        api.Metric.send(
            metric='yggtorrent.metric.'+name_metric,
            points=[(int(time.time()), float(metric))],
            tags=["yggAccount:"+user],
            type='gauge'
        )
        print("Sending "+name_metric+" metrics | "+user)
    except Exception as e:
        print(e)

## Function global
def botRatioYggtorrent():
    while True:
        # get the name of user for datadog tag
        user = yggtorrent_url.rpartition('/')[2]

        try:
            response = requests.get(yggtorrent_url)
            parsed_html = BeautifulSoup(response.content,features="html.parser")
            
            # parsing
            upload = float(parsed_html.find("strong", {"style":"font-size: 10px; color:#3dd806"}).text[:-2])
            download = float(parsed_html.find("strong", {"style":"font-size: 10px; color:#ea5656"}).text[:-2])
            ratio = float(upload/download)
            download = ["download",download]
            ratio = ["ratio",ratio]
            list_data = [upload,download,ratio]
            
            # sent data to datadog
            for i in list_data:
                sentDataToDatadog(i[0],i[1],user)
                    
        except Exception as e:
            print(e)
            print("[ERROR] : get yggtorrent or parsingfor "+ user)
        
        #WAITING 60 SEC    
        time.sleep(60)
    
botRatioYggtorrent()
