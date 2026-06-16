from datetime import datetime


def dt_input() :
   while True:   
         try:
             dt1 = input('enter date %d.%m.%Y')
             return datetime.strptime (dt1, '%d.%m.%Y')  
         except ValueError:
             print('is not true')

    

def calculate (dt1, dt2) :
    banana = dt1 - dt2
    days = banana.days  
    years = days // 365
    difference1 = days % 365 
    months  = difference1 // 30 
    difference2 = difference1 % 30 
    weeks = difference2 // 7 
    days = difference2 % 7 
    return years, months, weeks, days

def show_result (years, months, weeks, days,):
    print(f" is written here {years} ear, {months} +- four weeks and ,{weeks} in weeks, also {days} have been calculated ") 
       
  
dt1 = dt_input() 
dt2 = dt_input() 
years, months, weeks, days = calculate(dt2, dt1)
show_result(years, months , weeks, days)    
  
