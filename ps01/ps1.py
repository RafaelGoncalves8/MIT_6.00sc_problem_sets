# # ps_02 - Paying off credit card debt

# Minimum monthly payment = mmp rate * balance
# Interest Paid = Anual interest rate / 12 * balance
# Principal paid = mmp - interest paid
# Remaining balance = balance - principal paid

# Program 01:

balance = float(raw_input('Enter the outstanding balance on your credit card:'))
ai_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
mmp_rate = float(raw_input('Enter the minimum monthly payment rate as a decimal:'))

print '=' * 20

for i in range(1,13):
	mmp = float(mmp_rate * balance)
	int_paid = float(ai_rate/12.0 * balance)
	prin_paid = float(mmp - int_paid)
	remain_balance = float(balance - prin_paid)	
	print 'Month: %d' % i
	print '.' * 20
	print 'Minimum monthly payment: $%d' % mmp
	print 'Principle paid: $%d' % prin_paid
	print 'Remaining balance: $%d' % remain_balance
	print "\n=", "=" * 19
	balance = remain_balance
	
# Program 02:

balance0 = float(raw_input('Enter the outstanding balance on your credit card:'))
ai_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
mi_rate = ai_rate/12.0
mp = 0
balance = balance0

while balance > 0:
	mp += 10
	numMonths = 0
	balance = balance0
	while numMonths < 12 and balance > 0:
		numMonths += 1
		interest = mi_rate * balance
		balance -= (mp - interest)
balance = round(balance, 2)

print "RESULT"
print "=" *20
print "Monthly payment to pay off debt in 1 year:", mp
print "Number of months needed:", numMonths
print "Balance:",balance

# # Program 03:

balance0 = float(raw_input('Enter the outstanding balance on your credit card:'))
ai_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
mi_rate = ai_rate/12.0
mp = 0
balance = balance0
low = balance/12.0
high = (balance*(1+mi_rate)**12)/12
mp = (low+high)/2
epsilon = 0.01
numMonths = 0

while True:
	balance = balance0
	mp = (low + high)/2
	
	for month in range(1,13):
        interest = round(balance*mi_rate, 2)
        balance += interest - mp
        if balance <= 0:
            break
			
	if (high - low < 0.005):
		print "RESULT"
		print "=" *20
		mp = round(mp + 0.004999, 2)
		print "Monthly payment to pay off debt in 1 year:", round(mp,2)
		
		balance = balance0
        for month in range(1,13):
            interest = round(balance*mi_rate, 2)
            balance += interest - mp
            if balance <= 0:
                break
        print "Number of months needed:", month
        print "Balance:", round(balance,2)
        break
	elif balance < 0:
        high_payment = monthly_payment
    else:
        low_payment = monthly_payment



