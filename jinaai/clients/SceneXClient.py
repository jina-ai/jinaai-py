from .HTTPClient import HTTPClient

def autoFillFeatures(options=None):
    features = options.get('features', []) if options else []
    if options and 'question' in options and 'question_answer' not in features:
        features.append('question_answer')
    return features

class SceneXClient(HTTPClient):
    def __init__(self, headers=None, options=None):
        baseUrl = 'https://api.scenex.jina.ai/v1'
        defaultHeaders = { 
            'Content-Type': 'application/json',
        }
        mergedHeaders = defaultHeaders.update(headers)
        super().__init__(baseUrl=baseUrl, headers=defaultHeaders, options=options)

    def from_array(self, input, options=None):
        return {
            'data': [
                {
                    'image': i,
                    'features': autoFillFeatures(options),
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
                    'features': autoFillFeatures(options),
                    **(options or {})
                }
            ]
        }

    def to_simplified_output(self, output):
        if not output.get('result') or any(x.get('text') and x.get('text') != '' for x in output['result']) is False:
            raise Exception('Remote API Error, bad output: {}'.format(json.dumps(output)))
        return {
            'results': [
                {
                    'output': r['answer'] if 'answer' in r and r['answer'] is not None else r['text'],
                    'i18n': r['i18n']
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

