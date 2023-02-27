import yaml
import os
import time
import logging
from aws_deepracer_control_v3 import Client
import rclpy
from rclpy.node import Node

class ThrottleSubscriber(Node):
    def __init__(self) -> None:
        super().__init__('throttle_sub')
        self.subscription = self.create_subscription(
            xxx,
            'acceleration',
            10
        )

    def sub_callback(self, msg):
        pass


class SteerSubscriber(Node):
    def __init__(self) -> None:
        super().__init__('steer_sub')
        self.subscription = self.create_subscription(
            xxx,
            'steering',
            self.sub_callback,
            10
        )

    def sub_callback(self, msg):
        pass

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path,"deepracer-config.yaml"), 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    client = Client(password=cfg['password'], ip=cfg['ip'])

    logging.info("print vehicle info")
    client.show_vehicle_info()
    car_battery_level = client.get_battery_level()
    logging.info(u"car_battery_level %s", car_battery_level)
    logging.info("setting to manual mode...")
    client.set_manual_mode()
    logging.info("manual mode set")

    # throttle = client.get_calibration_throttle()
    # logging.info(u"throttle %s", throttle)

    logging.info("start the car...")
    client.start_car()
    logging.info("car started")
    
    # start listening to joystick
    # client.move(0.0, 1.0, .50)
    # logging.debug(u"client.move %s %s %s", 0.0, 1.0, 1.0)
    # time.sleep(2)
    # client.move(0.0, 0.0, 1.0)
    # logging.debug(u"client.move %s %s %s", 0.0, 0.0, 1.0)

    rclpy.init(args=None)
    throt_sub = ThrottleSubscriber()
    steer_sub = SteerSubscriber()

    rclpy.spin(throt_sub)
    rclpy.spin(steer_sub)

if __name__ == "__main__":
    main()