# SoccerNet YOLO Tracking Project

This project uses YOLO to track soccer players, the ball, and referees in SoccerNet videos.

##  Requirements
- Python 3.13.2
- YOLOv8
- SoccerNet dataset

    mySoccerNetDownloader.downloadDataTask(task="tracking", split=["train", "test", "challenge"])

    mySoccerNetDownloader.downloadDataTask(task="tracking-2023", split=["train", "test", "challenge"])

##  Installation

### 1. Clone the repository:
```bash
git clone https://github.com/<your-username>/soccer-yolo-tracking.git
cd soccer-yolo-tracking
