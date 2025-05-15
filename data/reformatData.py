import json


f1 = open("MathVSIncome_Cleaned.csv", "r")
lines = f1.readlines()

dictionary ={}

# Create the dictionary here
f1.close()

for line in lines:
    this_line = line.split(',')
    if(this_line[0] == "State"):
        print("I should continue")
        continue
    this_dict = {}
    for i in range(3):
        this_dict["Math_4"] = this_line[2]
        this_dict["Math_8"] = this_line[3]
        this_dict["Income"] = this_line[4][:-1]
    dictionary[this_line[1]] = this_dict


#Save the json object to a file
f2 = open("math_income.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()
