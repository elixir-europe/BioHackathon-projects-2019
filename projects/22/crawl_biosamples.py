import json

import requests

import config

request_timeout = 50


def main():
    # save_samples(project="FAANG")
    save_samples()


# Why we are not using multi-threading?
# BioSample uses Solr cursor to retrieve next set of samples in a page.
# If we use page, skip instead of using this cursor, Biosamples can time-out
def save_samples(limit=0, project=""):
    sample_count = 0

    with open(config.output_file, "w") as output:
        output.write("[\n")

    with open(config.output_file, "a") as output:
        url = config.biosamples_url + "?cursor=*&size=1000"
        if project != "":
            url = url + "&filter=attr:project:" + project

        print("Saving samples from: " + url)
        first = True
        while url != "" and (limit == 0 or limit > sample_count):
            samples, url = get_samples(url)

            for sample in samples:
                sample_count = sample_count + 1
                del sample["_links"]

                if first:
                    first = False
                else:
                    output.write(",\n")
                output.write(json.dumps(sample, indent=4))

                if sample_count % 5000 == 0:
                    print("Processed sample count: " + str(sample_count))

        output.write("\n]")
        print("Total samples collected: " + str(sample_count))


def get_samples(url):
    response = requests.get(url, timeout=request_timeout)
    samples = []
    if response.status_code == requests.codes.ok:
        json_output = response.json()
        if "_embedded" in json_output:
            samples = json_output["_embedded"]["samples"]

        if "next" in json_output["_links"]:
            url = json_output["_links"]["next"]["href"]
        else:
            url = ""
    else:
        print("invalid response code from biosamples")
        response.raise_for_status()

    return samples, url


if __name__ == "__main__":
    main()
