# Calculate Average Temparature

num_days = int(input("Enter the number of days: "))

total_temp = 0
for i in range(1, num_days+1):
    temp = float(input(f"Enter the temperature for day {i}: "))
    total_temp += temp

average_temp = total_temp / num_days
print("\n")
print(f"The average temperature over {num_days} days is: {average_temp:.2f}°C")