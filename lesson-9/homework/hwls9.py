import math
from datetime import datetime

# 1. Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


# 2. Person Class
class Person:
    def __init__(self, name, country, dob):  # dob in 'YYYY-MM-DD'
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, '%Y-%m-%d')

    def age(self):
        today = datetime.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))


# 3. Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


# 4. Shape and Subclasses
class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError


class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return 4 * self.side


# 5. Binary Search Tree
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if not node:
                return BSTNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(node, value):
            if not node:
                return False
            if node.value == value:
                return True
            elif value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)


# 6. Stack Data Structure
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            raise IndexError("Pop from empty stack.")
        return self.stack.pop()


# 7. Linked List Data Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if not temp:
            return
        if prev:
            prev.next = temp.next
        else:
            self.head = temp.next

    def display(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result


# 8. Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}

    def remove_item(self, name, quantity=1):
        if name in self.items:
            self.items[name]['quantity'] -= quantity
            if self.items[name]['quantity'] <= 0:
                del self.items[name]

    def total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.items.values())


# 9. Stack with Display
class DisplayStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            raise IndexError("Pop from empty stack.")
        return self.stack.pop()

    def display(self):
        return self.stack[::-1]


# 10. Queue Data Structure
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.queue:
            raise IndexError("Dequeue from empty queue.")
        return self.queue.pop(0)


# 11. Bank Class
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner, initial_deposit=0):
        if owner in self.accounts:
            raise ValueError("Account already exists.")
        self.accounts[owner] = Account(owner, initial_deposit)

    def deposit(self, owner, amount):
        if owner in self.accounts:
            self.accounts[owner].deposit(amount)

    def withdraw(self, owner, amount):
        if owner in self.accounts:
            self.accounts[owner].withdraw(amount)

    def get_balance(self, owner):
        if owner in self.accounts:
            return self.accounts[owner].balance
