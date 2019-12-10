from textminingservice_biokb import logger


def standardise_underscored_entity_code(entity_code: str) -> str:
    return entity_code.replace(':', '_', 1)


def standardise_entity_type(entity_type: str) -> str:
    if entity_type is not None:
        return entity_type.split('#')[-1]
    return entity_type


def uri_to_entity_code(uri: str) -> str:
    """Translates URIs such as http://lcsb.uni.lu/biokb/entities/BTO_0001043 to BTO:0001043
    Replaces only the first underscore with colon.

    Arguments:
        uri {str} -- [description]

    Returns:
        str -- [description]
    """
    return uri.split('/')[-1].replace('_', ':', 1)


# https: // bitbucket.org/larsjuhljensen/tagger/src/default/
reflect_types = {
    -1: 'http://lcsb.uni.lu/biokb#Chemical',
    -3: 'http://lcsb.uni.lu/biokb#Protein',
    -21: 'http://lcsb.uni.lu/biokb#BiologicalProcess',
    -22: 'http://lcsb.uni.lu/biokb#CellularComponent',
    -23: 'http://lcsb.uni.lu/biokb#MolecularFunction',
    -25: 'http://lcsb.uni.lu/biokb#Tissue',
    -26: 'http://lcsb.uni.lu/biokb#Disease',
}


def reflect_type_to_biokb(entity_type: int) -> str:
    if entity_type > 0:
        return 'http://lcsb.uni.lu/biokb#Protein'
    translated = reflect_types.get(entity_type, None)
    if translated is None:
        logger.warning(f'Type {entity_type} not found for BioKB.')
    return translated
