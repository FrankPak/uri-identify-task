
class identify:
    def __init__(self,uri):
        self.uri = uri
        self.path = None

    
    def parse(self): #Paths: login, confirm, sign
        expectedScheme = "visma-identity"
        expectedPath= ("login", "confirm", "sign")


        uriParsed = self.uri
        #should check that it correctly parses or if it gives error
        GivenScheme = uriParsed.split("://") #GivenScheme is should look like visma-identity://login?source=severa -> ["visma-identity", "login?source=severa"]
        
        GivenPath = GivenScheme[1].split("?")


        if GivenScheme[0] != expectedScheme: #tests if the start of given uri is actually "visma-identity"
            exit

        if GivenPath[0].endswith(expectedPath) == False: #Tests that if expectedPath is "login", "confirm", or "sign"
            exit
        
        

        
        return print(GivenPath) #path and parameter as key valye pairs


p1 = identify("visma-identity://login?source=severa")

p1.parse()