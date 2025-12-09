#This question may be a little challenging if your math skills are rusty. 
# Don't be afraid to take advantage of the hints. 
# Try your best to solve the problem,
#  but don't feel compelled to complete it if you become frustrated.
#Use the REPL and the arithmetic operators to extract the individual digits of 4936:

#One place is 6.
#Tens place is 3.
#Hundreds place is 9.
#Thousands place is 4.


number = 4936
ones = 4936 % 10
tens = (4936 // 10) % 10
hundreds = (4936 // 100) % 10
thousands = (4936 // 1000) % 10 
print(ones, tens, hundreds, thousands)  
