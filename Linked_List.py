class Node:
    __slots__ = 'user_name', 'user_mail', '_next'

    def __init__(self, user_name, user_mail, _next):
        self.user_name = user_name
        self.user_mail = user_mail
        self._next = _next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def create(self, name, mail):
        new_user = Node(name, mail, None)
        if self.is_empty():
            self.head = new_user
            self.tail = self.head
        else:
            self.tail._next = new_user
        self.tail = new_user
        self.size += 1

    def display(self):
        if self.is_empty():
            print('The list is empty\n')
        else:
            p = self.head
            while p is not None:
                print('User:', p.user_name)
                print('Mail:', p.user_mail, '\n')
                p = p._next

    def search_user(self, searching_user):
        p = self.head
        while p is not None:
            if p.user_name == searching_user:
                print('User', '"' + searching_user + '"', 'is found!')
                print('User:', p.user_name)
                print('Mail:', p.user_mail, '\n')
                return True
            else:
                p = p._next
        print('User is not found\n')
        return False

    def add_to_beginning(self, name, mail):
        user_first = Node(name, mail, None)
        if self.is_empty():
            self.head = user_first
            self.tail = user_first
        else:
            user_first._next = self.head
            self.head = user_first
        self.size += 1

    def add_user_to_random_place(self, add_name, add_mail, position):
        if position < 1:
            print('The list contains', self.size, 'elements')
            print("You can't insert in non existing position!\n")
            return False
        try:
            add_user = Node(add_name, add_mail, position)
            p = self.head
            i = 1
            while i < position - 1:
                p = p._next
                i += 1
            add_user._next = p._next
            p._next = add_user
            self.size += 1
        except AttributeError:
            print('The list contains', self.size, 'elements')
            print("You can't insert in non existing position!\n")

    def remove_user(self, removing_mail):
        if self.is_empty():
            print('The list is empty\n')
            return False
        p = self.head
        while p is not None:
            if p.user_mail == removing_mail:
                break
            temp = p
            p = p._next
        if p is None:
            print('User with the mail', removing_mail, 'is not found in the list\n')
            return False
        elif p == self.head:
            print('Deleting user', p.user_name, 'with the mail', p.user_mail)
            self.head = p._next
            self.size -= 1
            return True
        print('Deleting user', p.user_name, 'with the mail', p.user_mail)
        temp._next = p._next
        self.size -= 1
        return True


user = LinkedList()

user.create('Nick', 'nikita_tyupin@mail.ru')
user.create('Any', 'anynice@mail.ru')
user.create('David', 'david_d@mail.ru')
user.create('Zak', 'zakefron@mail.ru')
user.create('Bob', 'bob_dilan@mail.ru')
user.create('Yoo', 'yooyaK@mail.ru')
user.create('Valentine', 'valaya_q@mail.ru')
user.create('Lolly', 'lolly_=pop@mail.ru')
user.create('Frank', 'frankyy_poz@mail.ru')
user.create('Isaak', 'isaak_klark@mail.ru')
# user.display()

print(len(user))

user.remove_user('valaya_q@mail.ru')
user.remove_user('isaak_klark@mail.ru')
user.remove_user('nikita_tyupin@mail.ru')

user.display()
print(len(user))
