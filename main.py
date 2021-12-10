from matplotlib import pyplot

# num = randint(1,500)
num = int(input('Enter Starting Number: '))

vals = [num]

print(num)

while num != 1:
    num = num // 2 if num % 2 == 0 else (num * 3) + 1
    vals.append(num)
    print(num)


pyplot.plot(vals)
for i, txt in enumerate(vals):
    pyplot.annotate(txt, (i, vals[i]))
    pyplot.title('Collatz Conjecture')
pyplot.show()