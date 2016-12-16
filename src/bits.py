
import requests

RANDOM_ORG_QUOTA_API = 'https://www.random.org/quota/'
RANDOM_ORG_INTEGER_API = 'https://www.random.org/integers/'

class Failure(Exception):
    pass

class RandomOrg(object):
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'user-agent': 'stelminator@gmail.com'})

    def get_bits(self, num_bits):
        return ''

    def get_integers(self, num = 1, min_int = 1, max_int = 2, col = 1, base = 16, format_return='plain', rnd='1'):
        ints = self.session.get(RANDOM_ORG_INTEGER_API, params = {
            'num' : str(num),
            'min' : str(min_int),
            'max' : str(max_int),
            'col' : str(col),
            'base' : str(base),
            'format' : str(format_return),
            'rnd' : str(rnd)
            })
        # break into pieces, filter empties, parse as hex
        if 200 != ints.status_code:
            raise Failure(ints)
        try:
            vals = [int(y, 16) for y in [x.strip() for x in ints.content.strip().split()] if len(y)]
        except Exception as e:
            return ints
        return vals

    def get_and_save_bytes(self, num_bytes, directory='.'):
        pass


    def quota_remaining(self):
        resp = self.session.get(RANDOM_ORG_QUOTA_API, params=dict(format='plain'))
        return int(resp.content.strip())