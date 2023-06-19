import requests

class HTTPClient:
    def __init__(self, baseUrl, headers=None):
        self.baseUrl = baseUrl
        self.headers = headers if headers else {}

    def setHeaders(self, headers):
        self.headers = headers

    def addHeader(self, header):
        self.headers.update(header)

    def get(self, url):
        response = requests.get(self.baseUrl + url, headers=self.headers)
        responseData = response.json()
        return responseData

    def post(self, url, data):
        response = requests.post(self.baseUrl + url, json=data, headers=self.headers)
        responseData = response.json()
        if "error" in responseData:
            raise Exception(responseData["error"])
        return responseData

    def put(self, url, data):
        response = requests.put(self.baseUrl + url, headers=self.headers)
        responseData = response.json()
        return responseData

    def delete(self, url):
        response = requests.delete(self.baseUrl + url, headers=self.headers)
        responseData = response.json()
        return responseData
