import json
from datetime import datetime


class Datecalculator:

    def __init__(self, date1, date2):
        try:
            self.date1 = datetime.strptime(date1, '%d.%m.%Y')
            self.date2 = datetime.strptime(date2, '%d.%m.%Y')
        except ValueError:
            print("its no valid date")
            return

    def calculate(self):
        banana = self.date2 - self.date1
        days = banana.days
        years = days // 365
        months = (days % 365) // 30
        weeks = ((days % 365) % 30) // 7
        remaining_days = ((days % 365) % 30) % 7
        return f"{years} years {months} months {weeks} weeks {remaining_days} days"

    def save_result(self):
        data = {
            'date1': self.date1.strftime('%d.%m.%Y'),
            'date2': self.date2.strftime('%d.%m.%Y'),
            'result': self.calculate()
        }
        try:
            with open("result.json", "r") as f:
                history = json.load(f)
        except: 
            history = [] 

        history.append(data)          

        with open("result.json", "w") as f:
            json.dump(history, f)


date1 = input("Enter the first date ('%d.%m.%Y'): ")
date2 = input("Enter the second date ('%d.%m.%Y'): ")

cals = Datecalculator(date1, date2)
if hasattr(cals, 'date1'):
    print(cals.calculate())
    cals.save_result()
    print("result saved to result.json")