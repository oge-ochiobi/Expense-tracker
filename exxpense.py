# Import required modules
import uuid
from datetime import datetime, timezone

# Expense Class
class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())  # Unique ID
        self.title = title
        self.amount = float(amount)
        self.created_at = datetime.now(timezone.utc)  # Corrected UTC timestamp
        self.updated_at = self.created_at  # Initially same as created_at

    def update(self, new_title=None, new_amount=None):
        """Update the expense title and/or amount"""
        if new_title:
            self.title = new_title
        if new_amount:
            self.amount = float(new_amount)
        self.updated_at = datetime.now(timezone.utc)  # Corrected UTC timestamp

    def to_dict(self):
        """Return expense details as a dictionary"""
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }

# Expense Database Class
class ExpenseDatabase:
    def __init__(self):
        self.expenses = []  # List to store Expense objects

    def add_expense(self, expense):
        """Add an expense to the database"""
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        """Remove an expense by ID"""
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]

    def get_expense_by_id(self, expense_id):
        """Find an expense by its unique ID"""
        for exp in self.expenses:
            if exp.id == expense_id:
                return exp.to_dict()
        return None  # Return None if not found

    def get_expenses_by_title(self, title):
        """Find all expenses with a given title"""
        return [exp.to_dict() for exp in self.expenses if exp.title == title]

    def to_dict(self):
        """Return all expenses as a list of dictionaries"""
        return [exp.to_dict() for exp in self.expenses]

# ✅ Step 2: Creating an Expense Database
db = ExpenseDatabase()

# ✅ Creating Expenses (Make sure all expenses are created)
expense1 = Expense("Groceries", 50.75)  # Ensure expense1 exists
expense2 = Expense("Lunch", 12.99)
expense3 = Expense("Taxi", 8.50)

# ✅ Adding Expenses to Database
db.add_expense(expense1)
db.add_expense(expense2)
db.add_expense(expense3)

# ✅ Viewing All Expenses
print(db.to_dict())

# ✅ Searching for an Expense by Title
print(db.get_expenses_by_title("Lunch"))

# ✅ Removing an Expense
db.remove_expense(expense2.id)
print(db.to_dict())  # Lunch should be removed
