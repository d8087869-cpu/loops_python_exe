'''
fruits = ['apple', 'banana', 'cherry']
for items in fruits:
    print(items)
#2    
for i in range(1,6):
    print(i)
#3 
for i in range(0, 10, 2):
    print(i)'''
#4
'''
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f'{index}: {fruit}')
#5
scores = {'Alpha': 80, 'Bravo': 95}
for name , score in scores.items():
    print(f'{name} , {score}')
'''    
#6
'''
numbers = [1, 2, 3, 4, 5]
total = 0 
for i in numbers:
    total+=i
    print(total)'''
#7 
'''
i = 1
while i<= 5: 
    print(i)
    i+=1
'''
'''
for i in range(1,6):
    print(i)'''

#8
'''
matrix = [[1, 2, 3], [4, 5, 6]]
for row in matrix:
    for cell in row:
        print(cell)
'''       
#9 
squares = [n**2 for n in range(1, 11)]
print(squares)

#10
evens = [n for n in range(1, 21) if n % 2 == 0]
print(evens)

#part 2 
#1 
names = ['Alpha', 'Bravo']
scores = [80, 95]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

#2 
pairs = [(n, n**2) for n in range(1, 6)]
print(pairs)

#3 
names = ['david', 'ethan', 'gabi']
for index, names in enumerate(names, start=1):
    print(f'{index}: {names}')