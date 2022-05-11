#def selectNodeDemo():               how the node structure works
#    i=0                             i=0    
#    Items=("0","1","quit")          List the menu items
#    while i<len(Items):             loops number of items
#        print(str(i)+": "+Items[i]) Prints The string
#        i=i+1                       Ends loop
#    s=int(input("Select: "))#       User input as a integer

#    if s==0:                        If statement(possablility 1)
#        selectNode2()
#    elif s==1:                      elif statement(p2)
#        selectNode3()
#    else:                           quit statement(universal)(final Possability)
#        quit()
        

def selectStart():
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
    print("Version 0.1b")
    selectStart()

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
    else:                          
        quit()
        
def portATL():
    i=0
    Items=("London","Sydney","Quit") 
    print("") 
    print("You are at Atlanta:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))

    if s==0:                        
        portLHR()
    elif s==1:                     
        portSYD()
    else:                          
        quit()

def portLHR():
    i=0
    Items=("Atlanta","Sydney","Quit") 
    print("") 
    print("You are at London:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))

    if s==0:                        
        portATL()
    elif s==1:                     
        portSYD()
    else:                          
        quit()
    
def portSYD():
    i=0
    Items=("Atlanta","London","Quit") 
    print("") 
    print("You are at Sydney:")
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Fly to: "))

    if s==0:                        
        portATL()
    elif s==1:                     
        portLHR()
    else:                          
        quit()

selectStart()