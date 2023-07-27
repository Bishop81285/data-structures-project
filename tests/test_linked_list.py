"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest

import sys
from io import StringIO

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

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

        self.assertEqual(ll.to_list(), [{'id': 1, 'username': 'lazzy508509'}, 'idusername', [1, 2, 3],
                                             {'id': 2, 'username': 'mosh_s'}])

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

        self.assertEqual(ll.get_data_by_id(1), {'id': 1, 'username': 'lazzy508509'})
        self.assertEqual(ll.get_data_by_id(2), {'id': 2, 'username': 'mosh_s'})
        self.assertEqual(ll.get_data_by_id(3), None)
