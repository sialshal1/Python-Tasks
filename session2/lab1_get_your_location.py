"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    data = requests.get("https://ipinfo.io/json")
    return data.text
    
    """Write your solution here. Don't forget to return the result at the end."""


if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"


