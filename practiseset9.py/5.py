import random
class train:
    def __init__(self,trainno):
        self.trainno=trainno
        
    def book_a_ticket(self,f,to):
        print(f"your ticket is booked in train no:{self.trainno} from:{f} to:{to}")
    def get_status(self,sitno):
        print(f"your sit no is {sitno}")
    def get_fare_info(self):
        print(f"your fare amount will be{random.randint(22,44)}")
a=train(random.randint(222,555))
a.book_a_ticket("kathmandu","pokhara")
a.get_status(33)
a.get_fare_info()

