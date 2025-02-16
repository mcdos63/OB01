import tkinter as tk

# Декоратор для ввода данных через tkinter
def input_decorator(func):
    def wrapper(self, *args, **kwargs):
        # Проверяем, переданы ли оба позиционных аргумента (product и price)
        if len(args) == 2:
            # Если оба аргумента переданы, вызываем оригинальную функцию с этими аргументами
            return func(self, *args, **kwargs)

        # Если хотя бы один из аргументов не передан, открываем графический интерфейс
        def submit():
            product = entry_product.get()
            price = entry_price.get()
            root.quit()  # Закрываем окно после получения данных
            # Преобразуем цену в число, если это возможно
            try:
                price = float(price)
            except ValueError:
                price = None  # Если введена невалидная цена, оставляем None

            # Вызываем оригинальную функцию с полученными значениями
            func(self, product, price)

        # Создаем окно tkinter
        root = tk.Tk()
        root.title("Ввод товара")

        # Название магазина
        label_store = tk.Label(root, text=f"Магазин: {self.name}", font=("Arial", 14))
        label_store.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Метки и поля ввода для товара и цены с предустановленными значениями
        default_product = "Товар по умолчанию"
        default_price = "100.00"

        label_product = tk.Label(root, text="Введите название товара:", anchor='w')
        label_product.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        entry_product = tk.Entry(root)
        entry_product.grid(row=1, column=1, padx=10, pady=5)
        entry_product.insert(0, default_product)

        label_price = tk.Label(root, text="Введите цену товара:", anchor='w')
        label_price.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        entry_price = tk.Entry(root)
        entry_price.grid(row=2, column=1, padx=10, pady=5)
        entry_price.insert(0, default_price)

        # Кнопка для отправки данных
        submit_button = tk.Button(root, text="Отправить", command=submit)
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Запуск цикла обработки событий
        root.mainloop()

    return wrapper
