# Fizz Buzz game / different solutions

for n in range(1, 101):
  if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
  elif n % 5 == 0:
    print('Buzz')
  elif n % 3 == 0:
    print('Fizz')
  else:
    print(n)
    
# another solution below
    
for num in range(1,101):
  
  if num%3 == 0:
    if num%5 == 0:
      print("FizzBuzz")
    else:
      print("Fizz")
  elif num%5 == 0:
    print ("Buzz")
  else:
    print(num)
