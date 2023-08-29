import numpy as np

def welcome_guest(guest_info):
    name, time = guest_info
    return f"Welcome to Festivus {name}... You're {time} min late."

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
#  Each guest, for whatever reason, has decided to show up to the party in 10-minute increments. For example,
#  Jerry shows up to Festivus 10 minutes into the party's start time,
#  Kramer shows up 20 minutes into the party, and so on and so forth.

# Create a list of arrival times
arrival_times = [*range(10, 60, 10)]

print(arrival_times)

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

print(new_times)

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i], time) for i, time in enumerate(new_times)]
print(guest_arrivals)

# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')