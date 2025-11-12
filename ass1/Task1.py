total_seconds = int(input("Input a time in seconds: "))
hours = total_seconds // 3600
remining_hours = total_seconds % 3600
minutes = remining_hours // 60
remining_minutes = remining_hours % 60
seconds = remining_hours % 60
print(f"The time on Earth is {hours}hours, {minutes}minutes and {seconds}seconds")