import random 

'''
This function is used to reorganise the stack within an array
curr_stack --> number of stack within the array that is to be re-organised
'''
def reorganise(curr_stack):
    if(bottom_indices[curr_stack] == None): #current stack doesn't exists, so no re-organistation needed
        pass
    else: #stack exists so shift stack
        #creating new top and bottom for current stack
        len_below_stack = 0
        top_below_stack = 0
        bottom_below_stack = 0

        #calculating lengths of current stack and below stack to maintain gap propotionally
        for i in bottom_indices[curr_stack+1:]:
            if i is None:
                pass
            else:
                bottom_below_stack = bottom_indices[curr_stack+1]
                top_below_stack = top_indices[curr_stack]
        if(bottom_below_stack is None):  #no stack below current stack exists
            len_below_stack = 0
        else:
            len_below_stack = bottom_below_stack - top_below_stack
        len_curr_stack = bottom_indices[curr_stack] - top_indices[curr_stack-1]
        gap = abs(top_below_stack - bottom_indices[curr_stack])

        #print("below",len_below_stack)
        #print("curr",len_curr_stack)
        #print("gap",gap)   

        #if no stack below current stack exists, maintain some-offset
        part = gap//(len_below_stack+len_curr_stack)
        below_part = part*len_below_stack
        if(below_part==0):
            below_part = 2
        #print("below_part",below_part)

        #if stack below current stack exists, create new bottom
        index_end = -1
        for i in top_indices[curr_stack:]:
            if(i is not None):
                index_end = i-1-below_part
                break
        #print("new bottom:",index_end)

        #if no stack below current stack exists, then choose random location from free spots
        if(index_end == -1):
            index_start = bottom_indices[curr_stack-1]+2+len_curr_stack
            index_end = len(arr)-1
            index_end = random.randint(index_start,index_end)
        print("new bottom:",index_end)

        stack_start = bottom_indices[curr_stack]
        stack_stop = top_indices[curr_stack-1]
        bottom_indices[curr_stack] = index_end
        top_indices[curr_stack-1] = index_end

        #since new bottom is decided, move all stack elements using push() operation
        for i in range(stack_start,stack_stop,-1):
            push(curr_stack,arr[i])
            arr[i] = None

    
'''
This function is used to push element into a stack
stacknum --> number of stack within array into which element should be pushed
value --> value that is to be pushed into stack
'''
def push(stacknum,value):
    #check if stack is full
    check = isFull(stacknum)
    if(check):  #current stack is fill
        print("Stack full. Reorganising stacks...")
        #check if main array is filled and extend array
        fill = arr.count(None)
        l = len(arr)
        if(fill >= l/3):
            arr.extend([None]*10)
        
        #re-organising all stacks in iterative manner
        for i in range(max_stacks,stacknum-1,-1):
            print("Reorganising stack",i)
            reorganise(i)
            print("Stack ",i,"is reorganised\n")
            print("Array:",arr)
            print("Top indexes:",top_indices)
            print("Bottom indexes:",bottom_indices)
            if(i==stacknum):
                push(stacknum,value)

    else: # current stack isn't full, element can be inserted
        if(bottom_indices[stacknum] == None): #first entry into main stack
            index_start = bottom_indices[stacknum-1]+1
            index_end = -1
            if(top_indices[stacknum+1] == None):  #stack below current stack doesn't exist
                index_end = len(arr)-1
            else:
                index_end = top_indices[stacknum+1]-1
            #print(index_start,index_end)
            try:
                new_bottom = random.randint(index_start,index_end)
                bottom_indices[stacknum] = new_bottom
                top_indices[stacknum-1] = new_bottom
                arr[top_indices[stacknum-1]] = value
                top_indices[stacknum-1] = top_indices[stacknum-1]-1
                print("New Stack Created")
                print("Element pushed onto stack")
            except ValueError:
                #if element exists at last location, no more stacks can be allocated
                print("No more stacks can be allocated")

        else: #stack already exists
            arr[top_indices[stacknum-1]] = value
            top_indices[stacknum-1] = top_indices[stacknum-1]-1
            print("Element pushed onto stack")

'''
This function is used to pop topmost element from the stack
stacknum --> number of stack within array from which element should be popped
'''
def pop(stacknum):
    if(bottom_indices[stacknum] == None): #stack doesn't exist
        print("Stack doesn't exist")
    else: 
        #check if empty, so that underflow doesn't occur
        check = isEmpty(stacknum)
        if(check):
            print("Stack is empty")
        else:
            arr[top_indices[stacknum-1]+1] = None
            top_indices[stacknum-1] = top_indices[stacknum-1] + 1 

'''
This function is used to print topmost element from the stack
stacknum --> number of stack within array from which topmost element will be printed
'''
def peek(stacknum):
    if(bottom_indices[stacknum] == None): #stack doesn't exist
        print("Stack doesn't exist")
    else:
        #check if empty, so that underflow doesn't occur
        check = isEmpty(stacknum)
        if(check):
            print("Stack is empty")
        else:
            return(arr[top_indices[stacknum-1]+1])

'''
This function is used to check if stack is empty
stacknum --> number of stack within array which should be checked
'''
def isEmpty(stacknum):
    if(top_indices[stacknum-1] == bottom_indices[stacknum]):
        return(True)
    else:
        return(False)

'''
This function is used to check if stack is full
stacknum --> number of stack within array which should be checked
'''
def isFull(stacknum):
    if(top_indices[stacknum-1] == bottom_indices[stacknum-1]):
        return(True)
    else:
        return(False)

'''
arr --> maintains all stack elements within it in array format, initially every element is set to None
top_indices --> maintains indexes of top of all stacks, initially every element is set to None
bottom_indices --> maintains indexes of bottom of all stacks, initially every element
is set to None, except the 1st one which always points to top of the array
max_stacks --> maintains maximum stacks allocated within the array

#Usage of max_stacks
Makes re-organisation of stacks easier. We'll just use this integer and 
iterate backwards to organise each stack
'''
arr = [None]*10
top_indices = [None]*10
bottom_indices = [0]+[None]*10
max_stacks = 0

#Loop within which all stack operations can be performed
while(True):
    option = input("\n1. Push onto stack \n2. Pop from stack \n3. Peek stack \n4. Exit\nEnter Option: ")

    #push operation
    if(option=="1"):
        stacknum = int(input("\nPush element onto which stack: "))
        value = int(input("Enter value: "))
        if(stacknum == 0):  #stack naming starts from 1
            print("Stack number cannot be zero")
        else:
            if(stacknum>max_stacks):  #condition to maintain maximum stack number in array
                max_stacks = stacknum
            push(stacknum,value)
            print("Array:",arr)
            print("Top indexes:",top_indices)
            print("Bottom indexes:",bottom_indices)

    #pop operation
    elif(option=="2"):
        stacknum = int(input("\nPop element from which stack: "))
        pop(stacknum)
        print("Array:",arr)
        print("Top indexes:",top_indices)
        print("Bottom indexes:",bottom_indices)

    #Peek operation
    elif(option=="3"):
        stacknum = int(input("\nPrint element from which stack: "))
        value = peek(stacknum)
        if(value is None):  #spaces between stacks
            pass
        else:
            print("The top value of stack",stacknum,"is:",value)

    #exit the iteration
    else:
        exit()

