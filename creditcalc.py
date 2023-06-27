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
