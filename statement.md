Problem:- 
Tracking daily expenses is difficult when done manually. Users often forget when, where and how much they spent. 
This project aims to build a *simple expense tracking system* using Python to help users maintain records of spending and generate summaries.

Scope of the Project:-
The scope of this project is strictly defined by its Command Line Interface (CLI) nature and its flat file data structure.
In-Scope:
1.Data Entry: Logging expense details (Date, Category, Amount).
2.Data Storage: Persistent storage using a single, local text file (expenses.txt).
3.Reporting: Calculating the grand total and providing category-based monthly summaries.
4.User Interface: Text-based menu and console input/output.
Out-of-Scope (Future Enhancements):
1.Graphical User Interface (GUI).
2.Integration with external APIs or banking services.
3.Complex features like budgeting, forecasting, or recurrence.
4.Database management (e.g., SQLite, MySQL).
5.Advanced error handling (e.g., date parsing, category standardization).

Target Users:-
The primary target users for this simple CLI Expense Tracker are individuals who prioritize simplicity, speed, and local control over their data.
1.Students and Budget-Conscious Individuals: People who need to track spending quickly without the overhead of complex financial software.
2.Developers and Programmers: Users who are comfortable operating within the terminal and prefer lightweight, script-based tools for productivity.
3.Privacy-Focused Users: Individuals who prefer that their sensitive financial data remain completely local and not synced to cloud services.

High-Level Features:-
These are the main capabilities that the application provides to solve the problem of quick expense tracking.
Transactional Logging (CRUD: Create): Allows the user to Add a New Expense record by prompting for the date (DD-MM-YYYY), category, and numerical amount. Persists the data immediately to the expenses.txt file.
Record Viewing (CRUD: Read): Enables the user to View All Expenses recorded in the file, displayed in a clear, column-based format.
Total Accumulation (Reporting): Provides a function to Calculate the Grand Total Spent across all recorded transactions, giving an immediate overall spending figure.
Categorical Analysis (Reporting): Generates a Monthly Summary by filtering transactions by a user-specified month/year (MM-YYYY) and aggregating the total spent per unique category.
