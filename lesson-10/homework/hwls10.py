import datetime

# =======================
# Homework 1: ToDo List Application
# =======================

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.title} | {self.description} | Due: {self.due_date} | Status: {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return True
        return False

    def list_all_tasks(self):
        return [str(task) for task in self.tasks]

    def list_incomplete_tasks(self):
        return [str(task) for task in self.tasks if not task.completed]


def todo_cli():
    todo = ToDoList()
    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due date (YYYY-MM-DD): ")
            todo.add_task(Task(title, desc, due))
        elif choice == "2":
            title = input("Task title to mark as complete: ")
            if todo.complete_task(title):
                print("Marked as complete.")
            else:
                print("Task not found.")
        elif choice == "3":
            for t in todo.list_all_tasks():
                print(t)
        elif choice == "4":
            for t in todo.list_incomplete_tasks():
                print(t)
        elif choice == "0":
            break


# =======================
# Homework 2: Simple Blog System
# =======================

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"{self.title} by {self.author} on {self.date.strftime('%Y-%m-%d %H:%M')}\n{self.content}"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        return [str(post) for post in self.posts]

    def posts_by_author(self, author):
        return [str(post) for post in self.posts if post.author == author]

    def delete_post(self, title):
        self.posts = [post for post in self.posts if post.title != title]

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                return True
        return False

    def latest_posts(self, count=5):
        sorted_posts = sorted(self.posts, key=lambda x: x.date, reverse=True)
        return [str(post) for post in sorted_posts[:count]]


def blog_cli():
    blog = Blog()
    while True:
        print("\n--- Blog Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Show Latest Posts")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))
        elif choice == "2":
            for post in blog.list_posts():
                print(post, "\n")
        elif choice == "3":
            author = input("Author: ")
            for post in blog.posts_by_author(author):
                print(post, "\n")
        elif choice == "4":
            title = input("Post title to delete: ")
            blog.delete_post(title)
        elif choice == "5":
            title = input("Post title to edit: ")
            content = input("New content: ")
            if blog.edit_post(title, content):
                print("Post updated.")
            else:
                print("Post not found.")
        elif choice == "6":
            for post in blog.latest_posts():
                print(post, "\n")
        elif choice == "0":
            break


# =======================
# Homework 3: Simple Banking System
# =======================

class Account:
    def __init__(self, number, holder, balance=0):
        self.number = number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def transfer(self, target_account, amount):
        self.withdraw(amount)
        target_account.deposit(amount)

    def __str__(self):
        return f"Account {self.number} | {self.holder} | Balance: ${self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc):
        self.accounts[acc.number] = acc

    def get_account(self, number):
        return self.accounts.get(number)

    def check_balance(self, number):
        acc = self.get_account(number)
        return acc.balance if acc else None


def bank_cli():
    bank = Bank()
    while True:
        print("\n--- Bank Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Display Account Details")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            number = input("Account number: ")
            name = input("Holder name: ")
            balance = float(input("Initial deposit: "))
            bank.add_account(Account(number, name, balance))
        elif choice == "2":
            number = input("Account number: ")
            acc = bank.get_account(number)
            print(f"Balance: ${acc.balance:.2f}" if acc else "Account not found.")
        elif choice == "3":
            number = input("Account number: ")
            amount = float(input("Deposit amount: "))
            acc = bank.get_account(number)
            if acc:
                acc.deposit(amount)
                print("Deposit successful.")
            else:
                print("Account not found.")
        elif choice == "4":
            number = input("Account number: ")
            amount = float(input("Withdraw amount: "))
            acc = bank.get_account(number)
            if acc:
                try:
                    acc.withdraw(amount)
                    print("Withdrawal successful.")
                except ValueError as e:
                    print(e)
            else:
                print("Account not found.")
        elif choice == "5":
            src = input("From account: ")
            dst = input("To account: ")
            amount = float(input("Amount: "))
            src_acc = bank.get_account(src)
            dst_acc = bank.get_account(dst)
            if src_acc and dst_acc:
                try:
                    src_acc.transfer(dst_acc, amount)
                    print("Transfer successful.")
                except ValueError as e:
                    print(e)
            else:
                print("Invalid accounts.")
        elif choice == "6":
            number = input("Account number: ")
            acc = bank.get_account(number)
            print(acc if acc else "Account not found.")
        elif choice == "0":
            break


# Uncomment to run individual CLIs:
# todo_cli()
# blog_cli()
# bank_cli()
