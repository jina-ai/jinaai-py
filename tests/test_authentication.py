import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '..'))
mock_dir = os.path.abspath(os.path.join(current_dir, './mock'))
sys.path.append(root_dir)
sys.path.append(mock_dir)
from jinaai import JinaAI
from mock.HTTPClientMock import mock_post_method

def test_auth_ko_no_token():
    jinaai = JinaAI()
    with mock_post_method(jinaai.SXClient):
        try:
            jinaai.describe('https://picsum.photos/200')
            assert True == False
        except Exception as e:
            assert e.args[0]['message'] == 'No token provided'
            assert e.args[0]['status'] == 'UNAUTHENTICATED'

def test_auth_ok():
    jinaai = JinaAI(
        tokens={
            'promptperfect-token': 'some-fake-token',
            'scenex-token': 'some-fake-token',
            'rationale-token': 'some-fake-token',
            'jinachat-token': 'some-fake-token',
        }
    )
    with mock_post_method(jinaai.SXClient):
        r = jinaai.describe('https://picsum.photos/200')
        assert r["results"][0]["output"] and len(r["results"][0]["output"]) > 0
