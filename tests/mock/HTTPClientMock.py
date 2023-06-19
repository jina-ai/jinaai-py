from unittest.mock import patch
import json
import time

def loadJsonResponse(filename):
    with open("mock/responses/" + filename, "r") as file:
        return json.load(file)

AuthKOResponse = loadJsonResponse("Auth.KO.response.json")
NotImplementedResponse = loadJsonResponse("NotImplemented.response.json")

def SceneXResponse(input):
    return {
        'result': [
            {
                'id': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa' + str(i),
                'image': e['image'],
                'features': e['features'],
                'uid': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa' + str(i),
                'algorithm': e.get('algorithm', 'Aqua'),
                'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
                'userId': 'zoyqq4zkwdZLiBgH0eyhx4fcN9b2',
                'createdAt': int(time.time() * 1000),
                'i18n': {l: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.' for l in e.get('languages', ['en'])}
            }
            for i, e in enumerate(input["data"])
        ]
    }

def RationaleResponse(data):
    return NotImplementedResponse

def PromptPerfectResponse(input):
    return {
        'result': [
            {
                'prompt': e.get('prompt') or e.get('imagePrompt') or '',
                'imagePrompt': e.get('imagePrompt') or None,
                'targetModel': e['targetModel'],
                'features': e['features'],
                'iterations': e.get('iterations', 1),
                'previewSettings': e.get('previewSettings', {}),
                'previewVariables': e.get('previewVariables', {}),
                'timeout': e.get('timeout', 20000),
                'targetLanguage': e.get('target_language'),
                'promptOptimized': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
                'credits': 1,
                'language': e.get('target_language', 'en'),
                'intermediateResults': [{
                    'promptOptimized': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
                    'explain': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.'
                }],
                'explain': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec convallis ipsum est, et iaculis lacus tincidunt eget. Sed dictum diam ex, eget aliquam urna porta a.',
                'createdAt': int(time.time() * 1000),
                'userId': 'zoyqq4zkwdZLiBgH0eyhx4fcN9b2',
                'id': 'aaaaaaaaaaaaaaaaaaaaaaaaaaa' + str(i)
            }
            for i, e in enumerate(input["data"])
        ]
    }

def ChatCatResponse(data):
    return NotImplementedResponse

def hasAuthHeader (headers):
    if "x-api-key" in headers and headers["x-api-key"] != "":
        return True
    if "authorization" in headers and headers["authorization"] != "":
        return True
    return False

def post(self, url, data):
    if hasAuthHeader(self.headers) == False:
        responseData = AuthKOResponse
    else:
        if url == "/describe":
            responseData = SceneXResponse(data)
        elif url == "/analysisApi":
            responseData = RationaleResponse(data)
        elif url == "/optimizeBatch":
            responseData = PromptPerfectResponse(data)
        elif url == "/completion":
            responseData = ChatCatResponse(data)
        else:
            responseData = NotImplementedResponse
    if "error" in responseData:
        raise Exception(responseData["error"])
    return responseData

def mock_post_method(xClient):
    return patch.object(xClient.__class__, "post", post)