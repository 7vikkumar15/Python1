'''Tuple Operations
Outline:
Write a program to perform the following operations: 
1. Create a tuple with different datatypes 
2. Create another tuple of integers 
3. Create a new tuple by adding 9 to the previous tuple 
4. Count the occurrences of an element in the tuple
5. Perform slicing on the tuple'''


#Create a tuple with different data types

tuplex = ("tuple" ,  False , 3.4 , 4)
print(tuplex)

#Create a tuple

tuplex = (4,6,2,8,3,1)
print(tuplex)

#Tuples are immutable so no new elements can be added
#Use + to merge tuples

tuplex = tuplex + (9 , )
print(tuplex)

#Counts the number of occurences of item 50 from a tuple

tuple1 = (50 , 60 , 80 , 90 , 60 , 30 , 90 , 70 , 50, 60, 50, 80, 50, 50, 50)
print(tuple1.count(50))

#Slicing a tuple

tuplex = (9,8,6,4,2,5,1,5,0,6)
_slice = tuplex[3:5]
print(_slice)

_slice = tuplex[:6]
print(_slice)

'''Flip Flop
Outline:
Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. 
If it's a palindrome, then it is the same after being reversed.'''

def palind(r):
    e = len(r) - 1
    s = 0
    while(s<e):
        if(r[s] != r[e]):
            return False
        s+=1
        e-=1
    return True

r = (1,2,3,3,2,1)
if (palind(r)):
    print("The Tuple is a Flip - Flop")
else:
    print("The Tuple is not a Flip - Flop")

'''Weather Prediction
Outline:
Create a tuple named weather with these elements -
 (1, 0, 0, 0, 1, 1, 0). If the element is 1 then the
   value of rainy increases by 1 otherwise the
 value of sunny increases by 1.On the basis of the value of rainy and
   sunny, predict the weather.'''

weather = (1, 0, 0, 0, 1, 1, 0)
sunny = 0
rainy = 0
for i in range(0 , 7):
    if(weather[i]==0):
        rainy+=1
    else:
        sunny+=1

if (sunny > rainy):
    print("Good Weather")
else:
    print("Bad Weather")
