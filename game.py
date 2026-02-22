import numpy as np

high = 101
down = 1
number = np.random.randint(down, high)
count = 0
print(f'Загаданное число:{number}')
while True:
    numb = (high + down) // 2
    print(numb)
    if numb == number:
        print('Число было угадано')
        break
    if numb < number:
        down = numb
        
    if numb > number:
        high = numb
    count += 1
print(count)
        
    