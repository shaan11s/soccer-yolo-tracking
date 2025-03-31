import os
import logging
from SoccerNet.Downloader import SoccerNetDownloader

# Setup logging
logging.basicConfig(level=logging.INFO)

# Path setup
path = os.path.join(".", "data")  # Local directory set to ./data
mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory=path)

# Downloading data with error handling
try:
    logging.info("Downloading SoccerNet tracking data...")
    mySoccerNetDownloader.downloadDataTask(task="tracking", split=["train", "test", "challenge"])
    logging.info("Downloading SoccerNet tracking-2023 data...")
    mySoccerNetDownloader.downloadDataTask(task="tracking-2023", split=["train", "test", "challenge"])
    logging.info("Download complete!")
except Exception as e:
    logging.error(f"Error downloading SoccerNet data: {e}")

    #manual download was done later of additional dataset
    #https://www.kaggle.com/datasets/borhanitrash/football-players-detection-dataset?resource=download

