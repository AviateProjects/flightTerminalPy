#Made By Oliver W. 5-12-22
#More info can be found at
#Github.com/AviateProjects
# VERSION 1.2.1 using nodeMap 1.2.1 template

#selecting functions
def select2(a,b,s):
    #this function is for start()
    if s==0:
        a()
    elif s==1:
        b()
    else:
        quit()
def select3(a,b,c,s):
    if s==0:
        a()
    elif s==1:
        b()
    elif s==2:
        c()
    else:
        quit()
def select4(a,b,c,d,s):
    if s==0:
        a()
    elif s==1:
        b()
    elif s==2:
        c()
    elif s==3:
        d()
    else:
        quit()
def select5(a,b,c,d,e,s):
    if s==0:
        a()
    elif s==1:
        b()
    elif s==2:
        c()
    elif s==3:
        d()
    elif s==4:
        e()
    else:
        quit()
def select6(a,b,c,d,e,f,s):
    if s==0:
        a()
    elif s==1:
        b()
    elif s==2:
        c()
    elif s==3:
        d()
    elif s==4:
        e()
    elif s==5:
        f()
    else:
        quit()
def lister(Items):
    i=0
    while i<len(Items):
        print(str(i)+": "+Items[i])
        i=i+1

#Entrance Nodes
def start():
    Items=("Play Now","Info","Quit")
    print("")
    print("Welcome to Flight Transport for Python terminal")
    lister(Items)
    s=int(input("Select: "))
    select2(selectStartPort,info,s)
def info():
    print("")
    print("Welcome to Flight Transport for Python terminal")
    print("This game is in a Demo phase")
    print("This game is in a sandbox mode")
    print("more features are coming soon")
    print("Update can be found at AviateProjects On github")
    print("Made by Oliver W.")
    print("Version 1.2.1")
    start()
def selectStartPort():
    Items=("Atlanta","London","Tokyo","Sydney","Quit")
    print("")
    print("Starting Airports:")
    lister(Items)
    s=int(input("Select: "))
    select4(portATL,portLHR,portHND,portSYD,s)

#Airport nodes
def portADD():
    Items=("Mumbai","Cairo","Cape Town","Lagos","Tunisia","Quit")
    print("")
    print("You are at Addis Adiba:")
    lister(Items)
    s=int(input("Fly to: "))
    select5(portBOM,portCAI,portCPT,portLOS,portTUN,s)
def portATL():
    Items=("New York","Los Angeles","Mexico City","Quit")
    print("")
    print("You are at Atlanta:")
    lister(Items)
    s=int(input("Fly to: "))
    select3(portJFK,portLAX,portMEX,s)
def portBGW():
    Items=("Mumbai","Cairo","Delhi","Istanbul","Moscow","Quit")
    print("") 
    print("You are at Bahgdad:")
    lister(Items)                    
    s=int(input("Fly to: "))
    select5(portBOM,portCAI,portDEL,portIST,portSVO,s)
def portBOG():
    Items=("Rio De Jenero","New York","Lima","Mexico City","Quit")
    print("") 
    print("You are at Bogota:")
    lister(Items)               
    s=int(input("Fly to: "))
    select4(portGIG,portJFK,portLIM,portMEX,s)
def portBOM():
    Items=("Addis Adaba","Baghdad","Cape Town","Delhi","Hong Kong","Sydney","Quit")
    print("") 
    print("You are at Mumbai:")
    lister(Items)                
    s=int(input("Fly to: "))
    select6(portADD,portBGW,portCPT,portDEL,portHKG,portSYD,s)
def portCAI():
    Items=("Addis Adaba","Baghdad","Istanbul","Lagos","Tunisia","Quit")
    print("") 
    print("You are at Cairo:")
    lister(Items)                 
    s=int(input("Fly to: "))
    select5(portADD,portBGW,portIST,portLOS,portTUN,s)
def portCPT():
    Items=("Addis Addiba","Mumbai","Rio De Jenero","Lagos","Sydney","Quit")
    print("") 
    print("You are at CapeTown:")
    lister(Items)                   
    s=int(input("Fly to: "))
    select5(portADD,portBOM,portGIG,portLOS,portSYD,s)
def portDEL():
    Items=("Baghdad","Mumbai","Hong Kong","Quit")
    print("") 
    print("You are at New Delhi:")
    lister(Items)     
    s=int(input("Fly to: "))
    select3(portBGW,portBOM,portHKG,s)
