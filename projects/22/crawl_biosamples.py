import requests

from config_params import Configurations

request_timeout = 50


class BioSamplesClient:
    def __init__(self, page_size=1000, filters=[]):
        self.config = Configurations()
        self.filters = filters
        self.page_size = page_size

        self.page_url = self.config.biosamples_url + "?cursor=*&size=" + str(page_size)
        for f in filters:
            self.page_url += f.build_filter()

        print("Biosamples client initiated for URL: " + self.page_url)

    def get_next_page(self):
        samples, self.page_url = get_samples(self.page_url)
        return samples


class BioSamplesSearchFilter:
    def __init__(self, filter_type, filter_label, filter_value):
        self.filter_type = filter_type
        self.filter_label = filter_label
        self.filter_value = filter_value

    def build_filter(self):
        return "&filter=" + self.filter_type + ":" + self.filter_label \
               + (":" + self.filter_value if self.filter_value else "")


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
