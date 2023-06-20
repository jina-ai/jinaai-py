from .clients.SceneXClient import SceneXClient
from .clients.PromptPerfectClient import PromptPerfectClient
from .clients.RationaleClient import RationaleClient
from .clients.ChatCatClient import ChatCatClient
from .utils import is_url, is_base64, image_to_base64

class JinaAI:
    def __init__(self, tokens={}):
        PPToken = f"token {tokens['promptperfect-token']}" if tokens else ''
        SXToken = f"token {tokens['scenex-token']}" if tokens else ''
        RAToken = f"token {tokens['rationale-token']}" if tokens else ''
        CCToken = f"Bearer {tokens['chatcat-token']}" if tokens else ''
        self.PPClient = PromptPerfectClient(headers = { "x-api-key": PPToken })
        self.SXClient = SceneXClient(headers = { "x-api-key": SXToken })
        self.RAClient = RationaleClient(headers = { "x-api-key": RAToken })
        self.CCClient = ChatCatClient(headers = { "authorization": CCToken })

    def decide(self, input, options=None):
        if isinstance(input, list):
            data = self.RAClient.from_array(input, options)
        elif isinstance(input, str):
            data = self.RAClient.from_string(input, options)
        else:
            data = input
        return self.RAClient.decide(data, options)

    def optimize(self, input, options=None):
        if isinstance(input, list):
            data = self.PPClient.from_array(input, options)
        elif isinstance(input, str):
            data = self.PPClient.from_string(input, options)
        else:
            data = input
        return self.PPClient.optimize(data, options)

    def describe(self, input, options=None):
        if isinstance(input, list):
            data = self.SXClient.from_array(input, options)
        elif isinstance(input, str):
            data = self.SXClient.from_string(input, options)
        else:
            data = input
        return self.SXClient.describe(data, options)

    def generate(self, input, options=None):
        if isinstance(input, list):
            data = self.CCClient.from_array(input, options)
        elif isinstance(input, str):
            data = self.CCClient.from_string(input, options)
        else:
            data = input
        return self.CCClient.generate(data, options)

    def generate_image(self):
        raise Exception("banner not implemented")

    class utils:
        @staticmethod
        def is_url(string):
            return is_url(string)
        @staticmethod
        def is_base64(string):
            return is_base64(string)
        @staticmethod
        def image_to_base64(file_path):
            return image_to_base64(file_path)