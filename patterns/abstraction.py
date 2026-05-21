# 1
#
# from abc import ABC,abstractmethod
# import math
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return math.pi*self.r*self.r
#     def perimeter(self):
#         return 2*math.pi*self.r
# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         return self.l*self.b
#     def perimeter(self):
#         return 2*(self.l+self.b)
# class Triangle(Shape):
#     def __init__(self,a,b,c,length,width):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.length=length
#         self.width=width
#     def area(self):
#         return 0.5*self.length*self.width
#     def perimeter(self):
#         return self. a + self.b + self.c
#
# shapes=[Circle(3),Rectangle(4,5),Triangle(4,5,6,6,7)]
# for s in shapes:
#     print(s.area())
#     print(s.perimeter())


# 2
# from abc import ABC,abstractmethod
# class PaymentGateway(ABC):
#     @abstractmethod
#     def authenticate(self):
#         pass
#     @abstractmethod
#     def pay(self,amount):
#         pass
#     @abstractmethod
#     def refund(self,amount):
#         pass
#
# class UPIPayment(PaymentGateway):
#     def authenticate(self):
#         print("account has been verified")
#     def pay(self,amount):
#         print("amount has been paid",amount)
#     def refund(self,amount):
#         print("amount had been refunded",amount)
# class CardPayment(UPIPayment):
#     pass
# class NetBankingPayment(UPIPayment):
#     pass
# s=UPIPayment()
# s.pay(5000)
# s.refund(60000)
# s1=CardPayment()
# s1.pay(4000)
# s1.refund((9000))


#3
# from abc import ABC,abstractmethod
# class VehicleControl(ABC):
#     @abstractmethod
#     def accelerate(self):
#         pass
#     @abstractmethod
#     def brake(self):
#         pass
#     @abstractmethod
#     def steer(self):
#         pass
# class CarControl(VehicleControl):
#     def accelerate(self):
#         print("vechile is accterating")
#     def brake(self):
#         print("brake")
#     def steer(self):
#         print("steer")
# class BikeControl(CarControl):
#     pass
# class TruckControl(CarControl):
#     pass
# a=BikeControl()
# a.steer()
# a.brake()
# a.accelerate()



# 4
# from abc import ABC,abstractmethod
# class DatabassDriver(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#     @abstractmethod
#     def exectue(self,query):
#         pass
#     @abstractmethod
#     def close(self):
#         pass
# class MySQLDriver(DatabassDriver):
#     def connect(self):
#         print("database connecting with mysql")
#     def exectue(self,query):
#         print("query is executing",query)
#     def close(self):
#         print("db mysql is closing")
# class PostgresDriver(DatabassDriver):
#     def connect(self):
#         print("database connecting with postgrsdriver")
#     def exectue(self,query):
#         print("postgresdriver execting tge query",query)
#     def close(self):
#         print("postgresdriver is closing")
# class SQLliteDriver(DatabassDriver):
#     def connect(self):
#         print("database connecting with mysqllite")
#     def exectue(self,query):
#         print("my sql lite is executing a query",query)
#     def close(self):
#         print("my sql lite is closing")
# def run(driver:DatabassDriver):
#     driver.connect()
#     driver.exectue("SELECT * from users")
#     driver.close()
# db=MySQLDriver()
# run(db)
# print()
# db=SQLliteDriver()
# run(db)
# print()
# db=MySQLDriver()
# run(db)
# print()


#5
# from abc import ABC,abstractmethod
# class ReportGenerator(ABC):
#     @abstractmethod
#     def load_data(self):
#         pass
#     @abstractmethod
#     def process(self):
#         pass
#     @abstractmethod
#     def export(self):
#         pass
# class PDFReport(ReportGenerator):
#     def load_data(self):
#         print("dataloading")
#     def process(self):
#         print("data processing")
#     def export(self):
#         print("data exporting")
# class ExcelReport(PDFReport):
#     pass
# a=PDFReport()
# a.load_data()
# a.process()
# a.export()

#6
# from abc import ABC ,abstractmethod
# class RobotCommand(ABC):
#     @abstractmethod
#     def execute(self):
#         pass
#     @abstractmethod
#     def undo(self):
#         pass
# class PickCommand(RobotCommand):
#     def execute(self):
#         print("command execting")
#     def undo(self):
#         print("undo the command")
# class PlaceCommand(PickCommand):
#     pass
# class MoveCommand(PickCommand):
#     pass
# a=PickCommand()
# a.execute()
# a.undo()


#7
# from abc import ABC,abstractmethod
# class MLModel(ABC):
#     @abstractmethod
#     def train(self,data):
#         pass
#     @abstractmethod
#     def predict(self,x):
#         pass
#     @abstractmethod
#     def evaluate(self,test_set):
#         pass
# class LinerRegression(MLModel):
#     def train(self,data):
#         print("data is training")
#     def predict(self,x):
#         print("data is peridicting")
#         return 10
#     def evaluate(self,test_set):
#         print("data is evaluating")
# class Decisiontree(LinerRegression):
#     pass
# a=LinerRegression()
# a.train(8)
# a.evaluate(9)
# a.predict(10)


#9
# from abc import ABC,abstractmethod
# class Mediaplayer(ABC):
#     @abstractmethod
#     def load(self):
#         pass
#     @abstractmethod
#     def play(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
# class MP3Player(Mediaplayer):
#     def load(self):
#         print("music is loading")
#     def play(self):
#         print("music is playing")
#     def stop(self):
#         print("music is stoping")
# class WAVPlayer(MP3Player):
#     pass
# class AACPlayer(MP3Player):
#     pass
# a=WAVPlayer()
# a.load()
# a.play()
# a.stop()


#8
# def send_email(message):
#     print("sending mail",message)
# def send_sms(message):
#     print("sending sms",message)
# def send_push(message):
#     print("push notification",message)
# def modify_user(method,message):
#     if