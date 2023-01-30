import sys
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
        
        GivenPath = GivenScheme[1].split("?") # GivenScheme goes from "login?source=severa" to GivenPath as ["login", "source=severa"]

        if GivenPath[0].endswith(expectedPath) == False: #Tests that if GivenPath[0] is either "login", "confirm", or "sign"
            raise Exception( "'"+ GivenPath[0] + "' IS NOT CORRECT A PATH, EXPECTED 'login', 'confirm', OR 'sign', PLEASE FIX IT.")

        self.path = GivenPath[0] 

        GivenSource = GivenPath[1].split("=") # GivenPath[1] is split "source=severa" -> ["source", "severa"] or "source=netvisor&paymentnumber=102226" -> ["source", "netvisor&paymentnumber", "102226"]
        
        if GivenSource[0] != expectedSource: #checks if Source is written correctly
            raise Exception("'" + GivenSource[0] + "' IS NOT CORRECT WRITTEN SOURCE, EXPECTED" + expectedSource +" PLEASE FIX IT.")
        



        if GivenPath[0] == "login":
            list_length = len(GivenSource)

            #Checks that if the end number string is missing or there are too many strings at the end
            if list_length < 2: 
                raise Exception( "THERE ARE TOO LITTLE PARAMETERS, PLEASE CHECK THE URI")
            elif list_length > 2:
                raise Exception( "THERE ARE TOO MANY PARAMETERS, PLEASE CHECK THE URI.")

            key = GivenSource[0] #Just 'source' key
            SourceCompany = GivenSource[1]
            try:
                self.parameter[key] = SourceCompany
            except UnboundLocalError:
                print("SOMETHING WENT CRITICALLY WRONG AT END, PLEASE CHECK THAT THE END OF URI IS CORRECT")
                sys.exit()




        elif GivenPath[0] == "confirm": 
            list_length = len(GivenSource)
            #Checks that if the end number string is missing or there are too many strings at the end
            if list_length < 3: 
                raise Exception( "THERE ARE TOO LITTLE PARAMETERS, PLEASE CHECK THE URI.")
            elif list_length > 3:
                raise Exception( "THERE ARE TOO MANY PARAMETERS, PLEASE CHECK THE URI.")
                


            ParameterConfirm = GivenSource[1].split("&") #Parses "netvisor&paymentnumber" -> ["netvisor", "paymentnumber"]

            if ParameterConfirm[1] != expectedPayment:
                raise Exception( "'"+ ParameterConfirm[1] + "' IS NOT CORRECT, EXPECTED '"+ expectedPayment + "', PLEASE FIX IT.")


            key = GivenSource[0] #Just 'source' key

            SourceCompany = ParameterConfirm[0]

            self.parameter[key] = SourceCompany

            key = ParameterConfirm[1] #Just 'paymentnumber'

            try:
                paymentnumber = int(GivenSource[2]) #Check that it actually turn to int
            except ValueError:
                print("YOUR '" + GivenSource[2] + "' PARAMETER VALUE IS NOT CORRECT, IT SHOULD PRODUCE INT, PLEASE FIX IT")
                sys.exit()

            try:
                self.parameter[key] = paymentnumber #this expects to have a second, whaty if it dosent
            except UnboundLocalError:
                print("SOMETHING WENT CRITICALLY WRONG AT END, '"+ paymentnumber + "', PLEASE CHECK THAT THE END OF URI IS CORRECT")
                sys.exit()
            


        
        elif GivenPath[0] == "sign": 
            ParameterSign = GivenSource[1].split("&")  # "vismasign&documentid" -> ["vismasign", "documentid"]

            list_length = len(GivenSource)

            if list_length < 2 or list_length > 2:
                raise Exception( "'"+ ParameterConfirm[1] + "' IS NOT CORRECT, EXPECTED '"+ expectedPayment + "', PLEASE FIX IT.")

            key = GivenSource[0]

            self.parameter[key] = ParameterSign[0]

            if ParameterSign[1] != expectedDocumentStr:
                raise Exception( "'"+ ParameterSign[1] + "' IS NOT CORRECT, EXPECTED '"+ expectedDocumentStr + "', PLEASE FIX IT.")

            key = ParameterSign[1]
            
            try:
                self.parameter[key] = GivenSource[2]
            except UnboundLocalError:
                print("SOMETHING WENT CRITICALLY WRONG AT END,  '"+ GivenSource[2] + "', PLEASE CHECK THAT THE END OF URI IS CORRECT")
                sys.exit()


    
class TestClass():
    def __init__(self,uri):
        self.id = identify(uri)
    
    def get_path(self):
        return self.id.path

    def get_parameter(self):
        return self.id.parameter.values()
     

p1 = TestClass("visma-identity://confirm?source=netvisor&paymentnumber=102020")


print("Path: " + p1.get_path())
print("Parameters: ", end="")
print(p1.get_parameter())