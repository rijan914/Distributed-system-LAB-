import Pyro4

@Pyro4.expose

class Calculator(object):
    def add(self,x,y):
        return x+y
    def subtract(self,x,y):
        return x-y
    
#create Pyro4.daemon
daemon=Pyro4.Daemon()
uri=daemon.register(Calculator)

#print the URL 
print("Server URL:",uri)
#start the server
print("calculator server started . press ctrl+c to exit.")
try:
    daemon.requestLoop()
except KeyboardInterrupt:
    print("existing calculator server.")
    daemon.shutdown()
