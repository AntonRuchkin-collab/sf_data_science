import numpy as np

high = 101
down = 1

#def random_predict(high, down) -> int:
def random_number(high, down) -> int:
    """Функция для угадывания числа

    Args:
        high (int): верхняя граница интервала
        down (int): нижняя граница интервала

    Returns:
        int: число попыток
    """
    count = 0
    number = np.random.randint(down, high)

    while True:
        numb = (high + down) // 2
        if numb == number:
            print('Число было угадано')
            break
        if numb < number:
            down = numb
            
        if numb > number:
            high = numb
        count += 1
    print(f"Число попыток было:{count}")
    return (count)

if __name__ == '__main__':
    random_number(high, down)

        
    