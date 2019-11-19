def uri_to_code(uri: str) -> str:
    """Translates URIs such as http://lcsb.uni.lu/biokb/entities/BTO_0001043 to BTO_0001043

    Arguments:
        uri {str} -- [description]

    Returns:
        str -- [description]
    """
    return uri.split('/')[-1]
