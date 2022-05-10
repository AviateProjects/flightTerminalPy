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
    Items=("Play Now","Quit")
    while i<len(Items):
        print(str(i)+": "+Items[i])
        i=i+1
    s=int(input("Select: "))

    if s==0:
        selectStartPort()
    else:
        quit()

def selectStartPort():
    i=0                              
    print("Starting Airports:")
    Items=("Atlanta","London","Tokyo","Moscow","Quit")          
    while i<len(Items):            
        print(str(i)+": "+Items[i]) 
        i=i+1                       
    s=int(input("Select: "))

    if s==0:                        
        selectPortATL()
#    elif s==1:                     
#        selectNode3()
    else:                          
        quit()
        
def selectPortATL():
    i=input("hello world")

print("Welcome to Flight Transport Game for Python terminal")
selectStart()