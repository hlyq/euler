#Find the 10,001st Prime Number

print "Which prime would you like?"
StopPrime = int(raw_input("> "))

listofprimes = []

CurrentNum = float(1)
CurrentLength = len(listofprimes)
Divider = float(2)
Quotient = float(1)

while CurrentLength < StopPrime:
    CurrentNum = (CurrentNum + 1)
    Quotient = CurrentNum / Divider

    while Quotient != int(Quotient):
        Divider = (Divider + 1)
        Quotient = CurrentNum / Divider

    if Quotient == 1:
        listofprimes.append(CurrentNum)
        print "Prime %r is" % (CurrentLength + 1),
        print int(listofprimes[(CurrentLength)])

    Quotient = float(1)
    Divider = float(2)

    CurrentLength = len(listofprimes)

print " "
print "<3"