from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime
from emoji import emojize

if __name__ == "__main__":
    print(emojize('Python is :thumbs_up:'))
    dt = datetime.now()
    print(f'Current date: {dt.day}.{dt.month}.{dt.year}')
    get_employees('Ivan Petrov')
    calculate_salary(19900.00)