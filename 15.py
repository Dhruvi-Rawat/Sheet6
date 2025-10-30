A = input("Enter main string: ")
B = input("Enter word to find: ")
pos = A.find(B)
print(pos if pos != -1 else -1)
