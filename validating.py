import validators


def check_url(link):
    if validators.url(link):
        return link
