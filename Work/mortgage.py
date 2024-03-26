# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
minimum_payment = 2684.11
total_paid = 0.0
months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

print(f"Months | Total Paid ($) | Remaining Principal ($)")
print("-" * 55)
while principal > 0:
    months += 1
    if principal < minimum_payment:
        payment = principal * (1 + rate / 12)
    elif extra_payment_start_month <= months <= extra_payment_end_month:
        payment = minimum_payment + extra_payment
    else:
        payment = minimum_payment
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    print(f"{months:<6} | ${total_paid:<13,.2f} | ${principal:,.2f}")


print(f"Total Paid: ${total_paid:,.2f}")
print(f"Months: {months}")
