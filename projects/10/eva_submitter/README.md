# EVA Submitter: From a BrAPI compliant Database to EVA submission format

## BrAPI to EVA mapping

A mapping between BrAPI and EVA has been made [here](../EVA_Submission_template_V1_1_3_mapping_to_BRAPI_v2.xlsx)

## Extraction and validation

The validation of the format uses the JSON validator using JSON Schemas available [here](https://github.com/FAIRsharing/mircat/blob/master/miappe/schema/biological_material_schema.json)
the Elixir JSON validator API is called with the previous JSON-Schema and the BRAPI-formatted Samples

## How to: install and plug BrAPI extractor on your database
