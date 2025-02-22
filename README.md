# Expense-tracker
# Expense Tracker 🧾💰

## 📌 Project Description
This is a Python-based Expense Tracking System that helps users to track financial expenses.  Using Object-Oriented Programming (OOP), this project manages expenses by allowing users to add, update, retrieve, and remove expenses efficiently.

## 🛠️ Features
- Store expenses with title, amount, date, and category.
- Retrieve expenses by ID or title.
- Organized using OOP principles.
- Calculate and display total and average expenses in a structured format
- Store timestamps for when expenses are created and updated
  
## 🛠 Technologies Used 
- Python 3.x 
- UUID (for unique expense IDs) 
- Datetime module (for timestamps) 


## 📂 Project Structure 

```
expense-tracker/
│── expense.py          # Defines Expense and ExpenseDatabase classes
│── test_expense.py     # Contains test cases to validate the project
│── main.py             # Main script to interact with the tracker
│── README.md           # Documentation file (this file)
│── .gitignore          # Prevents unnecessary files from being uploaded
```

---

## 🚀 How to Clone & Set Up the Project
Follow these steps to download and run the project on your local machine.  

### 1️⃣ Clone the Repository
Open your terminal (or Command Prompt) and run:  

```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

### 2️⃣ Ensure Python is Installed
Check if you have Python installed by running:  

```bash
python --version
```
If Python is not installed, download it from [here](https://www.python.org/downloads/).  

---

## 📌 How to Run the Code

### 1️⃣ Running the Main Program
To run the main program where you can add, remove, and retrieve expenses, execute:  

```bash
python exxpense.py
```

### 2️⃣ Running the Test File 
To test the `Expense` and `ExpenseDatabase` functionalities:  

```bash
python testexpense.ipynb
```

### 3️⃣ Example Usage (Python Interactive Mode)  
If you want to test manually, open Python in interactive mode:  

```bash
python
```

Then, run:  

```python
from expense import Expense, ExpenseDatabase

# Create an instance of ExpenseDatabase
db = ExpenseDatabase()

# Add expenses
expense1 = Expense("Groceries", 50.75)
expense2 = Expense("Lunch", 12.99)

db.add_expense(expense1)
db.add_expense(expense2)

# Retrieve all expenses
for exp in db.expenses:
    print(exp.to_dict())

# Retrieve expense by ID
expense = db.get_expense_by_id(expense1.id)
print(expense.to_dict())
```

---

## 📌 Features & Functions 

### ✅ Expense Class 
Represents an individual financial expense.  

#### Attributes:  
- `id`: Unique identifier (UUID).  
- `title`: Name of the expense.  
- `amount`: Cost of the expense.  
- `created_at`: Timestamp when the expense was created.  
- `updated_at`: Timestamp when it was last updated.  

#### Methods:  
- `__init__`: Initializes attributes.  
- `update(title, amount)`: Updates title and amount, modifies `updated_at`.  
- `to_dict()`: Returns a dictionary representation of the expense.  

---

### ✅ ExpenseDatabase Class  
Manages a collection of `Expense` objects.  

#### Attributes:  
- `expenses`: List of stored expenses.  

#### Methods:  
- `add_expense(expense)`: Adds a new expense.  
- `remove_expense(expense_id)`: Removes an expense by ID.  
- `get_expense_by_id(expense_id)`: Finds an expense by its unique ID.  
- `get_expense_by_title(title)`: Retrieves expenses by their title.  
- `to_dict()`: Returns a list of dictionaries representing all expenses.  

---

## 💡 Sample Output  
When you **run `exxpense.py` or `testexpense.py`**, you should see an output similar to this:  

```json
{
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "title": "Lunch",
    "amount": 12.99,
    "created_at": "2025-02-20T10:30:00Z",
    "updated_at": "2025-02-20T10:30:00Z"
}
```

## 📌 Contributing  
If you’d like to contribute to this project, follow these steps:  

1. **Fork the repository**  
2. **Create a new branch** 
3. **Make your changes**  
4. **Submit a Pull Request**  

---

## **📄 License**  
This project is licensed under the **MIT License**. Feel free to modify and distribute it.  

---

## **🔗 Connect with Me!**  
If you have any questions or suggestions, reach out:  

📧 Email: **preciousochiobi18.com**  
🔗 GitHub: [oge-ochiobi](https://github.com/oge-ochiobi)  
📍 LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/precious-ochiobi)  

