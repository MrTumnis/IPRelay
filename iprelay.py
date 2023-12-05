#!/usr/bin/python

import subprocess
import piplates.RELAYplate as RELAY
import time
import json
import os.path
import ipaddress
import sys

RELAY.relayON(0,1)


delay = 10
relay_add = 0
relay_num = 1


file = ("target.json")


#open json file and convert to dictionary 
def file_read():
    with open(file, "r", encoding = "utf-8") as r:
        data = json.loads(r.read())
        return data

#write to json file
def file_write(write):
    with open(file, "w", encoding = "utf-8") as w:
         json.dump(write,w)
            

#create a JSON file for IP storage
def json_create():
    dic = {"data":{"IP":"$"}}
    file_write(dic)

    print("JSON has been created")
    main()
# write user defined IP to the JSON file
def write():

    ip_input = input("Enter IP Address: ")
    ipaddress.ip_address(ip_input)
    data = file_read()
    data['data']['IP'] = ip_input    
    file_write(data)

    print("Stand by for ping response...")
    main() 

#trigger the relay to power cycle the device
def relay(delay,add,num):

    data = file_read()
    ipaddr = data["data"]["IP"]
   
    try:
        output = subprocess.check_output(['ping', '-c 4', '{}'.format(ipaddr)])
        print(output)
        return True

    except:
        print(f"NO RESPONSE: Triggering Relay for {delay} seconds")
        RELAY.relayOFF(add,num)
        time.sleep(delay)
        RELAY.relayON(add,num)

    finally:
        print("Sequence Finished")
        sys.exit()

def sequence():
    
    data = file_read()
    check = data["data"]["IP"]
    

    if check == "$":
        write()

    if check != "$":
        relay(delay,relay_add,relay_num)

#    elif:
#        print("ERROR")
    

def main():
    if os.path.isfile("target.json") == False:
        json_create()
    elif os.path.isfile("target.json") == True:
        sequence()


if __name__ == "__main__":
    main()


