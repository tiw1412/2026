class Contact():
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def display_info(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        print(f'Телефон: {self.phone}')
        print(f'Email: {self.email}')

Ufa = Contact('Мухаммад', 'Шахедов', '89119111488', 'bashkortsuperduper@gmail.com')
Moscow = Contact('Мухаммад', 'Таджиков', '82280316752', 'cleancleaner@yandex.ru')
Little_Saint_James = Contact('Джеффри', 'Эпштейн', '19119111488', 'epsteinislandtoursonline@gmail.com')
# Ufa.display_info()
# Moscow.display_info()
# Little_Saint_James.display_info()

class Wallet():
    def __init__(self, owner, balance, currency):
        self.owner = owner
        self.balance = balance
        self.crn = currency
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print('Введена неккоректная сумма')
        else:
            self.balance -= amount

    def getbalance(self):
        print(self.balance)
    
    def transfer(self, othrwll, amount):
        self.withdraw(amount)
        othrwll.deposit(amount)

Hess = Wallet('Herr. Hess', 99999999999999999999, 'Reichmarks')
Shalomit = Wallet('Shalomit', 500, 'Shekel')
# Hess.getbalance()
# Shalomit.getbalance()
# Hess.transfer(Shalomit, 1000)
# Hess.getbalance()
# Shalomit.getbalance()

class Product():
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.qnt = quantity
        self.ctg = category
    
    def gettv(self):
        print(self.price * self.qnt)
        return (self.price * self.qnt) 
    
    def appldicnt(self, percent):
        self.price -= self.price / 100 * percent
        print(f'Скидка в размере {percent} применена')
    
    def sell(self, amount):
        if amount > self.qnt:
            print('Недостаточное количество проуктов')
        else:
            self.qnt -= amount
    
class Store():
    def __init__(self):
        self.list = []
    
    def add_product(self, product):
        self.list.append(product)
    
    def del_product(self, product):
        self.list.remove(product)

    def find_product(self, product):
        htdt = 0
        while self.list[htdt] != product:
            htdt += 1
        print(self.list[htdt].name)

    def getabsolute(self):
        ttl = 0
        for i in self.list:
            ttl += i.gettv()
    
    def get_products_by_category(self, categ):
        slc = ''
        for i in self.list:
            if i.ctg == categ:
                slc += str(i.name) + ' '
        print(slc)

Hren = Product('хрен', 140, 12, 'еда')
Morzh = Product('мясоморжа', 10000, 90, 'еда')
Shambala = Store()
# Shambala.add_product(Hren)
# Shambala.add_product(Morzh)
# Shambala.find_product(Hren)
# Shambala.find_product(Morzh)
# Shambala.getabsolute()
# Shambala.get_products_by_category('еда')

identification_total_number_int = 0

class LbrI():
    def __init__(self, title, id, aviable):
        self.title = title
        self.id = id
        self.avbl = aviable
        

    def checkout(self):
        self.avbl = False
        return False

    def retitem(self):
        self.avbl = True
        return True
    
    def get_info(self):
        print(f'Название: {self.title}')
        print(f'ID: {self.id}')
        print(f'Доступно: {self.avbl}')


class Book(LbrI):
    def __init__(self, title, id, aviable, author, pages, genre):
        super().__init__(title, id, aviable)
        self.author = author
        self.pages = pages
        self.genre = genre

    def get_info(self):
        print(super().get_info())
        print(f'Автор: {self.author}')
        print(f'Страницы: {self.pages}')
        print(f'Жанр: {self.genre}')
        print('----')
        
class Magazine(LbrI):
    def __init__(self, title, id, aviable, issuenumber, date):
        super().__init__(title, id, aviable)
        self.isss = issuenumber
        self.date = date

    def get_info(self):
        print(super().get_info())
        print(f'Номер: {self.isss}')
        print(f'Дата: {self.date}')
        print('----')

class DVD(LbrI):
    def __init__(self, title, id, aviable, director, duration, release):
        super().__init__(title, id, aviable)
        self.director = director
        self.duration = duration
        self.release = release

    def get_info(self):
        print(super().get_info())
        print(f'Режиссер: {self.director}')
        print(f'Хронометраж: {self.duration}')
        print(f'Дата: {self.release}')
        print('----')

class Library():
    def __init__(self):
        self.books = []
        self.identification_total_number_int = identification_total_number_int

    def addbooks(self, bookslist):
        self.books.append(bookslist)

    def findcalls(self, itsneedto):
        ttlid = ''
        for i in self.books:
            if i == itsneedto and i.self.avbl == True:
                ttlid += str(i.self.id) + ' '
        print(ttlid)


book = Book('Идиот', identification_total_number_int, True, 'Достоевский', 1000, 'Я не знаю какой это жанр')
magazin = Magazine('У меня нет рта, но я должен кричать', identification_total_number_int, True, 1, 2000)
dvd = DVD('Маша и Медведь', identification_total_number_int, True, 'Мельница', 999, 2011)
print(identification_total_number_int)
book.get_info()
lbbr = Library()
lbbr.addbooks(book)
lbbr.addbooks(magazin)
lbbr.addbooks(dvd)
lbbr.findcalls(Book)