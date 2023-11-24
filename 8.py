import tkinter as tk
from tkinter import messagebox
from random import randint
import itertools
import copy

class ArrayVariants: 
    def __init__(self, n): 
        self.n = n
        self.array = [0] * n

    def generate_array(self): # метод для генерации случайных величин для массива
        for i in range(self.n):
            self.array[i] = randint(-10, 10)

    def get_best_variant(self, max_sum): # метод для нахождения варианта, удовлетворяющего ограничению
        if max_sum < sum(x for x in self.array if x < 0):
            raise ValueError("Максимальная сумма не может быть меньше суммы положительных элементов")
        
        variants = []
        indices = [i for i in range(1, len(self.array), 2) if self.array[i] > 0]
        
        for i in range(len(indices) + 1):
            for combination in itertools.combinations(indices, i):
                variant = copy.deepcopy(self.array)
                for index in combination:
                    variant[index] = 0
                print(f"Полученный вариант: {variant}, сумма элементов: {sum(variant)}")  # выводим каждый вариант перед проверкой
                if sum(variant) <= max_sum:
                    variants.append(variant)
        
        best_variant = max(variants[::-1], key = sum)
        return best_variant

def generate_and_get_best_variant():
    try:
        n = int(entry_n.get())
        max_sum = int(entry_max_sum.get())

        array_variants = ArrayVariants(n)
        array_variants.generate_array()

        best_variant = array_variants.get_best_variant(max_sum)

        result_window = tk.Toplevel(root)
        result_label = tk.Label(result_window, text=f"Результат: {best_variant}")
        result_label.pack()
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

# создание основного окна
root = tk.Tk()
root.title("Программа для расчета вариантов массива c учетом ограничения")

# создание полей ввода
label_n = tk.Label(root, text = "Количество элементов массива (n):")
label_n.pack()
entry_n = tk.Entry(root)
entry_n.pack()

label_max_sum = tk.Label(root, text = "Максимальная сумма (max_sum):")
label_max_sum.pack()
entry_max_sum = tk.Entry(root)
entry_max_sum.pack()

# создание кнопки генерации лучшего варианта
button_generate = tk.Button(root, text = "Сгенерировать и получить лучший вариант", command = generate_and_get_best_variant)
button_generate.pack()

# запуск цикла обработки событий
root.mainloop()
