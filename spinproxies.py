import requests


class SpinProxies:
    '''Wrapper for the SpinProxies API.
    https://spinproxies.com/
    '''
    def __init__(self, params):
        self.params = params

    def _send_req(self, url, params):
        try:
            r = requests.get(url, params=params, timeout=8)
        except:
            return None
        return r.text

    def proxy_list(self):
        base_url = 'https://spinproxies.com/api/v1/proxylist'
        keys = ['key', 'format', 'type', 'protocols', 'country_code', \
                'new', 'limit']
        p = {}
        for k in keys:
            if k in self.params.keys():
                p[k] = self.params[k]
        return self._send_req(base_url, p)

    def proxy_rotate(self):
        base_url = 'https://spinproxies.com/api/v1/proxyrotate'
        keys = ['key', 'format', 'type', 'protocols', 'country_code', \
                'new']
        p = {}
        for k in keys:
            if k in self.params.keys():
                p[k] = self.params[k]
        return self._send_req(base_url, p)

