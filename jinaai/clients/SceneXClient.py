from .HTTPClient import HTTPClient

class SceneXClient(HTTPClient):
    def __init__(self, headers=None):
        baseUrl = 'https://us-central1-causal-diffusion.cloudfunctions.net'
        defaultHeaders = { 
            'Content-Type': 'application/json',
        }
        mergedHeaders = defaultHeaders.update(headers)
        super().__init__(baseUrl=baseUrl, headers=defaultHeaders)

    def from_array(self, input, options=None):
        return {
            'data': [
                {
                    'image': i,
                    'features': [],
                    **(options or {})
                }
                for i in input
            ]
        }

    def from_string(self, input, options=None):
        return {
            'data': [
                {
                    'image': input,
                    'features': [],
                    **(options or {})
                }
            ]
        }

    def to_simplified_output(self, output):
        if not output.get('result') or any(x.get('text') != '' for x in output['result']) is False:
            raise Exception('Remote API Error, bad output: {}'.format(json.dumps(output)))
        return {
            'results': [
                {
                    'output': r.get('text'),
                    'i18n': r.get('i18n')
                }
                for r in output['result']
            ]
        }

    def describe(self, data, options = None):
        raw_output = self.post('/describe', data)
        simplified_output = self.to_simplified_output(raw_output)
        if options and 'raw' in options:
            simplified_output['raw'] = raw_output
        return simplified_output

