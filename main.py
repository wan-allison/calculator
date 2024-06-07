numone = int(input("Choose a first number:　"))
numtwo = int(input("Choose a second number: "))
symbol = input("Now choose a mathematical symbol: ")
print("")
if symbol == "/":
  print(numone / numtwo)
elif symbol == "+":
  print(numone + numtwo)
elif symbol == "*":
  print(numone * numtwo)
else:
  print(numone - numtwo)