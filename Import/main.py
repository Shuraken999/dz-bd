import datetime

from application.salary import calculate_salary
from application.db.people import get_emloyees
from dirty_main import *

calculate_salary()
get_emloyees()
print('Today is ', datetime.date.today())
print_info()
