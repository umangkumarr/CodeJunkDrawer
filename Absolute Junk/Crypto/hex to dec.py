from ast import literal_eval
test_string = '0x64d8c41'
print("The original string : " + str(test_string))
res = literal_eval(test_string)
print("The decimal number of hexadecimal string : " + str(res))

print(chr(res))
