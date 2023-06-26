from .HTTPClient import HTTPClient
from ..utils import is_base64, is_url


class ChatCatClient(HTTPClient):
    def __init__(self, headers=None):
        baseUrl = 'https://api-dyzugixgtq-uc.a.run.app/v1/chat'
        defaultHeaders = { 
            'Content-Type': 'application/json',
        }
        mergedHeaders = defaultHeaders.update(headers)
        super().__init__(baseUrl=baseUrl, headers=defaultHeaders)

    def from_array(self, input, options=None):
        return {
            'messages': [
                {
                    'content': i,
                    **(((is_url(i) or is_base64(i)) and { 'image': i }) or {}),
                    'role': 'user',
                    **(options or {})
                }
                for i in input
            ],
            **(options or {})
        }

    def from_string(self, input, options=None):
        return {
            'messages': [
                {
                    'content': input,
                    **(((is_url(input) or is_base64(input)) and { 'image': input }) or {}),
                    'role': 'user',
                    **(options or {})
                }
            ],
            **(options or {})
        }

    def to_simplified_output(self, output):
        if 'choices' not in output or len(output['choices']) < 1 or output['choices'][0]['message']['content'] == '':
            raise Exception('Remote API Error, bad output: ' + str(output))
        return {
            'output': output['choices'][0]['message']['content'],
            'chatId': output['chatId']
        }

    def generate(self, data, options = None):
        raw_output = self.post('/completions', data)
        simplified_output = self.to_simplified_output(raw_output)
        if options and 'raw' in options:
            simplified_output['raw'] = raw_output
        return simplified_output
