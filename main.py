#Made By Oliver W. 5-10-22
#More info can be found at
#Github.com/AviateProjects
#Entrance Nodes
def Start():
    i=0
    Items=("Play Now","Info","Quit")
    print("")
    print("Welcome to Flight Transport for Python terminal")
    while i<len(Items):
        print(str(i)+": "+Items[i])
        i=i+1
    s=int(input("Select: "))

    if s==0:
        selectStartPort()
    elif s==1:
        info()
    else:
        quit()
def info():
    print("")
    print("Welcome to Flight Transport for Python terminal")
    print("This game is in a Demo phase")
    print("This game is in a sandbox mode")
    print("more features are coming soon")
    print("Update can be found at AviateProjects On github")
    print("Made by Oliver W.")
    print("Version 1.0b")
    Start()
def selectStartPort():
    i=0
    Items=("Atlanta","London","Tokyo","Sydney","Quit") 
    print("") 
    print("Starting Airports:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Select: "))

    if s==0:                        
        portATL()
    elif s==1:                     
        portLHR()
    elif s==2:                     
        portHND()
    elif s==3:                     
        portSYD()
    else:                          
       quit()
#Airport nodes
def portADD():
    i=0
    Items=("Mumbai","Cairo","Cape Town","Lagos","Tunisia","Quit") 
    print("") 
    print("You are at Addis Adiba:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))

    if s==0:                        
        portBOM()
    elif s==1:                     
        portCAI()
    elif s==2:                     
        portCPT()
    elif s==3:                     
        portLOS()
    elif s==4:                     
        portTUN()
    else:                          
        quit()
def portATL():
    i=0
    Items=("New York","Los Angles","Mexico City","Quit") 
    print("") 
    print("You are at Atlanta:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portJFK()
    elif s==1:                     
        portLAX()
    elif s==2:                     
        portMEX()
    else:                          
        quit()
def portBGW():
    i=0
    Items=("Mumbai","Cairo","Delhi","Istanbul","Moscow","Quit") 
    print("") 
    print("You are at Bahgdad:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portBOM()
    elif s==1:                     
        portCAI()
    elif s==2:                     
        portDEL()
    elif s==3:                     
        portIST()
    elif s==4:                     
        portSVO()
    else:                          
        quit()
def portBOG():
    i=0
    Items=("Rio De Jenero","New York","Lima","Mexico City","Quit") 
    print("") 
    print("You are at Bogota:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portGIG()
    elif s==1:                     
        portJFK()
    elif s==2:                     
        portLIM()
    elif s==3:                     
        portMEX()
    else:                          
        quit()
def portBOM():
    i=0
    Items=("Addis Adaba","Baghdad","Cape Town","Delhi","Hong Kong","Sydney","Quit") 
    print("") 
    print("You are at Mumbai:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portADD()
    elif s==1:                     
        portBGW()
    elif s==2:                     
        portCPT()
    elif s==3:                     
        portDEL()
    elif s==4:                     
        portHKG()
    elif s==5:                     
        portSYD()
    else:                          
        quit()
def portCAI():
    i=0
    Items=("Addis Adaba","Baghdad","Istanbul","Lagos","Tunisia","Quit") 
    print("") 
    print("You are at Cairo:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portADD()
    elif s==1:                     
        portBGW()
    elif s==2:                     
        portIST()
    elif s==3:                     
        portLOS()
    elif s==4:                     
        portTUN()
    else:                          
        quit()
def portCPT():
    i=0
    Items=("Addis Addiba","Mumbai","Rio De Jenero","Lagos","Sydney","Quit") 
    print("") 
    print("You are at CapeTown:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portADD()
    elif s==1:                     
        portBOM()
    elif s==2:                     
        portGIG()
    elif s==3:                     
        portLOS()
    elif s==4:                     
        portSYD()
    else:                          
        quit()
def portDEL():
    i=0
    Items=("Baghdad","Mumbai","Hong Kong","Quit") 
    print("") 
    print("You are at New Delhi:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))

    if s==0:                        
        portBGW()
    elif s==1:                     
        portBOM()
    elif s==2:                     
        portHKG()
    else:                          
        quit()
def portGIG():
    i=0
    Items=("Bogota","Cape Town","Lima","Lagos","Quit") 
    print("") 
    print("You are at Rio De Jenero:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portGIG()
    elif s==1:                     
        portCPT()
    elif s==2:                     
        portLIM()
    elif s==3:                     
        portLOS()
    else:                          
        quit()
def portHKG():
    i=0
    Items=("Mumbai","Delhi","Tokyo","Honolulu","Bejing","Sydney","Quit") 
    print("") 
    print("You are at Hong Kong:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portBOM()
    elif s==1:                     
        portDEL()
    elif s==2:                     
        portHND()
    elif s==3:                     
        portHNL()
    elif s==4:                     
        portPEK()
    elif s==5:                     
        portSYD()
    else:                          
        quit()
def portHND():
    i=0
    Items=("Hong Kong","Honalulu","Bejing","Sydney","Quit") 
    print("") 
    print("You are at Tokyo:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portHKG()
    elif s==1:                     
        portHNL()
    elif s==2:                     
        portPEK()
    elif s==3:                     
        portSYD()
    else:                          
        quit()
def portHNL():
    i=0
    Items=("Hong Kong","Tokyo","Los Angeles","Lima","Mexico City","Sydney","Quit") 
    print("") 
    print("You are at Hong Kong:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portHKG()
    elif s==1:                     
        portHND()
    elif s==2:                     
        portLAX()
    elif s==3:                     
        portLIM()
    elif s==4:                     
        portMEX()
    elif s==5:                     
        portSYD()
    else:                          
        quit()
def portIST():
    i=0
    Items=("Baghdad","Cairo","London","Moscow","Tunisia","Quit") 
    print("") 
    print("You are at Istanbul:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))

    if s==0:                        
        portBGW()
    elif s==1:                     
        portCAI()
    elif s==2:                     
        portLHR()
    elif s==3:                     
        portSVO()
    elif s==4:                     
        portTUN()
    else:                          
        quit()
def portJFK():
    i=0
    Items=("Atlanta","Bogota","London","Lagos","Quit") 
    print("") 
    print("You are at New York:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portATL()
    elif s==1:                     
        portBOG()
    elif s==2:                     
        portLHR()
    elif s==3:                     
        portLOS()
    else:                          
        quit()
def portLAX():
    i=0
    Items=("Atlanta","Honolulu","Mexico City","Quit") 
    print("") 
    print("You are at Los Angeles:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portATL()
    elif s==1:                     
        portHNL()
    elif s==2:                     
        portMEX()
    else:                          
        quit()
def portLHR():
    i=0
    Items=("Istanbul","New York","Moscow","Tunisia","Quit") 
    print("") 
    print("You are at London:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portIST()
    elif s==1:                     
        portJFK()
    elif s==2:                     
        portSVO()
    elif s==3:                     
        portTUN()
    else:                          
        quit()
def portLIM():
    i=0
    Items=("Bogota","Rio De Jenero","Honalulu","Quit") 
    print("") 
    print("You are at Lima:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portBOG()
    elif s==1:                     
        portGIG()
    elif s==2:                     
        portHNL()
    else:                          
        quit()
def portLOS():
    i=0
    Items=("Addis Addiba","Cairo","Cape Town","Rio De Jenero","New York","Quit") 
    print("") 
    print("You are at Lagos:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))

    if s==0:                        
        portADD()
    elif s==1:                     
        portCAI()
    elif s==2:                     
        portCPT()
    elif s==3:                     
        portGIG()
    elif s==4:                     
        portJFK()
    else:                          
        quit()
def portMEX():
    i=0
    Items=("Atlanta","Bogota","Honalulu","Los Angles","Quit") 
    print("") 
    print("You are at Mexico City:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portATL()
    elif s==1:                     
        portBOG()
    elif s==2:                     
        portHNL()
    elif s==3:                     
        portLAX()
    else:                          
        quit()
def portPEK():
    i=0
    Items=("Hong Kong","Honalulu","Moscow","Quit") 
    print("") 
    print("You are at Bejing:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portHKG()
    elif s==1:                     
        portHNL()
    elif s==2:                     
        portSVO()
    else:                          
        quit()   
def portSVO():
    i=0
    Items=("Bahgdad","Istanbul","London","Bejing","Quit") 
    print("") 
    print("You are at Moscow:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portBGW()
    elif s==1:                     
        portIST()
    elif s==2:                     
        portLHR()
    elif s==3:                     
        portPEK()
    else:                          
        quit()
def portSYD():
    i=0
    Items=("Mumbai","Cape Town","Hong Kong","Honnalulu","Quit") 
    print("") 
    print("You are at Sydney:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portBOM()
    elif s==1:                     
        portCPT()
    elif s==2:                     
        portHKG()
    elif s==3:                     
        portHNL()
    else:                          
        quit()
def portTUN():
    i=0
    Items=("Addis Addiba","Cairo","Istanbul","London","Quit") 
    print("") 
    print("You are at Tunisia:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))
    if s==0:                        
        portADD()
    elif s==1:                     
        portCAI()
    elif s==2:                     
        portIST()
    elif s==3:                     
        portLHR()
    else:                          
        quit()
    
Start()