class Category(object):

    def __init__(self, name):
        self.name = str(name).capitalize()
        self.ledger = []
        self.balance = 0

    # Appends {'amount': amount, 'description':description} to ledger
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount

    # Appends to ledger like deposit -> Amount needs to be negative
    # If funds not there return False otherwise True
    def withdraw(self, amount, description=''):
        successful = True
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            return successful
        return not successful

    def get_balance(self):
        return float(f'{self.balance:.2f}')

    # Withdraw from self then deposit to budget_category of choice
    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, description=f"Transfer to {other.name}")
            other.deposit(amount, description=f"Transfer from {self.name}")
            return True
        print("Transfer Error")
        return False

    # False if amount > balance & True otherwise
    def check_funds(self, amount):
        if (self.balance - amount) < 0:
            return False
        return True

    def display(self):
        display_lst = []
        length = len(self.name) % 2
        stars = ('*'*((30-len(self.name))//2))
        title = f'{stars}{self.name+("*"*length)}{stars}'
        display_lst.append(title)

        for transaction in self.ledger:
            display_lst.append(f'''{transaction["description"][:23]}{" "*((30 - len(transaction["description"][:23]))-len(f'{transaction["amount"]:.2f}'))}{transaction["amount"]:.2f}''')

        display_lst.append(f'Total: {self.get_balance()}')
        return '\n'.join(display_lst)

    def __repr__(self):
        return self.display()


def percent_spent(category):
    return sum([float(category.ledger[x]['amount']) for x in range(len(category.ledger)) if float(category.ledger[x]['amount']) < 0])


def create_spend_chart(categories):
    display_list = []
    withdraw_totals = [percent_spent(categories[x]) for x, percents in enumerate(categories)]
    withdraw_sums = sum(withdraw_totals)
    for i, wd in enumerate(withdraw_totals):
        withdraw_totals[i] = ((abs(wd)/abs(withdraw_sums))*100)
    bar_chart = list([f'{" "*(3-len(str(x)))}{x}| '] for x in range(100, -1, -10))
    for p, bars in enumerate(bar_chart):
        for o in range(len(withdraw_totals)):
            if withdraw_totals[o] >= int(bars[0].split('|')[0]):
                bars.append('o  ')
            else:
                bars.append('   ')
    bar_chart.append([f'{" "*4}{"-"*((len(categories)*3)+1)}'])

    display_list.append('Percentage spent by category')
    for bars in bar_chart:
        display_list.append(''.join(bars))

    grid_len = max([len(z.name) for z in categories])
    cat_grid = list([] for _ in range(grid_len))

    for n, word in enumerate(categories):
        categories[n] = word.name + " " * (grid_len - len(word.name))

    for cat in categories:
        for index, letter in enumerate(cat):
            cat_grid[index] += letter

    for m, rows in enumerate(cat_grid):
        cat_grid[m].insert(0, " "*3)

    for grid in cat_grid:
        display_list.append("  ".join(grid))
        display_list[-1] += '  '

    return '\n'.join(display_list)


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))
