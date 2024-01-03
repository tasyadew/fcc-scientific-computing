"""
Complete the Category class in budget.py. 

---
It should be able to instantiate objects based on different budget categories 
like food, clothing, and entertainment. When objects are created, they are passed 
in the name of the category. The class should have an instance variable called 
ledger that is a list. The class should also contain the following methods:

A deposit method that accepts an amount and description. 
If no description is given, it should default to an empty string. 
The method should append an object to the ledger list in the form of 
{"amount": amount, "description": description}.

A withdraw method that is similar to the deposit method, 
but the amount passed in should be stored in the ledger as a negative number. 
If there are not enough funds, nothing should be added to the ledger. 
This method should return True if the withdrawal took place, and False otherwise.

A get_balance method that returns the current balance of the budget category based on 
the deposits and withdrawals that have occurred.

A transfer method that accepts an amount and another budget category as arguments. 
The method should add a withdrawal with the amount and the description 
"Transfer to [Destination Budget Category]". The method should then add a deposit to the 
other budget category with the amount and the description "Transfer from [Source Budget Category]". 
If there are not enough funds, nothing should be added to either ledgers. 
This method should return True if the transfer took place, and False otherwise.

A check_funds method that accepts an amount as an argument. 
It returns False if the amount is greater than the balance of the budget category and 
returns True otherwise. This method should be used by both the withdraw method and transfer method.

---
When the budget object is printed it should display:

A title line of 30 characters where the name of the category is centered in a line of * characters.
A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
A line displaying the category total.
"""

class Category():

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.amount = 0

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += item["description"][:23].ljust(23) + "{:.2f}".format(item["amount"]).rjust(7) + "\n"
            total += item["amount"]
        output = title + items + "Total: " + str(total)
        return output

    def deposit(self, amount, description=""):
        self.amount = amount
        self.balance += amount
        return self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == False:
            return False
        self.amount = amount
        self.balance -= amount
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, name):
        if self.check_funds(amount) == False:
            return False
        self.amount = amount

        # balance change for both accounts
        self.balance -= amount
        name.balance += amount

        # ledger change for both accounts
        self.ledger.append({"amount": -amount, "description": "Transfer to " + name.name})
        name.ledger.append({"amount": amount, "description": "Transfer from " + self.name})

        return True
        

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

"""
Create a function (outside of the class) called create_spend_chart 
that takes a list of categories as an argument. 
It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. 
The percentage spent should be calculated only with withdrawals and not with deposits. 
Down the left side of the chart should be labels 0 - 100. 
The "bars" in the bar chart should be made out of the "o" character. 
The height of each bar should be rounded down to the nearest 10. 
The horizontal line below the bars should go two spaces past the final bar. 
Each category name should be written vertically below the bar. 
There should be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.
"""
def create_spend_chart(categories):
    # get total spent
    total_spent = 0
    for category in categories:
        total_spent += category.amount

    # get percentage spent for each category
    percentages = []
    for category in categories:
        percentage = category.amount / total_spent * 100
        percentages.append(percentage)

    # create chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    ----------\n"

    # get longest category name
    longest_name = 0
    for category in categories:
        if len(category.name) > longest_name:
            longest_name = len(category.name)

    # add category names to chart
    for i in range(longest_name):
        chart += "     "
        for category in categories:
            if len(category.name) > i:
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < longest_name - 1:
            chart += "\n"

    return chart