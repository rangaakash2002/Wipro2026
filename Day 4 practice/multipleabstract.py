from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def intrest(self):
        pass
    @abstractmethod
    def loan(self):
        pass
class SBI(Bank):
    def intrest(self):
        print("percentage is 60%")
    def loan(self):
        print("loan is available")
s=SBI()
s.intrest()
s.loan()
