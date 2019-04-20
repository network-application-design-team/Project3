from zeroconf import ServiceBrowser, Zeroconf

def fetch_ip():
      return((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close())\
        for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0])



class MyListener:

#    def remove_service(self, zeroconf, type, name):
 #       print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        #print("Service %s added, service info: %s" % (name, info))
         

zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
ipAddr = fetch_ip()

