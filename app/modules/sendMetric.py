# import
import time
from datadog import initialize, api
import os
import logging

# loggin
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# get variable from env
try:
    datadog_api_key = os.environ['DD_API_KEY']
    datadog_api_host = os.environ['DD_SITE']
    yggtorrent_profil_url = os.environ['YGGTORRENT_PROFILE_URL']
    logger.debug("----- env variables -----")
    logger.debug("DD_API_KEY="+datadog_api_key)
    logger.debug("DD_SITE="+datadog_api_host)
    logger.debug("YGGTORRENT_PROFILE_URL="+yggtorrent_profil_url)
except Exception as e:
    logger.error(e)

# set env for datadog
options = {
    'api_key': datadog_api_key,
    'api_host': datadog_api_host,
}

try:
    initialize(**options)
    logger.info("Datadog initializer OK")
except Exception as e:
    logger.error(e)

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
        logger.info("Sending "+name_metric+" metric | "+user)
    except Exception as e:
        logger.error(e)