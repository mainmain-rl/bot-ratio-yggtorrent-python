# import
import requests,logging
from bs4 import BeautifulSoup
from modules.sendMetric import sentDataToDatadog
# loggin
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Class
class yggtorrentClass:

    def __init__(self,yggtorrent_profil_url):
        self.yggtorrentProfilUrl = yggtorrent_profil_url
        self.user = self.yggtorrentProfilUrl.rpartition('/')[2]
        
    def lauchYggtorrentClass(self):
        self.getYggtorrent()
    
    def getYggtorrent(self):
        try:
            self.response = requests.get(self.yggtorrentProfilUrl)
        except Exception as e:
            logger.error(e)
            self.response = False
        self.parsingYggtorrent()
    
    def parsingYggtorrent(self):
        if self.response == False:
            logger.error("def getYggtorrent return False\nyggTorrent call didn't works")
        else:
            parsed_html = BeautifulSoup(self.response.content,features="html.parser")
            # parsing
            upload = float(parsed_html.find("strong", {"style":"font-size: 10px; color:#3dd806"}).text[:-2])
            download = float(parsed_html.find("strong", {"style":"font-size: 10px; color:#ea5656"}).text[:-2])
            ratio = float(upload/download)
            upload = ["upload",upload]
            download = ["download",download]
            ratio = ["ratio",ratio]
            self.list_data = [upload,download,ratio]
            self.sendingYggtorrentData()
    
    def sendingYggtorrentData(self):
        try:        
            for i in self.list_data:
                sentDataToDatadog(i[0],i[1],self.user)
            logger.info("\nStop process : Work done\n---------------")
        except Exception as e:
            logger.error(e)
            logger.error("[ERROR] sendingYggtorrentData : "+ self.user)