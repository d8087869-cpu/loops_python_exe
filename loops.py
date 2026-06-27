#1
'''
i = 0
while i <= 5: 
    print(i)
    i+=1
#2
i = 10
while i>=0 :
    print(i)    
    i=i-1'''
#3
'''
total = 0 
while total< 10:
    total+=1
print(total)    
#4
items = [2, 4, 6, 8]
i=0
while i< len (items)-1:
    print(items[i])
    i+=1
    if items[i]>5:
        break
#5
i = 0 
while i <=10:
    if  i% 2 == 0: 
        print(i)
    i=i+1
'''    

#6  
'''  
agents = ['Alpha', 'Bravo', 'Charlie']
i = 0 
while  i < len(agents):
    print(agents[i])
    i+=1
'''
"""
scores = {'Alpha': 80, 'Bravo': 95, 'Charlie': 70}
i = 0
while i  < len (scores)-1:
    print(scores.i)
"""
#8
'''
i=1
while i*2<100:
    i=i*2
print(i)
'''
#9
'''
data = [3, 7, 2, -1, 5]
i=0
total = 0
while i < len(data):
    if data[i]==-1:
        break
    total=total+data[i]
    i=i+1
print(total)
'''
#10
'''
n = 10
i = 1
while i<=10:
    print(f'')
'''#לא הצלחתי לפתור 


#part 2 
#1 
'''items = ['a', 'x', 'b', 'x', 'x'] 
i=0 
while i < len (items):
    items.remove("x")
    i+=1
print(items)    
'''



#2 
'''matrix = [[1, 2], [3, 4], [5, 6]]
i= 0 
while i <len (matrix):
    y=0
    while y<len(matrix[i]):
        print(matrix[i][y])
        y+=1
    i+=1'''
#3 
'''number =[1,2,3,4,5,6]
i = len (number)-1
while i >=0:
    print(number[i])
    i-=1 '''
#4
'''
data = [10, 30, 55, 20, 80]
i=0 
while i < len(data):
    if data[i] >= 50 :
        print('index', i )
    i+=1
    '''
#5 
'''
secret = 42
guesses = [10, 30, 42]
i=0
while i < len(guesses):
    if guesses[i]==secret: 
        print(i+1)
    i+=1    '''
#self learn 
#matrix is a list in a list becous if you whould have only one loop there will be only one row one list with no columns .
#2 brake in a inner loop stops the currrent row 
#in a outer loop it stops all the proccess of the loop 
#3 in sserch task you use braek when you find what you were looking for . and dont need the loop keep working .
#4 continue skips the val you told him , but keeps on the loop 
#5 current row continus to the next row 
# and the row you jumpt ren=main the same .  
#1 
matrix = [
    [2, 4, 6],
    [3, 99, 5],
    [8, 1, 7]]

for row in matrix:
    for value in row:
        if value > 50:
            print("Danger value:", value)
            break


#2 
matrix = [
    [5, -1, 8],
    [3, 4, -1],
    [9, 2, 6]]

for row in matrix:
    for value in row:
        if value == -1:
            continue  
        print("Valid value:", value)


#3 
matrix = [
    [4, 7, 2],
    [9, 0, 3],
    [1, 8, 5]
]

found = False
for row in matrix:
    for value in row:
        if value == 0:
            print("Found zero")
            found = True
            break
    if found:
        break
