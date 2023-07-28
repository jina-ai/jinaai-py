from .clients.SceneXClient import SceneXClient
from .clients.PromptPerfectClient import PromptPerfectClient
from .clients.RationaleClient import RationaleClient
from .clients.JinaChatClient import JinaChatClient
from .clients.BestBannerClient import BestBannerClient
from .utils import is_url, is_base64, image_to_base64

class JinaAI:
    def __init__(self, secrets={}):
        PPSecret = f"token {secrets['promptperfect-secret']}" if secrets and 'promptperfect-secret' in secrets else ''
        SXSecret = f"token {secrets['scenex-secret']}" if secrets and 'scenex-secret' in secrets else ''
        RASecret = f"token {secrets['rationale-secret']}" if secrets and 'rationale-secret' in secrets else ''
        CCSecret = f"Bearer {secrets['jinachat-secret']}" if secrets and 'jinachat-secret' in secrets else ''
        BBSecret = f"token {secrets['bestbanner-secret']}" if secrets and 'bestbanner-secret' in secrets else ''
        self.PPClient = PromptPerfectClient(headers = { "x-api-key": PPSecret })
        self.SXClient = SceneXClient(headers = { "x-api-key": SXSecret })
        self.RAClient = RationaleClient(headers = { "x-api-key": RASecret })
        self.CCClient = JinaChatClient(headers = { "authorization": CCSecret })
        self.BBClient = BestBannerClient(headers = { "x-api-key": BBSecret })

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
        if options is not None and options.get('stream', False):
            return self.CCClient.stream(data, options)
        else:
            return self.CCClient.generate(data, options)

    def imagine(self, input, options=None):
        if isinstance(input, list):
            data = self.BBClient.from_array(input, options)
        elif isinstance(input, str):
            data = self.BBClient.from_string(input, options)
        else:
            data = input
        return self.BBClient.imagine(data, options)

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