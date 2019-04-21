from zeroconf import ServiceBrowser, Zeroconf, ServiceStateChange
from requests.auth import HTTPBasicAuth
import socket
import requests
import time
def fetch_ip():
      return((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close())\
        for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0])
ipNum = 0




#    def remove_service(self, zeroconf, type, name):
 #       print("Service %s removed" % (name,))




class MyListener(object):  
    #def remove_service(self, zeroconf, type, name):
     #   print("Service %s removed" % (name,))
    def __init__(self):
        self.name = 0
    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        # print name, info.get_name(), info.server,
        if info.name == "team20_service._http._tcp.local.":
            self.name = socket.inet_ntoa(info.address)
            print(self.name)

         
if __name__ == '__main__':

    zeroconf = Zeroconf()
    listener = MyListener()
    browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
    time.sleep(5)


    print(listener.name)
    while(1):
   # print(globalAddress)
#    url = "http://" + str(globalAddress)
   # print(url)
 #   r = requests.get(ipNum, auth=HTTPBasicAuth("admin", "secret"))
        print("yes")
        break
