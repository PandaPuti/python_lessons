squares = ['red', 'blue', 'green', 'yellow' 'pink']
for square in squares:
    print(square)

squares = ['red','orange','blue','green','yellow','pink','orange']
for i in range(0,len(squares)):
    squares[i] = squares[i] + ' color'
squares

for i, square in enumerate(squares):
    print(f'{i} : {square}')


orangeSquares = []
for square in squares:
    if square == 'orange':
        orangeSquares.append(square)
orangeSquares

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])  

for i in range(0, 8):
    print(i)

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")

for num in range(1, 10):
    if num == 5:
        print("Breaking the loop at:", num)
        break
    print(num)

for num in range(1, 6):
    if num == 3:
        continue
    print(num)

count = 0
while count < 10:
    count += 1
    if count == 3:
        continue  # skip printing 3
    if count == 8:
        break     # stop the loop when count is 8
    print(count)
