# scripts/fetch_contributions.py
import json
import requests
from bs4 import BeautifulSoup

def fetch(username="sakethreddy0302"):
    url = f"https://github.com/users/{username}/contributions"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    days = []
    
    for cell in soup.find_all("td", class_="ContributionCalendar-day"):
        date = cell.get("data-date")
        level = cell.get("data-level", "0")
        if date:
            days.append({"date": date, "level": int(level)})
            
    with open("data/contributions.json", "w") as f:
        json.dump(days, f, indent=2)
    print("Contributions saved to data/contributions.json")

if __name__ == "__main__":
    fetch()