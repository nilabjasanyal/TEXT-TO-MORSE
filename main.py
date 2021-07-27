from code import code
string = input("INPUT THE STRING TO BE CONVERTED: ")

converted_code = []
new_string=""
for word in string:
    for letter in word:
        c_w = code[letter]
        converted_code+=[c_w]
    new_string+="".join(converted_code)
    

print(" ".join(converted_code))

