import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
from custom_module import generate_time_travel_message

current_date_time = dt.datetime.now()
print(current_date_time)

#create base cost
base_cost = Decimal("1000.00")
random_year = randint(1900, current_date_time.year)
year_difference = abs(current_date_time.year - random_year)
final_cost = base_cost * year_difference
print(final_cost)

destination = ["Prague", "Athens", "Krakow"]
random_selection = choice(destination)
print(random_selection)

message = generate_time_travel_message(random_year, random_selection, final_cost)
print(message)

