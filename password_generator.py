#Enter the number of letters you would like to be in your password
import random 
import string
def password_generator(n): 
	temp_num = 0
	#pass_string = random.choice(string.ascii_letters)  
	for i in range(n): 
		temp_num = random.randint(1,9)
		pass_string = str(pass_string) + str(temp_num) 

	print(pass_string)
	return pass_string 
password_generator(10)