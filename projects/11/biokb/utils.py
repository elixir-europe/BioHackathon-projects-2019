def standarise_underscored_entity_code(entity_code: str) -> str:
    return entity_code.replace(':', '_', 1)


def uri_to_entity_code(uri: str) -> str:
    """Translates URIs such as http://lcsb.uni.lu/biokb/entities/BTO_0001043 to BTO:0001043
    Replaces only the first underscore with colon.

    Arguments:
        uri {str} -- [description]

    Returns:
        str -- [description]
    """
    return uri.split('/')[-1].replace('_', ':', 1)
