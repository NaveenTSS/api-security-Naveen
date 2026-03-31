

import os
import requests
from dotenv import load_dotenv

#Task 1 — Remove the Hardcoded API Key

load_dotenv(".env")

url="https://api.openweathermap.org/data/3.0/onecall?"
try:
    response=requests.get(
        url,
        params={"lat":"17.72' N","lon":"83.30","appid":os.environ.get("API_KEY")},
        timeout=15
    )

#Task 2 — Handle Rate Limiting Gracefully
    response.raise_for_status()

    data=response.json()    
except requests.exceptions.HTTPError as e:
    # The server responded, but with a bad status (e.g., 404, 500).
    print(f"HTTP error occurred: Request failed with status {response.status_code}")

except requests.exceptions.ConnectionError:
    # Could not reach the server at all (no internet, DNS issues, server down).
    print("Connection error: Could not reach the server. Check your internet connection.")

except requests.exceptions.Timeout:
    # We waited too long for a response and gave up.
    print("Timeout: The server took too long to respond.")

except requests.exceptions.RequestException as e:
    # Any other request-related error (a safe generic catch).
    print(f"Request error: {response.status_code}")

except Exception as e:
    # Any other unexpected error (e.g., DataFrame operations).
    print(f"Unexpected error: {response.status_code}")

#Task 3 — Protect User Privacy
    #print(f"Fetching weather for: {city}...")
    #Location data shouldn't be logged as the API takes only Latitudes and Longitudes but not city because it's wrong to expose the location of the user.

