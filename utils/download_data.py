# Shaan Sekhon 

import SoccerNet
from SoccerNet.Downloader import SoccerNetDownloader

# Create a downloader object
my_downloader = SoccerNetDownloader(LocalDirectory="./data")

# Download bounding box data
my_downloader.downloadDataTask(task="tracking")
