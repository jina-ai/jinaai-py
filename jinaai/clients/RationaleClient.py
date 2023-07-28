from .HTTPClient import HTTPClient
from ..utils import is_base64, is_url

MAXLEN = 300

class RationaleClient(HTTPClient):
    def __init__(self, headers=None, options=None):
        baseUrl = 'https://us-central1-rationale-ai.cloudfunctions.net'
        defaultHeaders = { 
            'Content-Type': 'application/json',
        }
        mergedHeaders = defaultHeaders.update(headers)
        super().__init__(baseUrl=baseUrl, headers=defaultHeaders, options=options)

    def from_array(self, input, options=None):
        return {
            'data': [
                {
                    'decision': i[:MAXLEN],
                    **(options or {})
                }
                for i in input
            ]
        }

    def from_string(self, input, options=None):
        return {
            'data': [
                {
                    'decision': input[:MAXLEN],
                    **(options or {})
                }
            ]
        }

    def to_simplified_output(self, output):
        if 'result' not in output or 'result' not in output['result']:
            raise Exception('Remote API Error, bad output: ' + json.dumps(output))
        return {
            'results': [
                {
                    'proscons': r['keyResults'] if r['analysis'] == 'proscons' else None,
                    'swot': r['keyResults'] if r['analysis'] == 'swot' else None,
                    'multichoice': r['keyResults'] if r['analysis'] == 'multichoice' else None,
                    'outcomes': r['keyResults'] if r['analysis'] == 'outcomes' else None,
                }
                for r in output['result']['result']
            ]
        }

    def decide(self, data, options = None):
        raw_output = self.post('/analysisApi', data)
        simplified_output = self.to_simplified_output(raw_output)
        if options and 'raw' in options:
            simplified_output['raw'] = raw_output
        return simplified_output

