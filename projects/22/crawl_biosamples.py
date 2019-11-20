import json

import requests
from decouple import config

import neo_utils

request_timeout = 50


biosamples_url = config('biosamples_url')
output_file = config('data_file')


class BioSamplesCrawler:
    def __init__(self, page_size=1000, project=""):
        self.project = project
        self.page_size = page_size

        self.page_url = biosamples_url + "?cursor=*&size=" + str(page_size)
        if project != "":
            self.page_url += "&filter=attr:project:" + project

    def get_next_page(self):
        samples, self.page_url = get_samples(self.page_url)
        return samples


def main():
    # save_samples_to_one_big_file(project="FAANG")
    # save_samples_to_one_big_file()
    # load_and_save_samples_to_files(project="FAANG")
    load_and_save_samples_to_files()


# Why we are not using multi-threading?
# BioSample uses Solr cursor to retrieve next set of samples in a page.
# If we use page, skip instead of using this cursor, Biosamples can time-out
def save_samples_to_one_big_file(limit=0, project=""):
    sample_count = 0

    with open(output_file, "w") as output:
        output.write("[\n")

    with open(output_file, "a") as output:
        url = biosamples_url + "?cursor=*&size=1000"
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


def load_and_save_samples_to_files(project=""):
    sample_count = 0
    file_no = 1
    max_sample_per_file = 1000000

    url = biosamples_url + "?cursor=*&size=1000"
    if project != "":
        url = url + "&filter=attr:project:" + project

    sample_list = []
    while url != "":
        samples, url = get_samples(url)
        sample_list += samples
        sample_count += len(samples)

        if len(sample_list) >= max_sample_per_file:
            output_file_name = "data/samples_" + project + "_" + str(file_no) + ".json"
            print("Sample count: " + str(sample_count) + ", flushing " + str(len(sample_list)) + " samples to: " + output_file_name)
            with open(output_file_name, "w") as data_file:
                data_file.write(json.dumps(sample_list, indent=4))

            file_no += 1
            sample_list = []

    output_file_name = "data/samples_" + project + "_" + str(file_no) + ".json"
    print("Sample count: " + str(sample_count) + ", flushing " + str(len(sample_list)) + " samples to: " + output_file_name)
    with open(output_file_name, "w") as data_file:
        data_file.write(json.dumps(sample_list, indent=4))


def load_and_save_samples_to_db(project=""):
    sample_count = 0

    url = biosamples_url + "?cursor=*&size=1000"
    if project != "":
        url = url + "&filter=attr:project:" + project

    while url != "":
        samples, url = get_samples(url)
        sample_count += len(samples)

        if sample_count % 100000:
            print("Got " + str(sample_count) + " samples")

        neo_utils.save_samples(samples)


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


def get_samples_with_retry(url):
    samples = []
    try:
        samples, url = get_samples(url)
    except requests.exceptions.ReadTimeout:
        # todo add retry after some time
        print("Read timeout.")
    except requests.exceptions.HTTPError:
        # todo add retry after some time
        print("Internal server error. Server might be too busy")

    return samples, url


if __name__ == "__main__":
    main()
