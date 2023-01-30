
class identify:
    def __init__(self,uri):
        self.uri = uri
        self.path = None
        self.parameter = {}
        self.parse()

    
    def parse(self): 
        expectedScheme = "visma-identity"
        expectedPath= ("login", "confirm", "sign")
        expectedPayment = "paymentnumber"
        expectedDocumentStr = "documentid"
        expectedSource = "source"


        uriParsed = self.uri
        if isinstance(uriParsed, int) == True:
            raise Exception("URI NEEDS TO BE STRING, NOT INT. PLEASE FIX IT.")


        GivenScheme = uriParsed.split("://") # GivenScheme is should parsing like visma-identity://login?source=severa -> ["visma-identity", "login?source=severa"]


        if GivenScheme[0] != expectedScheme: #tests if the start of given uri is actually "visma-identity"
            raise Exception("'"+ GivenScheme[0] + "' IS NOT CORRECT SCHEME, EXPECTED '"+ expectedScheme + "', PLEASE FIX IT.")
        
        GivenPath = GivenScheme[1].split("?") # GivenPath goes from "login?source=severa" to ["login", "source=severa"]

        if GivenPath[0].endswith(expectedPath) == False: #Tests that if GivenPath is either "login", "confirm", or "sign"
            raise Exception( "'"+ GivenPath[0] + "' IS NOT CORRECT A PATH, EXPECTED 'login', 'confirm', OR 'sign', PLEASE FIX IT.")

        self.path = GivenPath[0] 

        GivenSource = GivenPath[1].split("=") # "source=severa" -> ["source", "severa"] or "source=netvisor&paymentnumber=102226" -> ["source", "netvisor&paymentnumber", "102226"]
        
        if GivenSource[0] != expectedSource: #check if Source is written correctly
            raise Exception("'" + GivenSource[0] + "' IS NOT CORRECT WRITTEN SOURCE, EXPECTED" + expectedSource +" PLEASE FIX IT.")



        if GivenPath[0] == "login":

            key = GivenSource[0]

            self.parameter[key] = GivenSource[1]

        elif GivenPath[0] == "confirm": #expects string and int

            ParameterConfirm = GivenSource[1].split("&") # "netvisor&paymentnumber" -> ["netvisor", "paymentnumber"]

            if ParameterConfirm[1] != expectedPayment:
                raise Exception( "'"+ ParameterConfirm[1] + "' IS NOT CORRECT, EXPECTED '"+ expectedPayment + "', PLEASE FIX IT.")

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
                raise Exception( "'"+ ParameterSign[1] + "' IS NOT CORRECT, EXPECTED '"+ expectedDocumentStr + "', PLEASE FIX IT.")

            key = ParameterSign[1]

            self.parameter[key] = key = GivenSource[2]
            #expects string id

    
class TestClass():
    def __init__(self,uri):
        self.id = identify(uri)
    
    def get_path(self):
        return self.id.path

    def get_parameter(self):
        return self.id.parameter.values() #Correct with the values?
        
p1 = TestClass("visma-identity://sonfirm?source=netvisor&paymentnumber=102226")


print("Path: " + p1.get_path())
print("Parameters: ", end="")
print(p1.get_parameter())