#!/usr/bin/env python3

import notify2
import requests
import json
import time
import os

#id is the variable that contains all id's for messages
id = []
"""This function takes in an id, and get's updates for announcements."""
def getupdates(id):
    #url for where to grab announcements
    url = "url for canvas"  # need to fill in url for canvas
    #get's the courses with there codes
    querystring = {"context_codes[]":["course 1","course 2"]}  # fill in all the courses
    #header with token key
    headers = {
        'authorization': "",  # bearer info
        'cache-control': "no-cache",
        'postman-token': ""  # postman token
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    resp = response.text
    data = json.loads(resp)
    title = []
    message = []
    #loop through all the responses
    for i in data:
        #if id exists skip do not add it to the list
        if id.__contains__(i['id']):
            print("exists")
        else:
            title.append(i['title'])
            message.append(i['message'])
            id.append(i['id'])
            """log to file"""
            t = i['title']
            m = i['message']
            os.system('echo "' + str(t) + '" >> log.txt')
            os.system('echo "' + str(m) + '" >> log.txt')
            os.system('echo "------------------" >> log.txt')
            """log ends here"""
    """creates an notify2 instance and shows the massages if it contains 1 or more messages."""
    notify2.init('Canvas')
    if len(title) > 0:
        n = notify2.Notification(title[0], message[0])
        n.set_timeout(5000)
        n.show()
        time.sleep(5)
        for t in range(0,len(title)-1):
            n.update(title[t+1], message[t+1])
            n.show()
            time.sleep(5)
"""checkes for messages, then sleeps for 10min. loops forever"""
while(True):
    getupdates(id)
    time.sleep(60 * 10)
