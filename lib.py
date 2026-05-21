class LibraryMember:
    max_limit=3

    def __init__(self,member_name,books_borrowed):
        self.member_name=member_name
        self.books_borrowed=books_borrowed
    def borrow(self):
        if self.books_borrowed<=LibraryMember.max_limit:
            self.books_borrowed+=1
        else:
            return "invalid"
    @classmethod
    def main(cls,new):
        cls.max_limit=new
    @staticmethod
    def allow():
        return LibraryMember.max_limit>0


s1=LibraryMember("mani",3)
s2=LibraryMember("yeshu",3)
LibraryMember.max_limit=4
print(f"{s1.member_name},{s1.books_borrowed}")
print(f"{s2.member_name},{s2.books_borrowed}")


