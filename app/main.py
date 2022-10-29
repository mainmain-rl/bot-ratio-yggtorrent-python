import os
import logging
from modules.yggtorrent import yggtorrentClass

# loggin
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("\n---------------\nStarting process")

# get variable from env
try:
    yggtorrent_profil_url = os.environ['YGGTORRENT_PROFILE_URL']
    logger.info("----- env variables -----")
    logger.info("YGGTORRENT_PROFILE_URL="+yggtorrent_profil_url)
except Exception as e:
    logger.error(e)


my_call_ygg_torrent = yggtorrentClass(yggtorrent_profil_url)
my_call_ygg_torrent.lauchYggtorrentClass()