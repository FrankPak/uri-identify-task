
class identify:
    def __init__(self,uri):
        self.uri = uri
        self.path = None
        self.parameter = {}

    
    def parse(self): #Paths: login, confirm, sign
        expectedScheme = "visma-identity"
        expectedPath= ("login", "confirm", "sign")
        expectedPayment = "paymentnumber"
        expectedDocumentStr = "documentid"
        expectedSource = "source"


        uriParsed = self.uri
        #should check that it correctly parses or if it gives error
        GivenScheme = uriParsed.split("://") # GivenScheme is should look like visma-identity://login?source=severa -> ["visma-identity", "login?source=severa"]
        
        GivenPath = GivenScheme[1].split("?") # GivenPath goes from "login?source=severa" to ["login", "source=severa"]

        if GivenScheme[0] != expectedScheme: #tests if the start of given uri is actually "visma-identity"
            exit

        if GivenPath[0].endswith(expectedPath) == False: #Tests that if expectedPath is either "login", "confirm", or "sign"
            exit

        self.path = GivenPath[0] #Is this truly in the right spot?

        GivenSource = GivenPath[1].split("=") # "source=severa" -> ["source", "severa"] or "source=netvisor&paymentnumber=102226" -> ["source", "netvisor&paymentnumber", "102226"]
        
        if GivenSource[0] != expectedSource: #check if it is source
            exit



        if GivenPath[0] == "login":

            key = GivenSource[0]

            self.parameter[key] = GivenSource[1]

        elif GivenPath[0] == "confirm": #expects string and int

            ParameterConfirm = GivenSource[1].split("&") # "netvisor&paymentnumber" -> ["netvisor", "paymentnumber"]

            if ParameterConfirm[1] != expectedPayment:
                exit

            key = GivenSource[0]

            self.parameter[key] = ParameterConfirm[0]

            key = ParameterConfirm[1]

            paymentnumber = int(GivenSource[2]) #Check that it actually turn to int

            self.parameter[key] = paymentnumber #this expects to have a second, whaty if it dosent


        
        elif GivenPath[0] == "sign": 
            ParameterSign = GivenSource[1].split("&")  # "vismasign&documentid" -> ["vismasign", "documentid"]

            key = GivenSource[0]

            self.parameter[key] = ParameterSign[0]

            if ParameterSign[1] != expectedDocumentStr:
                exit

            key = ParameterSign[1]

            self.parameter[key] = key = GivenSource[2]
            #expects string id

        
        return print() #path and parameter as key valye pairs


p1 = identify("visma-identity://confirm?source=netvisor&paymentnumber=102226")

p1.parse() # remember to add try catch