data = ['дфыр4', 'wppe3', 'fadf', '6', 'fd24']

#print(''.join(list(filter(lambda char: char.isdigit(), data))))

number = 1
print(any(str(number) in s for s in data))