mainMenuItems=("Play","Quit")
def select(a):
    i=0
    while i<len(a):
        print(str(i)+": "+a[i])
        i=i+1
    s=int(input("Select: "))
    return s;
s = select(mainMenuItems)
if s==0:
    print("Hello World")
elif s==1:
    quit()