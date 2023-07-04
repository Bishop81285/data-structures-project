"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Stack


class StackTest(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)

        self.assertEqual(stack.top.data, 30)
        self.assertEqual(stack.top.next_node.data, 20)
        self.assertEqual(stack.top.next_node.next_node.data, 10)
        self.assertIsNone(stack.top.next_node.next_node.next_node)

    def test_pop(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)

        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.is_empty())

    def test_is_empty(self):
        stack = Stack()

        self.assertTrue(stack.is_empty())

        stack.push(10)

        self.assertFalse(stack.is_empty())


if __name__ == '__main__':
    unittest.main()
