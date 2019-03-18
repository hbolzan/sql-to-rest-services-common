import re


def clear_punctuation(document):
    """Remove all punctuation signals from document."""
    return re.sub('\D', '', str(document))
