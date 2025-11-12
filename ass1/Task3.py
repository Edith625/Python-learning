total_seconds = int(input("Input a time in seconds: "))
hours = total_seconds // 3600
remining_hours = total_seconds % 3600
minutes = remining_hours // 60
remining_minutes = remining_hours % 60
seconds = remining_hours % 60

seconds_per_minute = int(input("Input the number of seconds in a minute on Trisolaris: "))
minutes_per_hours = int(input("Input the number of minutes in an hour on Trisolaris: "))
trisolaris_seconds_per_minute = seconds_per_minute * minutes_per_hours
trisolaris_hours = total_seconds // trisolaris_seconds_per_minute
remining_trisolaris_hours = total_seconds % trisolaris_seconds_per_minute
trisolaris_minutes = remining_trisolaris_hours // seconds_per_minute
trisolaris_seconds = remining_trisolaris_hours % seconds_per_minute

waiting_time = int(input("Input a duration in seconds: "))
new_total_seconds = total_seconds + waiting_time
new_trisolaris_hours = new_total_seconds // trisolaris_seconds_per_minute
new_trisolaris_remining = new_total_seconds % trisolaris_seconds_per_minute
new_trisolaris_mintues = new_trisolaris_remining // seconds_per_minute
new_trisolaris_seconds = new_trisolaris_remining % seconds_per_minute

print(f"The time on Trisolaris after waiting is {new_trisolaris_hours} hours {new_trisolaris_mintues} minutes and {new_trisolaris_seconds} seconds.")

print(f"The on Trisolaris is {trisolaris_hours}trisolaris_hours, {trisolaris_minutes}trisolaris_minutes and {trisolaris_seconds}trisolaris_seconds")

print(f"The time on Earth is {hours}hours, {minutes}minutes and {seconds}seconds")