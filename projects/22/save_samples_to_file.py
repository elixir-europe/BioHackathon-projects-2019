"""
Why we are not using multi-threading?
BioSample uses Solr cursor to retrieve next set of samples in a page.
If we use page, skip instead of using this cursor, Biosamples can time-out
"""

import json

from config_params import Configurations
from crawl_biosamples import BioSamplesClient, BioSamplesSearchFilter


def main():
    config = Configurations()
    # search_filters = [BioSamplesSearchFilter("attr", "project", "HipSci")]
    search_filters = [BioSamplesSearchFilter("rel", "derived from", "")]

    load_and_save_samples_to_files(config, filters=search_filters)
    # save_samples_to_one_big_file(config, project="EBiSC")


def load_and_save_samples_to_files(config, filters):
    sample_count = 0
    file_no = 1
    max_sample_per_file = 100000

    biosamples_client = BioSamplesClient(filters=filters)

    filter_values = ""
    for f in filters:
        filter_values += f.filter_label + "=" + f.filter_value + "_"

    sample_list = []
    samples = biosamples_client.get_next_page()
    while len(samples) > 0:
        sample_list += samples
        sample_count += len(samples)
        samples = biosamples_client.get_next_page()

        if len(sample_list) >= max_sample_per_file:
            output_file_name = config.data_file_pattern + filter_values + str(file_no) + ".json"
            print("Sample count: " + str(sample_count) + ", flushing " + str(
                len(sample_list)) + " samples to: " + output_file_name)
            with open(output_file_name, "w") as data_file:
                data_file.write(json.dumps(sample_list, indent=4))

            file_no += 1
            sample_list = []

    output_file_name = config.data_file_pattern + filter_values + str(file_no) + ".json"
    print("Sample count: " + str(sample_count) + ", flushing " + str(
        len(sample_list)) + " samples to: " + output_file_name)
    with open(output_file_name, "w") as data_file:
        data_file.write(json.dumps(sample_list, indent=4))


def save_samples_to_one_big_file(config, limit=0, filters=[]):
    sample_count = 0
    biosamples_client = BioSamplesClient(filters=filters)

    with open(config.data_file, "w") as output:
        output.write("[\n")

    with open(config.data_file, "a") as output:
        first = True
        samples = biosamples_client.get_next_page()
        while len(samples) > 0 and (limit == 0 or limit > sample_count):
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

            samples = biosamples_client.get_next_page()

        output.write("\n]")
        print("Total samples collected: " + str(sample_count))


if __name__ == "__main__":
    main()
