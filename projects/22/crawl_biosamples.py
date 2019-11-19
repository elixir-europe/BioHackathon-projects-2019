import json

import requests

import config

request_timeout = 50


def main():
    get_samples(cursor="*", size=100)


def get_samples(url="", cursor="*", size=20):
    params = {
        "cursor": cursor,
        "size": size,
        "filter": "attr:project:FAANG"
    }

    if url == "":
        response = requests.get(config.biosamples_url, params, timeout=request_timeout)
    else:
        response = requests.get(url, timeout=request_timeout)

    if response.status_code == requests.codes.ok:
        json_output = response.json()
        url = json_output["_links"]["next"]["href"]
        with open(config.output_file, "w") as output:
            output.write(json.dumps(json_output["_embedded"]["samples"], indent=4))
    else:
        print("invalid response code from biosamples")
        response.raise_for_status()

    return url


if __name__ == "__main__":
    main()
