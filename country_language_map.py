from mapping import mapping


def get_languages(country_code):
    """
    Function to get language code for the given country code.
    """

    return mapping[country_code]
