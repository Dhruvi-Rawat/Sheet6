n=int(input(" enter a string"))
# p=input("enter another string")
for i in range(n):
    m=input(f"string{i+1}:")
    vowels=0
    consonants=0
    m=m.lower()

    for ch in m:
        if ch.isalpha():
            if ch in 'aeiou':
                vowels+=1
            else:
                consonants+=1
    print( "vowels","consonants")

# n = int(input("Enter number of strings: "))

# for i in range(n):
#     m = input(f"Enter string {i+1}: ")
#     vowels = 0
#     consonants = 0
#     m = m.lower()

#     for ch in m:
#         if ch.isalpha():
#             if ch in 'aeiou':
#                 vowels += 1
#             else:
#                 consonants += 1

#     print(f"Vowels = {vowels}, Consonants = {consonants}")


