import datetime

# dt now
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# to README.md
text_to_write = f"Updated on {current_time}."

# open > w README.md 
with open("README.md", "w") as file:
    file.write(text_to_write)
