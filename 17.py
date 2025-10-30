A = input("Enter string: ")
A = A + A                 
A = ''.join(ch for ch in A if ch.islower())  
result = ''              
for ch in A:
    if ch in 'aeiou':
        result += '#'
    else:
        result += ch
print(result)
