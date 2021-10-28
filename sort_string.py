#This function swaps the characters in given string based on indices i,j 
def swap(TAM,i,j):
    if(i>=j):
        return TAM
    return(TAM[0:i]+TAM[j]+TAM[i+1:j]+TAM[i]+TAM[j+1:])

#Fetch input from user
string=input()
length = len(string)

'''
start --> this variable stores the position to which "T" should be swapped
end --> this variable stores the position to which "M" should be swapped
pos --> this variable gives the current position until which the string has been parsed
'''
start = 0
#Since last character is #, we don't swap M to last position
end = length-2
pos = 0

#We stop parsing the string when 'end' variable and 'pos' variable meet
while(pos<end+1):
    #if character is T, we swap with 'start' position
    if(string[pos]=="T"):
        string = swap(string,start,pos)
        start = start+1
        if(pos==0):
            #This makes us avoid infinite loop where we keep on swapping first character with itself
            pos = pos+1
    #if character is A, we skip current position
    elif(string[pos] == "A"):
        pos = pos+1
    #if character is M, we swap with 'end' position
    elif(string[pos] == "M"):
        string = swap(string,pos,end)
        end = end-1

print(string)