from six.moves import input
from zeroconf import ServiceBrowser, Zeroconf, ServiceInfo
from flask import Flask, request, render_template, Response, url_for
from functools import wraps
import datetime
import socket
import time
import pdb
import pymongo

app = Flask(__name__)
#!/usr/bin/env python3

# imports for Canvas API
import servicesKeys
import urllib as ul
from urllib.error import HTTPError as hpe

# General imports used for multiple sections
import json
import os, sys, time
import requests


 
# Access token and API URL
parent_dir = os.getcwd()
#parent_dir = '/home/pi/projects/Project3/'
web = 'https://vt.instructure.com/api/v1/courses/'
ckey = servicesKeys.ckey
course = '83639'
can_file = 'Assignment3.pdf'

# function to download file from canvas
payload = {'access_token' : ckey, 'search_term' : can_file}
r = requests.get(web+course+'/files', params = payload)
#url = web+course+'/files?search_term='+can_file+'&access_token='+ckey

try:
    # Fetch the course details
    can_file = ul.request.urlopen(r.url).read()

    # Parse the json response
    files = json.loads(can_file.decode('utf-8'))
    for file in files:
        # Deciding file location to save file
        file_loc = parent_dir
        print('file location:', file_loc)
        # Finding file url to download from
        file_url = file['url']
        print('url:', file_url)
        # Finding file to download from that url
        file_name = file['filename']
        print('filename:', file_name)
        file_path = file_loc + file_name
        # Downloading the file to the file location
        print('Downloading:', file_path)
        if not os.path.isfile(file_path):
            ul.request.urlretrieve(file_url, file_path)

except hpe as fileE:
    print('Error: No files with the given id')



class MyListener(object):
    # def remove_service(self, zeroconf, type, name):
    #  print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        # print name, info.get_name(), info.server,
        #        print name, info
        # @        print("no")
        if info.name == "team20_led._http._tcp.local.":
            global ledAddress
            #            print("yes")
            ledAddress = socket.inet_ntoa(info.address)
#            print("ip address ", ledAddress)


# zeroconf = Zeroconf()
# listener = MyListener()
# browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
# try:
#    input("Press enter to exit...\n\n")
# finally:
#    zeroconf.close()


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    userList = col.find_one({"user": username})
    passList = col.find_one({"Pass": password})
    # return username == "admin" and password == "secret"
    return userList != None and passList != None


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        "Could not verify your access level for that URL.\n"
        "You have to login with proper credentials",
        401,
        {"WWW-Authenticate": 'Basic realm="Login Required"'},
    )


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated


# color = "Red"
# dimness = 50
# status = "on"


templateData = {
    "title": "HELLO!",
    "time": "",
    "color": "white",
    "dimness": "0",
    "led": "off",
}




@app.route("/", methods=["GET"])
@requires_auth
def hello():
    if request.method == "GET":
        # print(command)
        #        pdb.set_trace()
        now = datetime.datetime.now()
        timeString = now.strftime("%Y-%m-%d %H:%M")
        # templateData = {
        #   "title": "HELLO!",
        #  "time": timeString,
        # "color": color,
        # "dimness": str(dimness),
        # "led": status
        # }
        templateData["time"] = timeString
        #        templateData["color"] = "white"
        #      templateData["dimness"] = "0"
        #     templateData["led"] = "off"
        return render_template("main.html", **templateData)


#        js = json.dumps(templateData)

#       resp = Response(js, status=200, mimetype='application/json')
#      resp.headers['Link'] = 'something'
#     return resp


@app.route("/LED", methods=["GET"])
@requires_auth
def handle_led():
    if request.method == "GET":
        #       pdb.set_trace()
        #   print(request.args)
        argList = request.args
        status = argList.get("status")
        color = argList.get("color")
        dimness = int(argList.get("intensity"))
        now = datetime.datetime.now()
        timeString = now.strftime("%Y-%m-%d %H:%M")
        templateData["time"] = timeString
        templateData["color"] = color
        templateData["dimness"] = str(dimness)
        templateData["led"] = status

        # templateData = {
        #   "title": "HELLO!",
        #  "time": timeString,
        # "color": color,
        # "dimness": str(dimness),
        # "led": status
        # }
        return render_template("main.html", **templateData)
    # js = json.dumps(templateData)

    # resp = Response(js, status=200, mimetype='application/json')
    # resp.headers['Link'] = 'something'

    # return resp


@app.route("/Canvas", methods=["GET"])
@requires_auth
def handle_canvas():
    if request.method == "GET":
        argList = request.args
        filename = argList.get("file")
        return render_template("main.html", **templateData)



# Pymongo
client = pymongo.MongoClient(
    host="localhost",
    port=27017,
    username="admin",
    password="idontknow",
    authSource="ECE4564_Assignment_3",
    authMechanism="SCRAM-SHA-1",
)
db = client.ECE4564_Assignment_3
col = db.service_auth
if __name__ == "__main__":
    #   app.run(host='0.0.0.0', port=80, debug=True)

def fetch_ip():
      return((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close())\
        for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0])




if __name__ == "__main__":
    #   app.run(host='0.0.0.0', port=80, debug=True)
    ledColors = {"red", "blue", "green", "magenta", "cyan", "yellow", "white"}
    ipAddr = fetch_ip()

    zeroconf = Zeroconf()
  #  service = ServiceInfo("_http._tcp.local.", "service20._http._tcp.local.",
 #socket.inet_aton(fetch_ip()), 5000, 0, 0, ledColors, "service20.local.")
 #   zeroconf.register_service(service)

    listener = MyListener()
    browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
    time.sleep(1)


    user1 = {"user": "Kishan", "Pass": "Something", "Delete": "True"}
    user2 = {"user": "Buse", "Pass": "Honaker", "Delete": "True"}
    user3 = {"user": "Ethan", "Pass": "Password", "Delete": "True"}
    posts = [user1, user2, user3]
    col.insert_many(posts)

#    zeroconf.register_service(service)

    # zeroconf.close()
    app.run(host="0.0.0.0", port=80, debug=True)
    # print("fff")
    try:
        print()
    finally:
        zeroconf.close()
        col.delete_many({"Delete": "True"})
