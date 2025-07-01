
# Calculate Average Temperature with Lists

num_days = int(input("Enter the number of days: "))
total_temp = 0.0 # Initialize total temperature to 0.0
temperatures = [] # Initialize an empty list to store temperatures
for i in range(1, num_days + 1):
    next_temp = float(input(f"Enter the temperature for day {i}: "))
    temperatures.append(next_temp) # Append the next temperature to the list
    total_temp += next_temp # Add the next temperature to the total temperature

average_temp = total_temp / num_days # Calculate the average temperature
print("\n")
print(f"The average temperature over {num_days} days is: {average_temp:.2f}°C")

above_temp = 0 # Initialize counter for temperatures above average
for temp in temperatures:
    if temp > average_temp: # Check if the temperature is above average
        above_temp += 1 # Increment the counter

print(f"There are {above_temp} days with temperatures above the average.") # Print the count of above-average temperatures
