from .HTTPClient import HTTPClient
import time

def autoFillFeatures(options=None):
    features = options.get('features', []) if options else []
    if options and 'question' in options and 'question_answer' not in features:
        features.append('question_answer')
    if options and 'json_schema' in options and 'json' not in features:
        features.append('json')
    return features

class SceneXClient(HTTPClient):
    def __init__(self, headers=None, options=None, baseUrl='https://api.scenex.jina.ai/v1'):
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
                    **({"video": i} if options and options.get("algorithm") == "Inception" else {}),
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
                    **({"video": input} if options and options.get("algorithm") == "Inception" else {}),
                    'features': autoFillFeatures(options),
                    **(options or {})
                }
            ]
        }

    def to_simplified_output(self, output):
        if not output.get('result') or any(x.get('image') or x.get('video') for x in output['result']) is False:
            raise Exception('Remote API Error, bad output: {}'.format(json.dumps(output)))
        return {
            'results': [
                {
                    'output': r['answer'] if 'answer' in r and r['answer'] is not None else (r['text'] if 'text' in r else 'Processing...'),
                    'i18n': r['i18n'] if "i18n" in r else None,
                    "tts": r["tts"] if "tts" in r else None,
                    "ssml": r["dialog"]["ssml"] if r.get("dialog") and "ssml" in r["dialog"] else None

                }
                for r in output['result']
            ]
        }

    def describe_video(self, output, options = None):
        for i, scene in enumerate(output["result"]):
            raw_output = None
            is_done = False
            while is_done is False:
                raw_output = self.get(f"/scene/{scene['id']}")
                if raw_output["result"]["data"]["status"] != "pending":
                    is_done = True
                time.sleep(10)
            if raw_output:
                output["result"][i] = raw_output["result"]["data"]
        return output

    def describe(self, data, options = None):
        raw_output = self.post('/describe', data)
        if options and 'algorithm' in options and options['algorithm'] == 'Inception':
            raw_output = self.describe_video(raw_output, options)
        simplified_output = self.to_simplified_output(raw_output)
        if options and 'raw' in options:
            simplified_output['raw'] = raw_output
        return simplified_output

