import tkinput as tk
class Store:
    def __init__(self, name, address, items: dict = None):
        self.name = name
        self.address = address
        self.items = items if items is not None else {}

    @tk.input_decorator
    def add_item(self, product, price):
        """Добавление товара в магазин"""
        if price is not None:
            self.items[product] = price
            print(f"Товар '{product}' с ценой {price} добавлен в магазин!")
        else:
            print("Неверная цена товара.")

    def remove_item(self, product):
        'Удаление товара из магазина'
        if product in self.items:
            print(f"Товар '{product}' удален из магазина '{self.name}'")
            del self.items[product]

    def get_product_price(self, product):  #
        'Получение цены товара'
        print(f"Магазин '{self.name}': Цена товара '{product}'")
        return self.items.get(product, None)

    def get_all_products(self):  #
        'Вывод всех имеющихся в магазине продуктов'
        return self.items

    def new_price(self, product, new_price):  #
        'Изменение цены товара'
        if product in self.items:
            print(f"Магазин '{self.name}': Цена товара '{product}' изменена на '{new_price}'")
            self.items[product] = new_price

    def __del__(self):
        pass
