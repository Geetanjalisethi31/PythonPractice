print('***************Bank Account *****************')
class bankAccount():
    bankName='SBI'
    def __init__(self,accountNumber,balance):
        self.AccountNumber=accountNumber
        self.Balance=balance
    def dispayAccount(self):
        print('Account Number=',self.AccountNumber)
        print('Balance=',self.Balance)
    def withDrawAmt(self,Amount):

        if self.Balance>=Amount:
            NewAmount=self.Balance-Amount
            print('Remaining amount=',NewAmount)
        else:
            print('Insufficient Balance')
    @ staticmethod
    def user(a):
        print('Welcome to Banking .')
        while True:

            print('Press 1 for AccountEnq 2 for withdraw')

            option=int(input('Enter the Option'))
            if option==1:
                b1.dispayAccount()
            elif option==2:
                print('Enter the Amount ')
                amt=int(input('Enter the amount'))
                b1.withDrawAmt(amt)

            else:
                print('Invalid Entry')
            print('Press 1 to continue 2 Exit')
            n=int(input('Enter the option'))
            if n==1:
              continue
            elif n==2:
               print('Thank u see u Again')
               break
            else:
                print('invalid option')


b1=bankAccount(12345,5000)
b1.dispayAccount()

pin=int(input('enter the pin'))
if pin==2323:
     bankAccount.user(12356)
elif pin==3333:
     bankAccount.user(4567)
else:
     print('invalid pin.Try Again')