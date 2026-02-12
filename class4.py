#Storing Values
'''
tree1 = 98
tree2 = 94
tree3 = 41
tree4 = 95
tree5 = 11

#Finding the total of trees

sum = tree1 + tree2 + tree3 + tree4 + tree5
print("The sum of all the 5 trees is: " , sum )


#Finding the average of trees
average = sum/5
print("The average of aall the trees is :" , average)


'''


#Take Marks as input obtained in 4 subjects

print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english:"))
science = int(input("science :"))
hindi = int(input("hindi :"))


#Lets calculate the percentage of marks
sum = math+english+science+hindi

print("Sum of math,english,science,hindi ")


perc = (sum/400)*100

print(end="Percentage Mark = ")

print(perc)