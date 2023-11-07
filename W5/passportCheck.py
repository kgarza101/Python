from passport import * 

alan = Passport(
			"Alan", 
			"Turing", 
			"1912-06-23", 
			"The United Kingdom", 
			"1954-06-07"
		)

alan.is_valid()

print(alan.summary())

