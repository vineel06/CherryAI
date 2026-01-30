import requests


def is_online() -> bool:
    """
    Reliable internet check using HTTP.
    """
    try:
        response = requests.get("https://www.google.com", timeout=3)
        return response.status_code == 200
    except requests.RequestException:
        return False
