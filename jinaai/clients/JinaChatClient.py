from .HTTPClient import HTTPClient
from ..utils import is_base64, is_url, omit


class JinaChatClient(HTTPClient):
    def __init__(self, headers=None, options=None, baseUrl='https://api.chat.jina.ai/v1/chat'):
        defaultHeaders = { 
            'Content-Type': 'application/json',
        }
        mergedHeaders = defaultHeaders.update(headers)
        super().__init__(baseUrl=baseUrl, headers=defaultHeaders, options=options)

    def from_array(self, input, options=None):
        return {
            'messages': [
                {
                    'content': i,
                    **((options and options.get("image") and (is_url(options['image']) or is_base64(options['image'])) and { 'image': options['image'] }) or {}),
                    'role': 'user',
                    **(omit(options, 'image'))
                }
                for i in input
            ],
            **(omit(options, 'image'))
        }

    def from_string(self, input, options=None):
        return {
            'messages': [
                {
                    'content': input,
                    **((options and options.get("image") and (is_url(options['image']) or is_base64(options['image'])) and { 'image': options['image'] }) or {}),
                    'role': 'user',
                    **(omit(options, 'image'))
                }
            ],
            **(omit(options, 'image'))
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

    def stream(self, data, options = None):
        return self.post('/completions', data, False)
