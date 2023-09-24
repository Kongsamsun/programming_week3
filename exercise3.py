class Item():
    count = 0
    def __init__(self, title, cost):
        self.title, self.cost = title, cost
        Item.count += 1
    def getprice(self):
        return "* %s의 가격은 %d원 입니다" % (self.title, self.cost)
    
class Book(Item):
    def __init__(self, title, cost, page, author):
        super().__init__(title, cost)
        self.page, self.author = page, author
    def getprice(self):
        return super().getprice()       
    def __str__(self):
        return "제목: %s, 가격: %d, 페이지 수: %d, 저자: %s" % (self.title, self.cost, self.page, self.author)
    
class Magazine(Item):
    def __init__(self, title, cost, month):
        super().__init__(title, cost)
        self.month = month
    def getprice(self):
        return super().getprice()        
    def __str__(self):
        return "제목: %s, 가격: %d, 출간 월: %d" % (self.title, self.cost, self.month)
    
if __name__ == '__main__':

    book1 = Book('소나기', 10000, 124, '황순원')
    book2 = Book('메밀꽃 필 무렵', 15000, 142, '이효석')
    book3 = Book('난쏘공', 12000, 112, '조세희')
    magazine1 = Magazine('보그', 11000, 9)
    magazine2 = Magazine('싱글즈', 13000, 8)
    print('',book1,'\n',book2,'\n',book3,'\n',magazine1,'\n',magazine2)
    print("총", Item.count, "권")

    print(book2.getprice())
    print(magazine1.getprice())
    print(book1.getprice())