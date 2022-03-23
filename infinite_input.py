x = []
while(True):
    a=input()
    if(str(a) == "exit"):
        break
    else:
        try:
            a=int(a)
            x.append(a)
        except ValueError:
            print("Inavlid input") 
x.sort()
print(*x,sep=" ")