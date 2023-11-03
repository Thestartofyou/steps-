import random
import datetime

# Initialize a variable to store the total steps
total_steps = 0

# Create a function to generate random steps for a given date
def generate_random_steps(date):
    # Simulate step data
    return random.randint(1000, 15000)

# Get today's date
today = datetime.date.today()

# Simulate tracking steps for the last 7 days
for _ in range(7):
    steps = generate_random_steps(today)
    total_steps += steps
    print(f"{today}: {steps} steps")
    today -= datetime.timedelta(days=1)

# Display the total steps for the last 7 days
print(f"Total steps in the last 7 days: {total_steps} steps")
