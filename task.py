import time

class Task():
    _instances = []

    def __init__(self, name, date = None, status = False):
        self.name = name
        self.date = date if date is not None else time.strftime("%Y-%m-%d", time.localtime())
        self.status = status
        self.__class__._instances.append(self)  # Сохраняем экземпляр в списке класса

    @classmethod
    def get_instances(cls, status = False):
        return [i for i in cls._instances if i.status == status]

    def status_change(self):
        self.status = not self.status

    def delete(self):
        if self in self.__class__._instances:
            self.__class__._instances.remove(self)
        del self  # Теперь можно безопасно удалять объект

    def __del__(self):
        # Удаляем объект из списка экземпляров, если он в нем есть
        if self in self.__class__._instances:
            self.__class__._instances.remove(self)

    def __repr__(self):
        return f"Task('{self.name}', '{self.date}', {self.status})"


t1 = Task("task1")
t2 = Task("task2", '2025-01-01')
t3 = Task("task3", '2025-02-01', False)

print(t1.date, t1.status)
t1.status_change()

print(t2.date, t2.status)
t1.status_change()

t2.delete()  # Удаляем t2

# Печатаем все экземпляры с status = False
for i in Task.get_instances(False):
    print(i.name, i.date, i.status)

# Попытка доступа к удаленному t2 вызывает ошибку
try:
    print('--------delete---------', t2.name, t2.date, t2.status)
except NameError as e:
    print(f"Ошибка: {e}")

# Печатаем снова все экземпляры с status = False
for i in Task.get_instances(False):
    print(i.name, i.date, i.status)