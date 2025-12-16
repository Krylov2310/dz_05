from random import randint
import os
import platform
import time

list_size = [10, 100, 1000]


def info():
    print('\033[33mДомашнее задание 5\n'
          '"Быстрая сортировка"\n'
          'Студент Крылов Эдуард Васильевич\n'
          'Дата: 16.12.2025г.\033[0m')


# Очистка консоли
def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')  # From Linux


# Переход по заданиям
def any_key():
    input('\n\033[33mНажмите "Enter" для продолжения...\033[0m')


# Отсчёт начала времени
def start_time():
    start_time_ = time.perf_counter()  # точное время в секундах
    return start_time_


# Отсчёт конца времени
def print_time(get_time):
    end_time_ = time.perf_counter()
    elapsed_time = end_time_ - get_time
    print(f'\033[31mВремя: {elapsed_time:.6f}\033[0m')


# Генератор списка
def list_generate(size_list):
    arr1 = []
    for i in range(size_list):
        arr1.append(randint(1, 1000))
    return arr1


# 01
def print_fibonacci():
    print('\033[34m\n001 функция для вычисления n-го числа Фибоначчи.\033[0m')
    t = start_time()
    num = 5
    print(f'Число Фибоначчи: {num} = {fibonacci(num)}')
    print_time(t)


def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


# 02
def print_max(arr):
    print(f'\033[34m\n002 Рекурсивная функция для нахождения максимального элемента в списке: '
          f'{len(arr)} элементов.\033[0m')
    print(f'Список поиска: {arr}')
    t = start_time()
    result = find_max(arr)
    print(f"Максимальный элемент: {result}")
    print_time(t)


def find_max(arr, start=0, end=None):
    # Инициализация end при первом вызове
    if end is None:
        end = len(arr) - 1
    # Базовый случай: один элемент
    if start == end:
        return arr[start]
    # Разделяем список на две половины
    mid = (start + end) // 2
    # Рекурсивно находим максимум в левой и правой половинах
    left_max = find_max(arr, start, mid)
    right_max = find_max(arr, mid + 1, end)
    # Возвращаем больший из двух максимумов
    return max(left_max, right_max)


# 03
def print_quicksort(numbers):
    print(f'\033[34m\n003 Функция для реализации быстрой сортировки (QuickSort) в списке из: {n} элементов.\033[0m')
    print("До сортировки:", numbers)
    # Сортируем
    t = start_time()
    quicksort(numbers)
    print("После сортировки:", numbers)
    print_time(t)


def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        # Шаг 1: находим индекс опорного элемента после разделения
        pivot_index = partition(arr, low, high)
        # Шаг 2: рекурсивно сортируем левую часть
        quicksort(arr, low, pivot_index - 1)
        # Шаг 3: рекурсивно сортируем правую часть
        quicksort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    # Опорный элемент — последний в текущем диапазоне
    pivot = arr[high]
    # i — индекс меньшего элемента (граница левой части)
    i = low - 1
    for j in range(low, high):
        # Если текущий элемент ≤ pivot, перемещаем его влево
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Обмен
    # Ставим pivot на правильное место
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# 04
def insertion_sort(arr):
    print(f'\033[34m\n004 Сравнение сортировки вставками списка из: {len(arr)} элементов.\033[0m')
    print("До сортировки:", arr)
    t = start_time()
    num = len(arr)
    # Начинаем со второго элемента (индекс 1)
    for i in range(1, num):
        key = arr[i]  # Текущий элемент для вставки
        j = i - 1  # Индекс предыдущего элемента в отсортированной части
        # Перемещаем элементы, большие key, на одну позицию вперёд
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Вставляем key на правильное место
        arr[j + 1] = key
    print("После сортировки:", arr)
    print_time(t)


# Пример использования
if __name__ in '__main__':
    clear_screen()
    info()
    print_fibonacci()  # 01
    any_key()
    for n in list_size:  # 02
        arr_list = list_generate(n)
        print_max(arr_list)
    any_key()
    for n in list_size:
        arr_list_1 = list_generate(n)
        arr_list_2 = arr_list_1.copy()
        print_quicksort(arr_list_1)  # 03
        insertion_sort(arr_list_2)  # 04
        any_key()

print('\n\033[33mДомашнее задание закончено.\033[0m')
