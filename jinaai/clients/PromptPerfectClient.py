from .HTTPClient import HTTPClient
from ..utils import is_base64, is_url

class PromptPerfectClient(HTTPClient):
    def __init__(self, headers=None, options=None):
        baseUrl = 'https://api.promptperfect.jina.ai'
        defaultHeaders = { 
            'Content-Type': 'application/json',
        }
        mergedHeaders = defaultHeaders.update(headers)
        super().__init__(baseUrl=baseUrl, headers=defaultHeaders, options=options)

    def from_array(self, input, options=None):
        return {
            'data': [
                {
                    **(((not is_url(i) and not is_base64(i)) and { 'prompt': i }) or {}),
                    **(((is_url(i) or is_base64(i)) and { 'imagePrompt': i }) or {}),
                    'targetModel': 'chatgpt',
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
                    **(((not is_url(input) and not is_base64(input)) and { 'prompt': input }) or {}),
                    **(((is_url(input) or is_base64(input)) and { 'imagePrompt': input }) or {}),
                    'targetModel': 'chatgpt',
                    'features': [],
                    **(options or {})
                }
            ]
        }

    def to_simplified_output(self, output):
        if not output.get('result') or any(x.get('promptOptimized') != '' for x in output['result']) is False:
            raise Exception('Remote API Error, bad output: {}'.format(json.dumps(output)))
        return {
            'results': [
                {
                    'output': r.get('promptOptimized'),
                }
                for r in output['result']
            ]
        }

    def optimize(self, data, options = None):
        raw_output = self.post('/optimizeBatch', data)
        simplified_output = self.to_simplified_output(raw_output)
        if options and 'raw' in options:
            simplified_output['raw'] = raw_output
        return simplified_output

