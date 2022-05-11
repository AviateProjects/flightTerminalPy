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

def portBGW():
    i=input("hello A")
    portDEL()

def portBOM():
    i=input("hello B")
    portDEL()

def portHKG():
    i=input("hello C")
    portDEL()

def portLOS():
    i=input("hello D")
    portDEL()

def portSYD():
    i=input("hello E")
    portDEL()

def portSYDa():
    i=input("hello F")
    portDEL()

portDEL()