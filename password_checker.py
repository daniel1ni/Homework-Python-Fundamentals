
print("Welcome to the password checker!\nA strong password must meet the following criteria:")
print("-Between 7 and 20 characters long")
print("-Include at least one special character")
print("-Include at least one number")

# Function to validate the password

def password_check(passwd):
	
	SpecialSym =['$', '@', '#', '%']
	val = True
	
	if len(passwd) < 7:
		print('length should be at least 6')
		val = False
		
	if len(passwd) > 20:
		print('length should be not be greater than 8')
		val = False
		
	if not any(char.isdigit() for char in passwd):
		print('Password should have at least one numeral')
		val = False
		
	if not any(char.isupper() for char in passwd):
		print('Password should have at least one uppercase letter')
		val = False
		
	if not any(char.islower() for char in passwd):
		print('Password should have at least one lowercase letter')
		val = False
		
	if not any(char in SpecialSym for char in passwd):
		print('Password should have at least one of the symbols $@#')
		val = False
	if val:
		return val

attempts = 0



while attempts < 3:
	passwd = input()
	if password_check(passwd):
		print("Valid password")
		break
	else:
		print("Invalid password")
		attempts+=1
		continue
	