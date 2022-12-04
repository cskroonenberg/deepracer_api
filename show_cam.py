import yaml
import os
import time
from aws_deepracer_control_v3 import Client
from core import deepracer_cam
import cv2

window_name = "deepracer_camera_left"
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path,"deepracer-config.yaml"), 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

client = Client(password=cfg['password'], ip=cfg['ip'])

camera_feed_one = deepracer_cam.DeepracerCam(client)
camera_feed_one.start()
time.sleep(1)
i = 0
while True:
    image = camera_feed_one.get_image(timeout=1)
    if image is not None:
        cv2.imshow(window_name, image)
    else:
        print("waiting", i)
        i = i + 1
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        exit(0)
