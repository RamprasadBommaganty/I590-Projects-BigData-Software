import sys
def fizzbuzz(n):
	for i in range(1,n):
		if(i%6==0):
			print("fizzbuzz")
		elif(i%2==0):
			print("fizz")
		elif(i%3==0):
			print("buzz")
		else:
			print(i)

fizzbuzz(int(sys.argv[1]))
