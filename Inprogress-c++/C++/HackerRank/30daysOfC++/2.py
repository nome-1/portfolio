
def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    l=tip_percent/100*meal_cost
    n=tax_percent/100*meal_cost
    print(round(meal_cost+l+n))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)