import yaml
import os
import time
import logging
from aws_deepracer_control_v3 import Client

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path,"deepracer-config.yaml"), 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    client = Client(password=cfg['password'], ip=cfg['ip'])

    logging.info("print vehicle info")
    client.show_vehicle_info()
    car_battery_level = client.get_battery_level()
    logging.info(u"car_battery_level %s", car_battery_level)
    logging.info("set to manual mode.")
    client.set_manual_mode()
    # throttle = client.get_calibration_throttle()
    # logging.info(u"throttle %s", throttle)
    logging.info("start the car")
    client.start_car()
    
    # start listening to joystick
    client.move(0.0, 1.0, .50)
    logging.debug(u"client.move %s %s %s", 0.0, 1.0, 1.0)
    time.sleep(2)
    client.move(0.0, 0.0, 1.0)
    logging.debug(u"client.move %s %s %s", 0.0, 0.0, 1.0)

    client.stop_car()

if __name__ == "__main__":
    main()
