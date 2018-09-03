class PersonalAccount:
	def __init__(self, name, AccountType, AccountNum, InitialDeposit, gender, amount):
		self.name = name
		self.AccountType = AccountType
		self.AccountNum = AccountNum
		self.InitialDeposit = 0
		self.Deposit = 0
		self.gender = gender
		self.availableBalance = availableBalance
		self.amount = amount

		
		def  Deposit(self,InitialDeposit, availableBalance, Deposit):
			availableBalance = InitialDeposit + Deposit
			if availableBalance <100000 :
				Deposit = int(input(Please enter amount: ))
				availableBalance += Deposit
				if AccountType == "savings":
					






			