def portGIG():
    Items=("Bogota","Cape Town","Lima","Lagos","Quit")
    print("") 
    print("You are at Rio De Jenero:")
    lister(Items)               
    s=int(input("Fly to: "))
    select4(portBOG,portCPT,portLIM,portLOS,s)
def portHKG():
    Items=("Mumbai","Delhi","Tokyo","Honolulu","Bejing","Sydney","Quit")
    print("") 
    print("You are at Hong Kong:")
    lister(Items)                
    s=int(input("Fly to: "))
    select6(portBOM,portDEL,portHND,portHNL,portPEK,portSYD,s)
def portHND():
    Items=("Hong Kong","Honalulu","Bejing","Sydney","Quit") 
    print("") 
    print("You are at Tokyo:")
    lister(Items)                 
    s=int(input("Fly to: "))
    select4(portHKG,portHNL,portPEK,portSYD,s)
def portHNL():
    Items=("Hong Kong","Tokyo","Los Angeles","Lima","Mexico City","Sydney","Quit") 
    print("") 
    print("You are at Hong Kong:")
    lister(Items)                     
    s=int(input("Fly to: "))
    select6(portHKG,portHND,portLAX,portLIM,portMEX,portSYD,s)
def portIST():
    Items=("Baghdad","Cairo","London","Moscow","Tunisia","Quit") 
    print("") 
    print("You are at Istanbul:")
    lister(Items)                 
    s=int(input("Fly to: "))
    select5(portBGW,portCAI,portLHR,portSVO,portTUN,s)
def portJFK():
    Items=("Atlanta","Bogota","London","Lagos","Quit") 
    print("") 
    print("You are at New York:")
    lister(Items)           
    s=int(input("Fly to: "))
    select4(portATL,portBOG,portLHR,portLOS,s)
def portLAX():
    Items=("Atlanta","Honolulu","Mexico City","Quit") 
    print("") 
    print("You are at Los Angeles:")
    lister(Items)                
    s=int(input("Fly to: "))
    select3(portATL,portHNL,portMEX,s)
def portLHR():
    Items=("Istanbul","New York","Moscow","Tunisia","Quit") 
    print("") 
    print("You are at London:")
    lister(Items)                           
    s=int(input("Fly to: "))
    select4(portIST,portJFK,portSVO,portTUN,s)
def portLIM():
    Items=("Bogota","Rio De Jenero","Honalulu","Quit") 
    print("") 
    print("You are at Lima:")
    lister(Items)                    
    s=int(input("Fly to: "))
    select3(portBOG,portGIG,portHNL,s)
def portLOS():
    Items=("Addis Addiba","Cairo","Cape Town","Rio De Jenero","New York","Quit") 
    print("") 
    print("You are at Lagos:")
    lister(Items)                       
    s=int(input("Fly to: "))
    select5(portADD,portCAI,portCPT,portGIG,portJFK,s)
def portMEX():
    Items=("Atlanta","Bogota","Honalulu","Los Angles","Quit") 
    print("") 
    print("You are at Mexico City:")
    lister(Items)       
    s=int(input("Fly to: "))
    select4(portATL,portBOG,portHNL,portLAX,s)
def portPEK():
    Items=("Hong Kong","Honalulu","Moscow","Quit") 
    print("") 
    print("You are at Bejing:")
    lister(Items)           
    s=int(input("Fly to: "))
    select3(portHKG,portHNL,portSVO,s)
def portSVO():
    Items=("Bahgdad","Istanbul","London","Bejing","Quit") 
    print("") 
    print("You are at Moscow:")
    lister(Items)           
    s=int(input("Fly to: "))
    select4(portBGW,portIST,portLHR,portPEK,s)
def portSYD():
    Items=("Mumbai","Cape Town","Hong Kong","Honnalulu","Quit") 
    print("") 
    print("You are at Sydney:")
    lister(Items)            
    s=int(input("Fly to: "))
    select4(portBOM,portCPT,portHKG,portHNL,s)
def portTUN():
    Items=("Addis Addiba","Cairo","Istanbul","London","Quit") 
    print("") 
    print("You are at Tunisia:")
    lister(Items)        
    s=int(input("Fly to: "))
    select4(portADD,portCAI,portIST,portLAX,s)
    
start()
