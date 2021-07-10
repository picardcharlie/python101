# Population Growth Calculator
# Write the necessary code to display the total population count for the next 3 years (without a leap year).
# Here are the specifications:
# In the country we want to investigate:
# The current population is 380,123,456
# One person is born every 6 seconds
# One person dies every 12 seconds
# One person immigrates every 40 seconds

total_seconds = 31536000
starting_pop = 380123456
born_per_year = total_seconds / 6
death_per_year = total_seconds / 12
immigrate_per_year = total_seconds / 40

print("Starting population: " + str(starting_pop))

first_year = starting_pop + born_per_year + immigrate_per_year - death_per_year
print("First year total population: " + str(first_year))

second_year = first_year + born_per_year + immigrate_per_year - death_per_year
print("Second year total population: " + str(second_year))

third_year = second_year + born_per_year + immigrate_per_year - death_per_year
print("Third year total population: " + str(third_year))