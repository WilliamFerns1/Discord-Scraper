import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv
import os
import json

invite_code = input("Discord server: (name, id, or url): ")
invite_code = invite_code.split("/")[-1].replace("/", "")

url = "https://discord.com/api/v8/invites/" + invite_code

querystring = {"with_counts": "true"}

payload = ""
headers = {
    # Your headers here
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
name = response.json()["code"]
member_count = response.json()["approximate_member_count"]
online_count = response.json()["approximate_presence_count"]

print("Server Name:")
print(name)
print("Member Count:")
print(member_count)
print("Current Online Users:")
print(online_count)

# Get Server ID:
url = "https://discord.com/api/v9/invites/" + invite_code
querystring = {"with_counts": "true", "with_expiration": "true"}
payload = ""
headers = {
    # Your headers here
}
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
server_id = response.json()["guild"]["id"]
print("Server ID:")
print(server_id)

# Queries:
channel = input("What channel do you want to get the queries for? (format: #generate-, or #generate-1): ")

# Get the current date
current_date = datetime.now()

# Calculate one day ago by subtracting one day from the current date
one_day_ago = current_date - timedelta(days=1)

# Format the date as "YYYY-MM-DD"
formatted_date = one_day_ago.strftime("%Y-%m-%d")

# Build the query search string
query_search = f"in:{channel} after:{formatted_date}"
print("Query Search:")
print(query_search)

print(f"Getting Results for {channel}...\n")
firefox_profile_path = 'C:/Users/willf/AppData/Roaming/Mozilla/Firefox/Profiles/25blhvso.DiscordProfile'

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument(f'--profile={firefox_profile_path}')
# Create a new instance of the Firefox driver with the custom profile
driver = webdriver.Firefox(options=firefox_options)
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(50)

driver.get(f"https://discord.com/channels/{server_id}")

search_button = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/section/div/div[2]/div[5]/div/div/div[1]/div[2]/div")
    )
)
search_button.click()

# Send the search query
for character in query_search:
    search_button.send_keys(character)
    time.sleep(0.1)

search_button.send_keys(Keys.RETURN)

results_container = driver.find_element(by="xpath", value="/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div/section/header/div[1]/div")
time.sleep(2)
queries_results = results_container.text

while True:
    if queries_results == "Searching…":
        results_container = driver.find_element(by="xpath", value="/html/body/div/1/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div/section/header/div[1]/div")
        time.sleep(random.uniform(3.0, 5.0))
        queries_results = results_container.text

    else:
        break
# Display queries_results
print("Queries Results:")
if queries_results == "No Results":
    queries_results = 0
else:
    # Extract the entire number from the results
    import re
    matches = re.findall(r'\d+', queries_results)
    queries_results = int(''.join(matches))

print(queries_results)

driver.quit()

# Sign-ups by day

# Get the current date
current_date = datetime.now()

# Calculate one day ago by subtracting one day from the current date
one_day_ago = current_date - timedelta(days=1)

# Format the date as "YYYY-MM-DD"
formatted_date = one_day_ago.strftime("%Y-%m-%d")



# Build the query search string for sign-ups
query_search = f"in:#welcome after:{formatted_date}"
print("Sign-ups Query Search:")
print(query_search)

print("Getting Sign-ups Results...")

firefox_profile_path = 'C:/Users/willf/AppData/Roaming/Mozilla/Firefox/Profiles/25blhvso.DiscordProfile'

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument(f'--profile={firefox_profile_path}')
# Create a new instance of the Firefox driver with the custom profile
driver = webdriver.Firefox(options=firefox_options)
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(50)

driver.get(f"https://discord.com/channels/{server_id}")

search_button = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/section/div/div[2]/div[5]/div/div/div[1]/div[2]/div")
    )
)
search_button.click()

# Send the search query for sign-ups
for character in query_search:
    search_button.send_keys(character)
    time.sleep(0.1)

search_button.send_keys(Keys.RETURN)

results_container = driver.find_element(by="xpath", value="/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div/section/header/div[1]/div")
time.sleep(2)
daily_sign_ups_results = results_container.text

while True:
    if daily_sign_ups_results == "Searching…":
        results_container = driver.find_element(by="xpath", value="/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div/section/header/div[1]/div")
        time.sleep(random.uniform(3.0, 5.0))
        daily_sign_ups_results = results_container.text
    else:
        break

# Display daily_sign_ups_results
print("Sign-ups by Day Results:")
print("Queries Results:")
if daily_sign_ups_results == "No Results":
    daily_sign_ups_results = 0
else:
    # Extract the entire number from the results
    import re
    matches = re.findall(r'\d+', daily_sign_ups_results)
    daily_sign_ups_results = int(''.join(matches))

print(daily_sign_ups_results)
driver.quit()

# Lets try it on another server.


# Format the date as "YYYY/MM/DD"
formatted_date = one_day_ago.strftime("%Y/%m/%d")

server = {
    "name": name,
    "date": formatted_date,
    "member_count": member_count,
    "online_count": online_count,
    "server_id": server_id,
    "queries": queries_results,
    "daily_sign_ups": daily_sign_ups_results,
}

# Save the server data in a JSON file
# Save the server data in a JSON file
json_filename = "server_data.json"
json_data = {}  # Initialize an empty dictionary

# Check if the JSON file already exists
if os.path.isfile(json_filename):
    # If the JSON file already exists, load its data
    with open(json_filename, 'r') as json_file:
        json_data = json.load(json_file)

# Append the data for the current server or create a new list if it doesn't exist
if server["name"] in json_data:
    json_data[server["name"]].append(server)
else:
    json_data[server["name"]] = [server]

# Write the updated data back to the JSON file
with open(json_filename, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"Data saved to {json_filename}")


# Create or update the CSV file based on the JSON data
csv_filename = "server_data.csv"
csv_headers = ["Server Name", "Date", "Total Number of Users in Server", "Current Online Users", "Sign ups by day", "Queries"]

# Read existing data from the JSON file
existing_data = {}
if os.path.isfile(json_filename):
    with open(json_filename, 'r') as json_file:
        existing_data = json.load(json_file)

# Write the data to the CSV file
with open(csv_filename, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(csv_headers)

    for server_name, server_data_list in existing_data.items():
        for server_data in server_data_list:
            date = server_data["date"]
            writer.writerow([server_data["name"], date, server_data["member_count"], server_data["online_count"], server_data["daily_sign_ups"], server_data["queries"]])

print(f"Data saved to {csv_filename}")
