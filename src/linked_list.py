class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        """Конструктор класса LinkedList"""
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)

        if self.is_empty():
            self.head = self.tail = new_node
            self.tail.next_node = None
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)

        if self.is_empty():
            self.head = self.tail = new_node
            self.tail.next_node = None
        else:
            new_node.next_node = None
            self.tail.next_node = new_node
            self.tail = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head

        if node is None:
            return str(None)

        ll_string = ''

        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string

    def is_empty(self):
        """
        Метод проверяющий пустоту списка

        :return: True если список пуст, False в противном случае
        """
        return self.head is None

    def to_list(self) -> list:
        """
        Метод, который возвращает список с данными, содержащимися в односвязном списке LinkedList

        :return: список с данными из узлов списка
        """
        data_list = []

        node = self.head

        while node:
            data_list.append(node.data)

            node = node.next_node

        return data_list

    def get_data_by_id(self, _id):
        """
        Метод, который возвращает первый найденный в LinkedList словарь с ключом 'id',
        значение которого равно переданному в метод значению.

        :param _id: значение ключа 'id', которое ищем в словарях узлов списка
        :return: словарь с соответствующим значением ключа 'id' или None, если такого нет
        """

        node = self.head

        while node:
            try:
                if not isinstance(node.data, dict):
                    raise TypeError
                elif 'id' not in node.data:
                    raise TypeError
                elif node.data['id'] == _id:
                    return node.data
            except TypeError:
                print(f"Данные ({node.data}) не являются словарем или в словаре нет id.")
            finally:
                node = node.next_node

        return None
