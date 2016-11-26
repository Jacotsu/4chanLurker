#!/usr/bin/python
#Released under apache license 2.0, no warranties included in this software and it's not meant for
#any production purpose. I decline any responsibility
#copyright 2016 Raffaele Di Campli
from PostSifter import *
import logging, sys, subprocess, time, threading
import json

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    config = []
    with open("conf.json") as configFile:
            config = json.load(configFile)
            config["boards"] = config["boards"].split(" ")

    logging.debug("main: {}".format(config))

    sifter = PostSifter(config)
    post = sifter.get_random_post()

    logging.debug("main: display -resize {}x{} -flatten -backdrop -background '#3f3f3f'".format(config["width"],config["height"]))

    p = subprocess.Popen(["display", "-flatten", "-backdrop", "-background", "#3f3f3f","-resize", "{}x{}".format(config["width"],config["height"])],stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    "must use multithreading because subprocess.communicate() is blocking"
    thr = threading.Thread(target = p.communicate, args = (post.image,))
    thr.start()

    logging.debug("main: i'm going to sleep")

    time.sleep(config["delay"])
    p.terminate()
    thr.join()




