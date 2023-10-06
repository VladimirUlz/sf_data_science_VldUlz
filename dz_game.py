import random

def binary_search(number: int) -> int:
    """Бинарный поиск для угадывания числа"""
    count = 0
    low = 1
    high = 100
    while True:
        count += 1
        predict_number = (low + high) // 2
        if number == predict_number:
            return count
        elif number > predict_number:
            low = predict_number + 1
        else:
            high = predict_number - 1

def score_game(binary_search) -> int:
    """За какое количество попыток в среднем угадывается число"""
    count_ls = []
    random_array = [random.randint(1, 100) for _ in range(1000)]
    for number in random_array:
        count_ls.append(binary_search(number))
    score = int(sum(count_ls) / len(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score

if __name__ == "__main__":
    score_game(binary_search)
