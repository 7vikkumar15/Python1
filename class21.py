'''

student_data = {
    "id1" : {"Name" : "Sara" , "Class" : "V" , "Subject_intergration" : "English , maths , science"},

    "id2" : {"Name" : "Surya" , "Class" : "V" , "Subject_intergration" : "English , maths , science"},

    "id3" : {"Name" : "David" , "Class" : "V" , "Subject_intergration" : "English , maths , science"},

    "id1" : {"Name" : "Sara" , "Class" : "V" , "Subject_intergration" : "English , maths , science"},
}

result = {}
seen_keys = []

for student_id , details in student_data.items():
    unique_key = (details["Name"], details["Class"] , details["Subject_intergration"]) 

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details


for k , v in result.items():
    print(k , ":" , v)
    

test_dict = {'Codingal' : 2 , 'is': 2 ,'best ': 2 , 'for': 2 , 'coding': 1,  }


print("The Orignal Dictionary : "  + str(test_dict))

K = 2

res = 0 
for key in test_dict:
    if test_dict[key] == K :
        res = res +1

print("The Frequency is : " + str(res))
'''

country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}

print("Country Code for india - ")
print(country_code.get("India" , "Not Found"))

print("Country Code for japan - ")
print(country_code.get("japan" , "Not Found"))

