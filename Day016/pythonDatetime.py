# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()
# Extract day, month, year, hour, and minute from the current date and time
current_day = current_datetime.day
current_month = current_datetime.month
current_year = current_datetime.year
current_hour = current_datetime.hour
current_minute = current_datetime.minute
# Get the timestamp from the current date and time
timestamp = current_datetime.timestamp()
print("Current Date and Time:")
print(f"Day: {current_day}")
print(f"Month: {current_month}")
print(f"Year: {current_year}")
print(f"Hour: {current_hour}")
print(f"Minute: {current_minute}")
print(f"Timestamp: {timestamp}")


# Format the current date using this format: "%m/%d/%Y, %H:%M:%S"
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Format the current date using the specified format
formatted_date = current_datetime.strftime("%m/%d/%Y, %H:%M:%S")

print("Formatted Current Date and Time:")
print(formatted_date)


# Today is 5 December, 2019. Change this time string to time.
from datetime import datetime

# Input time string
time_string = "5 December, 2019"

# Convert time string to datetime object
time = datetime.strptime(time_string, "%d %B, %Y")

print("Converted Time:")
print(time)


# Calculate the time difference between now and new year.
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Get the upcoming New Year
new_year = datetime(current_datetime.year + 1, 1, 1)

# Calculate the time difference
time_difference = new_year - current_datetime

print("Time Difference until New Year:")
print(time_difference)


# Calculate the time difference between 1 January 1970 and now.
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Define the Unix epoch (January 1, 1970)
epoch = datetime(1970, 1, 1)

# Calculate the time difference
time_difference = current_datetime - epoch

print("Time Difference since Unix Epoch:")
print(time_difference)