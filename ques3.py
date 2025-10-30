# str="PyThoN"
# str1=str.lower()
# print(str1)

# str="PyThoN"
# str1=str.isalnum()
# print(str1)


## Input number of test cases
T = int(input())

for i in range(T):
    S = input().strip()  
    if S == S[::-1]:
        print(1)
    else:
        print(0)
