# Recevive 3 ints as an input : 
# First the start time.
# Second the end time.
# Third the total number of drops in the timeframe.
# Start and end time represent one drop each from the desired amount.

from datetime import datetime
import os

start = ""
end = ""
drop_cnt = 0
output = []
save_yn = ""

# Getting user inputs, checking format validity.
while len(start) != 4:
    start = input("Enter the time of the first drop of the day in HHMM format: ")
    try:
        int(start)
    except:
        start = ""

while len(end) != 4:
    end = input("Enter the time of the last drop of the day in HHMM format: ")
    try:
        int(end)
    except:
        end = ""
while not drop_cnt:
    try:
        drop_cnt = int(input("Enter the number drops for the day (the toal numbar, including the first and last drops specified previously): "))
    except:
        drop_cnt = 0

# Separating hours and minutes.
start_time = [int(start[0] + start[1]), int(start[2] + start[3])]
end_time = [int(end[0] + end[1]), int(end[2] + end[3])]

# Converting the start and end time to "a float hour" format.
start_as_hour = start_time[1] / 60 + start_time[0]
end_as_hour = end_time[1] / 60 + end_time[0]

# Calculating the intervals for the drops.
drop_interval = (end_as_hour - start_as_hour) / (drop_cnt -1)

# Drop_cnt times: prints the current date and the calculated times for the drops, converting back to HH:MM format.
for i in range(drop_cnt):
    hour = int(start_as_hour)
    minutes = int((start_as_hour % hour) * 60)
    output.append("{0} \t {1:>2}:{2:02}".format(datetime.today().date(), hour, minutes))
    print("{0} \t {1:>2}:{2:02}".format(datetime.today().date(), hour, minutes))
    start_as_hour += drop_interval

# print(os.getcwd())
# print(os.path.dirname(os.path.realpath(__file__)))

# Ask for user input if this should be written to a file, chaek for validity.
save_yn = input("Would you like to write these in a file? y / n\n").lower()
while save_yn not in ("y", "n"):
    save_yn = input("Would you like to write these in a file? y / n\n").lower()
if save_yn == "y":
# Check .py location, append to the file "time_to_drop.txt"
    with open(os.path.dirname(os.path.realpath(__file__)) + "\\time_to_drop.txt","a") as f:
        f.write("\n".join(output))
        f.write("\n")
        f.close()

# print("start time: ", start_time)
# print ("start as hour: ", start_as_hour)
# print("end time:", end_time)
# print("end as hour: ", end_as_hour)
# print("drop count: ", drop_cnt)
# print("drop interval: ", drop_interval)
