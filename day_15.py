import time 
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
hour = int(timestamp) # Yahan string ko number mein badla
timestamp = time.strftime('%M')
print(timestamp)    
timestamp = time.strftime('%S')
print(timestamp)
if hour < 12:
    print("Good Morning")
elif hour >= 12 and hour < 17:
    print("Good Afternoon")
else:
    print("Good Evening")