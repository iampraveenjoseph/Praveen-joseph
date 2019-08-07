a = 'hello world 123'
numbers = sum(c.isdigit() for c in a)
words   = sum(c.isalpha() for c in a)
print("LETTER ",words)
print("DIGIT ",numbers)
