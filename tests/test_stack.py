"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest
from src.stack import Node, Stack


def test_push():
    # Создаем объект класса Stack
    stack = Stack()

    # Добавляем элементы на вершину стека
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')

    # Проверяем, что вершина стека содержит последний добавленный элемент
    assert stack.top.data == 'data3'

    # Проверяем, что следующий элемент в стеке содержит предыдущий добавленный элемент
    assert stack.top.next_node.data == 'data2'

    # Проверяем, что следующий элемент в стеке содержит еще предыдущий добавленный элемент
    assert stack.top.next_node.next_node.data == 'data1'
