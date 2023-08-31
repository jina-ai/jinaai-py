import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(root_dir)
from jinaai import JinaAI

def test_default_urls():
    jinaai = JinaAI()
    assert jinaai.PPClient.baseUrl == 'https://api.promptperfect.jina.ai'
    assert jinaai.SXClient.baseUrl == 'https://api.scenex.jina.ai/v1'
    assert jinaai.RAClient.baseUrl == 'https://us-central1-rationale-ai.cloudfunctions.net'
    assert jinaai.CCClient.baseUrl == 'https://api.chat.jina.ai/v1/chat'
    assert jinaai.BBClient.baseUrl == 'https://api.bestbanner.jina.ai/v1'

def test_customs_urls():
    jinaai = JinaAI(
        baseUrls={
            'promptperfect': 'https://promptperfect-customurl.jina.ai',
            'scenex': 'https://scenex-customurl.jina.ai',
            'rationale': 'https://rationale-customurl.jina.ai',
            'jinachat': 'https://jinachat-customurl.jina.ai',
            'bestbanner': 'https://bestbanner-customurl.jina.ai',
        }
    )
    assert jinaai.PPClient.baseUrl == 'https://promptperfect-customurl.jina.ai'
    assert jinaai.SXClient.baseUrl == 'https://scenex-customurl.jina.ai'
    assert jinaai.RAClient.baseUrl == 'https://rationale-customurl.jina.ai'
    assert jinaai.CCClient.baseUrl == 'https://jinachat-customurl.jina.ai'
    assert jinaai.BBClient.baseUrl == 'https://bestbanner-customurl.jina.ai'

