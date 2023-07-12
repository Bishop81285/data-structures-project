"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest

from src.queue import Queue


class QueueTest(unittest.TestCase):
    def test_empty_queue(self):
        queue = Queue()

        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)
        self.assertTrue(queue.is_empty())

        queue.enqueue(1)

        self.assertFalse(queue.is_empty())

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(queue.head.data, 1)
        self.assertEqual(queue.tail.data, 3)
        self.assertEqual(queue.head.next_node.data, 2)
        self.assertEqual(queue.tail.next_node, None)
        self.assertFalse(queue.is_empty())

    def test_str(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        self.assertEqual(str(queue), '10\n20\n30')
