import requests
import argparse
import json


def get_ip_info(ip_address):
    try:
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


def create_google_maps_link(loc):
    latitude, longitude = loc.split(",")
    return f"https://www.google.com/maps?q={latitude},{longitude}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IPアドレスの解析")
    parser.add_argument("-t", type=str, required=True, help="IP address")
    args = parser.parse_args()

    ip_info = get_ip_info(args.t)

    if isinstance(ip_info, dict):
        print(json.dumps(ip_info, indent=4, ensure_ascii=False))
    else:
        print(ip_info)

    if "loc" in ip_info:
        google_maps_link = create_google_maps_link(ip_info["loc"])
        print(f"Google Maps Link: {google_maps_link}")
