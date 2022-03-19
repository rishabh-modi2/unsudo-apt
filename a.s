import praw, os, random, requests, schedule, cv2
import urllib.request
from time import sleep
reddit = praw.Reddit(
    client_id="j3W2u4EWnddWZy5XQxvA7g",
    client_secret="LXNRfWMHx7snXTMu2-Fkv1oq4hLPJw",
    user_agent="anas",
    username="Dangerous_Salary_388",
    password="Rishabh@2021",
    ratelimit_seconds=900,
)


# reddit = praw.Reddit(
#     client_id="j3W2u4EWnddWZy5XQxvA7g",
#     client_secret="LXNRfWMHx7snXTMu2-Fkv1oq4hLPJw",
#     user_agent="anas",
#     username="Dangerous_Salary_388",
#     password="03rishabh",
#     ratelimit_seconds=900
# )
#def get_first_frame(video_path: pathlib.Path) -> pathlib.Path:
os.system('rm video.mp4 thumb.png')
title = input('enter title: ')
url_link = input('enter The video link:  ')
urllib.request.urlretrieve(url_link, 'video.mp4')

vidcap = cv2.VideoCapture(str('video.mp4'))
success, image = vidcap.read()
if success:
  cv2.imwrite('thumb.png', image)  # save frame as JPEG file


sub = ['IndianDankMemes', 'dankinindia', 'HindiMemes']
for vid in sub:
  print(vid)
  reddit.subreddit(vid).submit_video(title, 'video.mp4', thumbnail_path='thumb.png')
# for subm in reddit.subreddit("all").top(limit=25)
