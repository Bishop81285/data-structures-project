"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest

from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_insert_beginning(self):
        ll = LinkedList()

        data1 = {"name": "John", "age": 30}
        data2 = {"name": "Alice", "age": 25}

        ll.insert_beginning(data1)
        self.assertEqual(str(ll), " {'name': 'John', 'age': 30} -> None")

        ll.insert_beginning(data2)
        self.assertEqual(str(ll), " {'name': 'Alice', 'age': 25} -> {'name': 'John', 'age': 30} -> None")

    def test_insert_at_end(self):
        ll = LinkedList()

        data1 = {"name": "John", "age": 30}
        data2 = {"name": "Alice", "age": 25}

        ll.insert_at_end(data1)
        self.assertEqual(str(ll), " {'name': 'John', 'age': 30} -> None")

        ll.insert_at_end(data2)
        self.assertEqual(str(ll), " {'name': 'John', 'age': 30} -> {'name': 'Alice', 'age': 25} -> None")

    def test_is_empty(self):
        ll = LinkedList()
        self.assertTrue(ll.is_empty())

        data = {"name": "John", "age": 30}

        ll.insert_beginning(data)
        self.assertFalse(ll.is_empty())
