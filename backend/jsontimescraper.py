import json
import datetime

#read the json file under raw_data folder

with open('raw_data\\timetable.json') as json_file:
    json_data = json.load(json_file)
    
#print(json_data)
all_data = []

course_1 = json_data[0]
campus = course_1['campus']
test_time = course_1['lec'][0]['times'][0]['time']

print(campus)
print(test_time)

#parse 8:00 AM - 9:00 AM to get start time and end time
start_time = test_time.split('-')[0].strip()
end_time = test_time.split('-')[1].strip()
print(start_time)
print(end_time)

#use datetime library to convert time to datetime object

start_time = datetime.datetime.strptime(start_time, '%I:%M %p')
end_time = datetime.datetime.strptime(end_time, '%I:%M %p')
print(start_time)
print(end_time)
duration = end_time - start_time
print(duration)
#convert duration to minutes
duration_in_m = int(duration.total_seconds()/60)
print(duration_in_m)



for course in json_data:
    for lec in course['lec']:
        for time in lec['times']:
            
            start_time = time['time'].split('-')[0].strip()
            end_time = time['time'].split('-')[1].strip()
            start_time = datetime.datetime.strptime(start_time, '%I:%M %p')
            end_time = datetime.datetime.strptime(end_time, '%I:%M %p')
            duration = end_time - start_time
            duration_in_m = int(duration.total_seconds()/60)
            
            #format start and end time to 24 hour format and convert to string
            start_time = start_time.strftime('%H:%M')
            end_time = end_time.strftime('%H:%M')
            
            all_data.append([course['code'], lec['section'],time['day'], start_time, end_time, str(duration_in_m)])
    for tut in course['tut']:
        for time in tut['times']:
            start_time = time['time'].split('-')[0].strip()
            end_time = time['time'].split('-')[1].strip()
            start_time = datetime.datetime.strptime(start_time, '%I:%M %p')
            end_time = datetime.datetime.strptime(end_time, '%I:%M %p')
            duration = end_time - start_time
            duration_in_m = int(duration.total_seconds()/60)
            start_time = start_time.strftime('%H:%M')
            end_time = end_time.strftime('%H:%M')
            all_data.append([course['code'], lec['section'],time['day'], start_time, end_time, str(duration_in_m)])

print(all_data)

#store each entry in all_data into a csv file
#q: how to convert datetime object to string?
#a: use strftime() method

with open('timetable.csv', 'w') as csv_file:
    for entry in all_data:
        csv_file.write(','.join(entry) + '\n')
