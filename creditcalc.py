import math
import argparse


def diff_payment(p, periods, interest):
    i_ = interest / (12 * 100)
    total_payment = 0
    for m in range(1, periods + 1):
        d_m = math.ceil(p / periods + i_ * (p - (p * (m - 1)) / periods))
        total_payment += d_m
        print(f"Month {m}: payment is {d_m}")
    overpayment_ = total_payment - p
    print(f"\nOverpayment = {overpayment_}")


parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)

args = parser.parse_args()

if args.type == "diff":
    if args.principal and args.periods and args.interest:
        if args.principal > 0 and args.periods > 0 and args.interest > 0:
            diff_payment(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
elif args.type == "annuity":
    if args.principal and args.periods and args.interest:
        i = args.interest / (12 * 100)
        annuity_payment = math.ceil(args.principal * ((i * math.pow(1 + i, args.periods))
                                                      / (math.pow(1 + i, args.periods) - 1)))
        overpayment = annuity_payment * args.periods - args.principal
        print(f"Your annuity payment = {annuity_payment}!")
        print(f"Overpayment = {overpayment}")
    elif args.payment and args.periods and args.interest:
        i = args.interest / (12 * 100)
        principal = math.floor(args.payment / ((i * math.pow(1 + i, args.periods))
                                               / (math.pow(1 + i, args.periods) - 1)))
        overpayment = args.payment * args.periods - principal
        print(f"Your loan principal = {principal}!")
        print(f"Overpayment = {overpayment}")
    elif args.principal and args.payment and args.interest:
        i = args.interest / (12 * 100)
        n = math.ceil(math.log(args.payment / (args.payment - i * args.principal), 1 + i))
        overpayment = n * args.payment - args.principal
        years, months = divmod(n, 12)
        if years == 0:
            print(f"It will take {months} months to repay this loan!")
        elif months == 0:
            print(f"It will take {years} years to repay this loan!")
        else:
            print(f"It will take {years} years and {months} months to repay this loan!")
        print(f"Overpayment = {overpayment}")
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")


# python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10

# > python creditcalc.py --principal=1000000 --periods=60 --interest=10
# Incorrect parameters

# > python creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
# Incorrect parameters

# > python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
# Incorrect parameters

# > python creditcalc.py --type=annuity --principal=1000000 --payment=104000
# Incorrect parameters

# > python creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
# Incorrect parameters 

# > python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
# Month 1: payment is 108334
# Month 2: payment is 107500
# Month 3: payment is 106667
# Month 4: payment is 105834
# Month 5: payment is 105000
# Month 6: payment is 104167
# Month 7: payment is 103334
# Month 8: payment is 102500
# Month 9: payment is 101667
# Month 10: payment is 100834
# 
# Overpayment = 45837

# > python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
# Your annuity payment = 21248!
# Overpayment = 274880

# > python creditcalc.py --type=diff --principal=1000000 --payment=104000
# Incorrect parameters.

# > python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8
# Month 1: payment is 65750
# Month 2: payment is 65344
# Month 3: payment is 64938
# Month 4: payment is 64532
# Month 5: payment is 64125
# Month 6: payment is 63719
# Month 7: payment is 63313
# Month 8: payment is 62907
#
# Overpayment = 14628

# > python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
# Your loan principal = 800018!
# Overpayment = 246622

# > python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
# It will take 2 years to repay this loan!
# Overpayment = 52000
