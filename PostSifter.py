#!/usr/bin/python
#Released under apache license 2.0, no warranties included in this software and it's not meant for
#any production purpose. I decline any responsibility
#copyright 2016 Raffaele Di Campli
#

import json
import urllib.request
from random import randint
import logging

class PostSifter():
    def __init__(self,config):
           self.config = config
           self.logger = logging.getLogger()

    def get_random_post(self, board=None):
        "choose a random board if you didn't specify any"
        if board is None:
            board = self.config["boards"][randint(0,len(self.config["boards"])-1)]

        data = []
        "this code gets all the threads in the specified board"
        with urllib.request.urlopen("http://a.{}/{}/threads.json".format(self.config["chanDomain"], board)) as page:
            data = json.loads(page.read().decode("utf-8"))

        postNumbers = []
        for page in data:
            for thread in page["threads"]:
                postNumbers.append(thread["no"])

        "chooses a random thread"
        no = postNumbers[randint(0,len(postNumbers)-1)]
        with urllib.request.urlopen("http://a.{}/{}/thread/{}.json".format(self.config["chanDomain"], board, no)) as page:
            data = json.loads(page.read().decode("utf-8"))

        "gets a random post from the random thread"
        chosen_one = []

        "A post without an image is boring"
        while len(data["posts"]) > 0:
            chosen_one = data["posts"].pop(randint(0,len(data["posts"])-1))
            if "filename" in chosen_one:
                break

        com = ""
        if "com" in chosen_one:
            com = chosen_one["com"]

        "downloads the image in memory"
        self.logger.debug("PostSifter: {}".format(chosen_one))
        self.logger.info("PostSifter: http://i.{}/{}/{}{}".format(self.config["chanDomain"],board,chosen_one["tim"],chosen_one["ext"]))

        with urllib.request.urlopen("http://i.{}/{}/{}{}".format(self.config["chanDomain"],board,chosen_one["tim"],chosen_one["ext"])) as page:
            return Post(page.read(),com)

class Post():
    def __init__(self,image,text):
        self.image = image
        self.text = text




