import hashlib

input = 'bgvyzdsv'

for i in range(9999999):
    # Combine numner and input together in string
    number = str(i)
    fullInput = input + number
    
    # Calculate MD5 hash
    result = (hashlib.md5(fullInput.encode('utf-8')).hexdigest())
    # print(result)

    # identify first result that begins with 5 zeros
    # change to 0:6 and '000000' to obtain Part 2 answer
    if result[0:5] == '00000':
        print(result)
        print(number)
        break



