import numpy as np

high = 101
down = 1

def serch_elemnts(number, down, high) -> int:
    """ Функция для поиска случайно заданного элемента.
        Поиск осуществляется с помощью алгоритма бинарного поиска.


    Args:
        number (int): случайно заданное число, которое нужно найти
        down (int): нижняя граница интервала в котором содержится число numder
        high (int): верхняя граница интервала в котором содержится число numder

    Returns:
        count (int) : число итераций алгоритма для нахождения number
    """
    count = 0

    while True:
        numb = (high + down) // 2
        if numb == number:
            break
        if numb < number:
            down = numb
        if numb > number:
            high = numb
        count += 1
    
    return count

def average_number(down, high) -> int:
    """_summary_

    Args:
        down (int): нижняя граница интервала в котором содержится число numder
        high (int): верхняя граница интервала в котором содержится число numder

    Returns:
        score (int): среднее число итераций на массиве в 10 000 случайных чисел
    """
    list_with_result = []
    
    random_array = np.random.randint(down, high, size=(10000))
    
    for number in random_array:
        list_with_result.append(serch_elemnts(number, down, high))
    
    score = int(np.mean(list_with_result))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    return score

if __name__ == '__main__':
    average_number(down, high)

        
    