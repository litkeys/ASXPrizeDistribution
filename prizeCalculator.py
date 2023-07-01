# the sample values in portfolio_values are from our winning league in 2023
# $300 have been deducted from normal total_prize for extra arrangements

# =======================
dampen_factor = 0.8 # 1 is normal scale, 0.5 is square root, etc.
# =======================

total_prize = 2700 # the total prize received for winning

minimum_prize = 100 # this is the prize received by the member with the lowest portfolio value

with open("portfolio_values.txt") as t:
    data = t.readlines()[1:]
    member_portfolios = sorted(float(value) for value in data)
    lowest_portfolio, highest_portfolio = member_portfolios[0], member_portfolios[-1]
    member_count = len(member_portfolios)

#print(member_portfolios)

if minimum_prize * member_count > total_prize:
    print("Minimum prize too high, distribution is not possible.")
    quit()

bonus_pool = total_prize - minimum_prize * member_count

max_deviation = sum((value - lowest_portfolio)**dampen_factor for value in member_portfolios)
deviation_ratios = [(value - lowest_portfolio)**dampen_factor / max_deviation for value in member_portfolios]

distributed_prizes = [minimum_prize + deviation_ratios[i] * bonus_pool for i in range(member_count)]

print("Below are the prizes (from low to high)")
for prize in distributed_prizes:
    print(round(prize, 1))