'''
Overload Operators
Outline:
Write a program to overload the less than
(<) and equal to (==) operators. For example,
create objects - ob1 and ob2 with values 3 and
 4 to compare values, respectively. You can
 additionally create more 
objects to try different values.
class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self , other):
        if(self.a < other.a):
            return "ob1 is less then ob2"
        else:
            return "ob2 is less than ob1"
    def __eq__(self,other):
        if(self.a == other.a):
            return " Both are equal"
        else:
            return"Not Equal"
        
        
ob1 = A(2)
ob2 = A(3)

print("Passed Values :" ,ob1.a , ob2.a )
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print("Passed Values :" , ob3.a , ob4.a)
print(ob3 == ob4)

Flashcards
Outline:
Create a python program to create a flashcard using object-
oriented programming. A flashcard is a two-sided card with
 information on both sides that can assist memory. A question
 and an answer are usually printed on one side of a flashcard
 Follow these steps to complete the activity - 1. From the 
 user, take the input for a word and its definition. 2. To 
assign values for Word and Meaning, create a class called 
 flashcard and use the __init__() function. 3. We'll use
 the __str__() function to get a string with the term 
and its definition. 4. Save the strings that have been
 returned in a list. 5. 
To print all of the stored flashcards, use a while loop.



class flashcard:
    def __init__(self , word , meaning):
        self.word = word
        self.meaning = meaning
    def __str__ (self):
        return self.word +'('+self.meaning+')'

flash = []
print("Welcome to the flashcard application")

while (True):
    word = input("Enter the name you want to add to the flashcard : ")
    meaning = input("Enter the meaning of the word: ")

    flash.append(flashcard(word,meaning))
    option = int(input("Enter 0 , If you want to add another flashcard otherwise enter 1: "))


    if(option):
        break

print("\n Your flashcards")
for i in flash:
    print(">" , i)

Fruit Quiz
Outline:
Write a program to create a quiz related to multiple fruits using object-oriented 
programming in Python. Create a class that consists of - 1. a constructor with a 
dictionary of fruits and respective colours 2. a function to execute the quiz. 
Here, the fruit will be chosen at random from the 
dictionary. Then ask the user to enter the colour of that fruit. Evaluate the answer and display the result accordingly.


    '''

import random

class FruitQuiz:

    def __init__(self):
        self.fruits = {'apple':'red',
                       'orange':'orange',
                       'watermelon':'green',
                       'banana':'yellow'}
    def quiz(self):
        while(True):
            fruit , color = random.choice(list(self.fruits.items()))

            print("What is the color of {} ".format(fruit))
            user_answer = input()

            if(user_answer.lower()==color):
                print("Correct answer")
            else:
                print("Wrong Answer")

            option = int(input("Enter 0 to play again otherwise enter 1"))
            if (option):
                break

print("Welcome to the fruit Quiz")
fq = FruitQuiz()
fq.quiz()
