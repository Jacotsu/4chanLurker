#!/usr/bin/python3
# Released under apache license 2.0, no warranties
# included in this software and it's not meant for
# any production purpose. I decline any responsibility
# copyright 2016 Raffaele Di Campli
from postsifter import PostSifter, Post
import logging
import sys
import subprocess
import time
import threading
import json

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    config = []
    with open("conf.json") as configFile:
            config = json.load(configFile)
            config["boards"] = config["boards"].split(" ")
            config["command"] = config["command"].split(" ")

    logging.debug("main: {}".format(config))

    sifter = PostSifter(config)
    post = sifter.get_random_post()

    logging.debug("main: {}".format(config["command"]))

    p = subprocess.Popen(config["command"], stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)

    #must use multithreading because subprocess.communicate() is blocking
    thr = threading.Thread(target=p.communicate, args=(post.image,))
    thr.start()

    logging.debug("main: i'm going to sleep")

    time.sleep(config["delay"])
    p.terminate()
    thr.join()
