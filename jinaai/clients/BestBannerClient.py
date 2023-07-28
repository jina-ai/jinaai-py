from .HTTPClient import HTTPClient

class BestBannerClient(HTTPClient):
    def __init__(self, headers=None, options=None):
        baseUrl = 'https://api.bestbanner.jina.ai/v1'
        defaultHeaders = { 
            'Content-Type': 'application/json',
        }
        mergedHeaders = defaultHeaders.update(headers)
        super().__init__(baseUrl=baseUrl, headers=defaultHeaders, options=options)

    def from_array(self, input, options=None):
        return {
            'data': [
                {
                    'text': i,
                    **(options or {})
                }
                for i in input
            ]
        }

    def from_string(self, input, options=None):
        return {
            'data': [
                {
                    'text': input,
                    **(options or {})
                }
            ]
        }

    def to_simplified_output(self, output):
        if not output.get('result') or any(x.get('banners') and len(x['banners']) != 0 for x in output['result']) is False:
            raise Exception('Remote API Error, bad output: {}'.format(json.dumps(output)))
        return {
            'results': [
                {
                    'output': [
                        b['url'] for b in r['banners']
                    ]
                }
                for r in output['result']
            ]
        }

    def imagine(self, data, options = None):
        raw_output = self.post('/generate', data)
        simplified_output = self.to_simplified_output(raw_output)
        if options and 'raw' in options:
            simplified_output['raw'] = raw_output
        return simplified_output

