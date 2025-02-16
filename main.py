import store as s

shop1 = s.Store('Главрыба', 'Мытищи', {'Лещ': 200, 'Вобла': 450, 'Хек': 200, 'Осётр': 1300})
shop2 = s.Store('Магнит', 'Торецк', {'Курица': 100, 'Говядина': 300, 'Свинина': 200})
shop3 = s.Store('Дымок', 'Челябинск')

shop3.add_item('Друг', 120)
shop3.add_item('Спорт', 60)
shop3.add_item('Танзания', 6000)
print(shop3.get_all_products())
shop3.new_price('Танзания', 5000)
print(shop3.get_all_products())
shop3.remove_item('Танзания')
print(shop3.get_all_products())
shop3.remove_item('Танзания')
print(shop1.get_all_products())

print(shop1.get_product_price('Лещ'))
shop1.add_item('Минтай', 120)
shop1.add_item('Икра Минтая', 190)
shop2.new_price('Говядина', 400)
print(shop2.get_all_products())