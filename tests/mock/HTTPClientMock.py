from unittest.mock import patch
import json
import time
from .responses.SceneXResponse import SceneXResponse
from .responses.PromptPerfectResponse import PromptPerfectResponse
from .responses.RationaleResponse import RationaleResponse
from .responses.JinaChatResponse import JinaChatResponse

def loadJsonResponse(filename):
    with open("mock/responses/" + filename, "r") as file:
        return json.load(file)

AuthKOResponse = loadJsonResponse("Auth.KO.response.json")
NotImplementedResponse = loadJsonResponse("NotImplemented.response.json")

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
        elif url == "/completions":
            responseData = JinaChatResponse(data)
        else:
            responseData = NotImplementedResponse
    if "error" in responseData:
        raise Exception(responseData["error"])
    return responseData

def mock_post_method(xClient):
    return patch.object(xClient.__class__, "post", post)