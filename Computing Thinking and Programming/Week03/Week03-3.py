class Item:
    count = 0
    def __init__(self, title, price):
        self.title = title
        self.price = price
        Item.count += 1

    def getprice(self):
        return(print("* %s 의 가격은 %d 입니다." %(self.title, self.price)))

    def __str__(self):
        return("총 %f 권" %(Item.count))

class Book(Item):
    def __init__(self, title, price, pages, author):
        super().__init__(title, price)
        self.pages = pages
        self.author = author
    def __str__(self):
        return("제목 : %s, 가격 : %d, 페이지 수 : %d, 저자 : %s" %(self.title, self.price, self.pages, self.author))

class Magazine(Item):
    def __init__(self, title, price, month):
        super().__init__(title, price)
        self.month = month
    def __str__(self):
        return("제목 : %s, 가격 : %d, 출간 월 : %d" %(self.title, self.price, self.month))