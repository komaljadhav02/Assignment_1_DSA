#1 Write a program to find all pairs of an integer array whose sum is equal to a given number?
arr=[]
lenth= int(input("Enter no of items : "))
for i in range(lenth):
    num=int(input(f"Enter {i+1} element : "))
    arr.append(num)
num= int (input("Enter sum of pair : "))
def pairs(arr,num):
    pair=set()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            # print(arr[i],arr[j],num)
            if arr[i]+arr[j]==num:
                pa=(min(arr[i],arr[j]),max(arr[i],arr[j]))
                pair.add(pa)
    if not pair:
        print ("No Pairs found!",end=" ")
    else:
        return pair
print(pairs(arr,num))
"""
-----Expected Output-----
Enter no of items : 5
Enter 1 element : 2
Enter 2 element : 3
Enter 3 element : 4
Enter 4 element : 6
Enter 5 element : 4
Enter sum of pair : 8
{(4, 4), (2, 6)}
"""

# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def reverse(arr):
    left, right = 0, len(arr) - 1  # Initialize two pointers

    while left < right:
        # Swap the elements at the left and right pointers
        arr[left], arr[right] = arr[right], arr[left]

        # Move the pointers towards each other
        left += 1
        right -= 1
    return arr
arr=[]
lenth= int(input("Enter no of items : "))
for i in range(lenth):
    num=int(input(f"Enter {i+1} number : "))
    arr.append(num)
print(reverse(arr))
"""
-----Expected Output-----
Enter no of items : 5
Enter 1 number : 2
Enter 2 number : 3
Enter 3 number : 4
Enter 4 number : 5
Enter 5 number : 6
[6, 5, 4, 3, 2]
"""

# Q3. Write a program to check if two strings are a rotation of each other?
string1=input("Enter string 1 : ")
string2=input("Enter string 2 : ")
def  rotatestring(str1,str2):
    if len(str1)!=len(str2):
        return False
    temp=str1+str2
    if str1 in temp:
        return True
    else:
        return False
    
if rotatestring(string1,string2):
    print("Yes!")
else:
    print("No!")

"""
-----Expected Output-----
Enter string 1 : Komal
Enter string 2 : lamoK
Yes!
"""

# Q4. Write a program to print the first non-repeated character from a string?

string=input("Enter string : ")
def repeat(string)->str:
    temp={}
    for i in string:
        temp[i]=1+temp.get(i,0)
    for i in string:
        if temp[i]==1:
            return i
print('Non-repeated character : ',repeat(string))
"""
-----Expected Output-----
Enter string : komaljadhav
Non-repeated character :  k
"""

# Q5. Write a recursive function to check if a given string is a palindrome.

string= input("Enter string : ")
def palindrome(string):
    if len(string)==1:
        return True
    if string[0]==string[-1]:
        return palindrome(string[1:-1])
    else:
        return False
print(palindrome(string))
"""
-----Expected Output-----
Enter string : kayak
True
"""

# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
      
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  
        else:
            return None
    
    def get_stack(self):
        if not self.is_empty():
            return self.items
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def clearAll(self):
        self.items.clear()
        print("All Elements removed.")

string = input("Enter the postfix : ")
 
def postfix(string):
    res=''
    if len(string)<=1:
        return string
    else:
        stack=Stack()
        for strs in string:
            if strs in ["+",'-','*','/']:
                s1=stack.peek()
                stack.pop()
                s2=stack.peek()
                
                stack.pop()
                try:
                    res=strs+s2+s1+res
                except:
                    print ('Enter the valid postfix : ')
            else:
                stack.push(strs)
    return res
print('Prefix : ',postfix(string))
"""
-----Expected Output-----
Enter the postfix : 23-12+
Prefix :  +12-23
"""

# Q7. Write a program to convert prefix expression to infix expression.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
      
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  
        else:
            return None
    
    
    
    def is_empty(self):
        return len(self.items) == 0

string = input("Enter the postfix : ")
 
def postfix(string):
    string=string[::-1]
    res=''
    if len(string)<=1 or string==None:
        return string
    else:
        stack=Stack()
        for strs in string:
            if strs in ["+",'-','*','/']:
                str = "(" + stack.pop() + f"{strs}" + stack.pop() + ")"
                stack.push(str)
            else:
                stack.push(strs)
    while not stack.is_empty():
        res+=stack.pop()
        
    return res 
print('Infix : ',postfix(string))
"""
-----Expected Output-----
Enter the postfix : *-2/12*/312
Infix :  ((2-(1/2))*((3/1)*2))
"""

# Q8. Write a program to check if all the brackets are closed in a given code snippet.

def closed(string):
    temp={'(':0,')':0}
    for c in string:
        if c == "(" :
            temp['(']+=1
        if c==")":
            temp[')']+=1

        
    return temp['(']%2==0 and temp[')']%2==0

string = input('Enter the string : ')
print(closed(string))
"""
-----Expected Output-----
Enter the string : ((()))
False
"""

# Q9. Write a program to reverse a stack.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
      
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  
        else:
            return None
    
    def get_stack(self):
        if not self.is_empty():
            return self.items
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def clearAll(self):
        self.items.clear()
        print("All Elements removed.")

stack=Stack()
newstack=Stack()
lenth=int(input('Enter no of items to Push : '))
for i in range(lenth):
    num=int(input(f"Enter {i+1} number to append : "))
    stack.push(num)
print ('Original  Stack : ',stack.get_stack())
for i in range(lenth):
    stc=stack.get_stack()
    newstack.push(stc[lenth-(i+1)])
print ('New Stack : ',newstack.get_stack())
"""
-----Expected Output-----
Enter no of items to Push : 5
Enter 1 number to append : 10
Enter 2 number to append : 20
Enter 3 number to append : 40
Enter 4 number to append : 50
Enter 5 number to append : 70
Original  Stack :  [10, 20, 40, 50, 70]
New Stack :  [70, 50, 40, 20, 10]
"""

# Q10. Write a program to find the smallest number using a stack.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
      
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  
        else:
            return None
    
    def get_stack(self):
        if not self.is_empty():
            return self.items
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def clearAll(self):
        self.items.clear()
        print("All Elements removed.")

stack=Stack()
lenth=int(input('Enter no of items to Push : '))
for i in range(lenth):
    num=int(input(f"Enter {i+1} number to append : "))
    stack.push(num)
print ('Original  Stack : ',stack.get_stack())
print('Smallest number : ',min(stack.get_stack()))
"""
-----Expected Output-----
Enter no of items to Push : 4
Enter 1 number to append : 20
Enter 2 number to append : 30
Enter 3 number to append : 40
Enter 4 number to append : 50
Original  Stack :  [20, 30, 40, 50]
Smallest number :  20
"""