'''Lists
Outline:
Write a program to perform the following operations on a List: 1. Create an empty list 2. A list with elements 3. Use * operator 4. Reverse a list

empty_list = []
print()


numbers = [1,2,3,4,5]
print(numbers)


triples = [1,2,3]*3
print(triples)

aList = [100 , 200 , 300 , 400 , 500]
aList = aList[::-1]
print(aList , "\n")
'''
'''Word Matching
Outline:
Write a Python program to count the number of strings where the string length is two or more, and the first and last 
characters are the same from a given list of strings.

def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("List of words with first and last character same \n" , lst)
    return ctr

count = match_words(["abc" , "aba" , "rct" , "cab" , "ctrr" , "1221"])
'''

'''Play with Lists
Outline:
Write a Python program to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements. 
Also, find the largest and the smallest number in the list.'''


L = [4 , 5 , 1 , 2 , 9 , 7 , 10 , 8]
print("Orignal List : " , L)


count = 0

for i in L:
    count += i 


avg = count/len(L)

print("sum = " , count)
print("average = " , avg)

L.sort()

print("Smallest element is : " , L[0])

print("Largest element is : ",L[-1])