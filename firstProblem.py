__author__ = 'admin'
x = []
a = 0
odd = notOdd = 0
while True:
    a = raw_input()
    if a == '.':
        break
    else:
        if a.isdigit():
            if int(a) % 2 == 0:
                notOdd += 1
            else:
                odd += 1


print "Odd",odd
print "Not odd",notOdd