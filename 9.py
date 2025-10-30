s = input("Enter string: ")
words = s.split()
rev_words = [w[::-1] for w in words]
print(' '.join(rev_words))
