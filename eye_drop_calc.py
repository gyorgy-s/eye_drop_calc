# # recevive 3 ints as an input : 
# first the start time
# second the end time 
# third the total number of drops in the timeframe
# start and end time represent one drop each from the desired amount

from datetime import datetime

start = ""
end = ""
drop_cnt = 0


# getting user inputs, checking format validity
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

# separating hours and minutes
start_time = [int(start[0] + start[1]), int(start[2] + start[3])]
end_time = [int(end[0] + end[1]), int(end[2] + end[3])]

# converting the start and end time to "a float hour" format
start_as_hour = start_time[1] / 60 + start_time[0]
end_as_hour = end_time[1] / 60 + end_time[0]

# calculating the intervals for the drops
drop_interval = (end_as_hour - start_as_hour) / (drop_cnt -1)

# drop_cnt times: prints the current date and the calculated times for the drops, converting back to HH:MM format
for i in range(drop_cnt):
    hour = int(start_as_hour)
    minutes = int((start_as_hour % hour) * 60)
    print("{0} \t {1:>2}:{2:02}".format(datetime.today().date(), hour, minutes))
    start_as_hour += drop_interval
