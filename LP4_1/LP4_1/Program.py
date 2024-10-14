
copies = int(input("Enter # of copies to print:  "))
price = 0
cost = 0

if copies > 0 and copies <= 99:
    price = .30
elif cpoes > 90 and copies <= 499:
    price = .28
elif cpoes > 499 and copies <= 749:
    price = .28
elif cpoes > 749 and copies <= 1000:
    price = .26
elif copies > 1000:
    price = .25
else:
    print("Invalid # of copies")

cost = copies * price
print("Price per copy is $" + str(price))
print("Total cost is $" + str(round(cost,2)))
input() # Press 'Enter' to close; only needed for sharp develoup




























print "Hello, World!"
