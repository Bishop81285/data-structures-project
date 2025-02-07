class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        tmp = self.top
        print_list = []

        while tmp:
            print_list.append(str(tmp.data))
            tmp = tmp.next_node

        return "\n".join(print_list)

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data, self.top)
        self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.is_empty():
            raise Exception("Stack is empty!")
        data = self.top.data
        self.top = self.top.next_node
        return data

    def is_empty(self):
        """
        Метод проверяющий пустоту стека

        :return: True если стек пустой, False в противном случае
        """
        return self.top is None
