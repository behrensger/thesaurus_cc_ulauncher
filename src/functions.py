import json
from urllib.request import urlopen, Request
from urllib.parse import urlencode


SEARCH_OPENTHESAURUS_URL = "https://www.openthesaurus.de/synonyme/search?format=application/json&"

def generate_url(search):
    return SEARCH_OPENTHESAURUS_URL + urlencode({"s": search})


def generate_synTerms(word):
    # make a request
    url = SEARCH_OPENTHESAURUS_URL + urlencode({"q": word})
    req = Request(url)

    # parse the response
    response = []
    with urlopen(req) as url:
        response = json.loads(url.read().decode()) or []

    terms = []
    for synsets in response.get('synsets', []):
        for term in synsets.get('terms', []):
            terms.append(term.get('term'))

    # prepare and return the found terms
    terms = list(set(terms))[0:6]  # first 6 elements of a unique list
    return terms
