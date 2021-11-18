class Bank_account:
	def __init__(self):
		self.balance = 0
		print("Hello!! Welcome to dopsit and Withdrawal Machine!!\n")

	def deposit(self):
		amount = float(input("Enter Amount to be Deposited: \n"))
		self.balance += amount
		print(f"You Deposited:  {amount} \n")
		
	def withdrawal(self):
		amount = float(input("Enter Amount to be Withdrawal: \n"))
		
		if self.balance >= amount:
			self.balane -= amount
			print(f"You Withdraw  {amount} \n")
			
		else:
			print("\n Insufficiant balance")
			
			
	def display(self):
	 	print("\n Net Available balance is = " + self.balance)




acc = Bank_account()
acc.deposit()
acc.withdrawal()
acc.display()
