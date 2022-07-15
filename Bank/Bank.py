import logging as lg
try:
    lg.basicConfig(filename="Bank.txt",format='%(asctime)s %(message)s',level=lg.INFO)

    lg.info("This is log about the Bank class and It's operations")
    class Bank:
        """
        This is the Docstring of Base class for bank, this includes constructor which accepts 3 variable Name, Account and Balance
        This is the parent class for the SBI and Axis Class.
        The Bank class has three methods greet, account_type and balance.
        """
        lg.info("Bank object is created...")
        def __init__(self, Name, Account, Balance):
            self.Name = Name
            self.Account = Account
            self.Balance = Balance

        def greet(self):
            lg.info("welcome " + self.Name)

        def Account_Type(self):
            lg.info("Your account type is " + self.Account)

        def balance(self):
            lg.info("Your Balance is " + str(self.Balance))



    class SBI(Bank):
        """
        This is the SBI bank class which is derived from the parent class Bank.
        this class has method called withdraw which will help to withdrwa the money from account.
        """

        __BankName = "SBI"
        lg.info("Sbi bank object is initialized...")
        def greet(self):
            lg.info("Welcome to the  SBI "  + self.Name)

        def Account_Type(self):
            lg.info("Your Account type is "+self.Account)

        def balance(self):
            lg.info("Your balance is ", str(self.Balance))

        try:
            def withdraw(self, amount):
                lg.warning("Initalizing withdrawing service...")
                if amount <= self.Balance:
                    self.Balance = self.Balance - amount
                    lg.info("Remaining Balance is " ,str(self.Balance))

                else:
                    lg.warning("You have not enough balance... ")
        except Exception as e:
            lg.exception(e)

        finally:
            lg.info("Thank you for using our services...")



    class Axis(Bank):
        """
        This is the Axis bank class which is derived from the parent class Bank.
        this class has method called withdraw which will help to withdraw the money from account.
        """

        __BankName = "Axis Bank"
        lg.info("You are now in Axis Bank ...")

        def greet(self):
            lg.info("Welcome to the Axis "+ self.Name)

        def Account_Type(self):
            lg.info("Your account type is " + self.Account)

        def balance(self):
            lg.info("Your balance is ", str(self.Balance))

        try:
            lg.warning("Initializing withdrawing service...")
            def withdraw(self,amount):
                if(amount <= self.Balance):
                    self.Balance = self.Balance - amount
                    lg.info("The remaining balance is ")
                else:
                    lg.warning("You don't have enough balance...")
        except Exception as e:
            lg.exception(e)

        finally:
            lg.info("Thank you for using services...")

    lg.info("Creating object of Bank class")
    bank = Bank("John","Saving",1000)
    bank.greet()
    bank.balance()
    bank.Account_Type()

    lg.info("Creating object of SBI class")
    sbi = SBI("James","Current",33000)
    sbi.greet()
    sbi.Account_Type()
    sbi.withdraw(40000)

    lg.info("Creating object of Axis class")
    axis = Axis("Joy","Saving",3000)
    axis.greet()
    axis.Account_Type()
    axis.withdraw(4000)

except Exception as e:
     lg.warning(e)