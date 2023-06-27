import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '..'))
mock_dir = os.path.abspath(os.path.join(current_dir, './mock'))
sys.path.append(root_dir)
sys.path.append(mock_dir)
from jinaai import JinaAI
from mock.HTTPClientMock import mock_post_method

jinaai = JinaAI(
    secrets={
        'promptperfect-secret': 'some-fake-secret',
        'scenex-secret': 'some-fake-secret',
        'rationale-secret': 'some-fake-secret',
        'jinachat-secret': 'some-fake-secret',
    }
)

def test_default_input():
    with mock_post_method(jinaai.PPClient):
        input = ['Give me an Hello World function in Typescript']
        r1 = jinaai.optimize({ "data": [
            {
                'prompt': i,
                'targetModel': 'chatgpt',
                'features': [],
                'target_language': 'it'
            } for i in input
        ]})
        results = r1['results']
        assert results
        assert len(results) == 1
        assert len(results[0]['output']) > 0

def test_string_input():
    with mock_post_method(jinaai.PPClient):
        input1 = 'Give me an Hello World function in Typescript'
        input2 = 'https://picsum.photos/200'
        r1 = jinaai.optimize(input1)
        results = r1['results']
        assert results
        assert len(results) == 1
        assert len(results[0]['output']) > 0
        r2 = jinaai.optimize(input2, {
            'targetModel': 'dalle',
            'features': ['shorten'],
            'target_language': 'fr'
        })
        results = r2['results']
        assert results
        assert len(results) == 1
        assert len(results[0]['output']) > 0

def test_arr_input():
    with mock_post_method(jinaai.PPClient):
        input = ['Give me an Hello World function in Typescript', 'https://picsum.photos/300']
        r1 = jinaai.optimize(input)
        results = r1['results']
        assert results
        assert len(results) == 2
        assert len(results[0]['output']) > 0
        assert len(results[1]['output']) > 0
        r2 = jinaai.optimize(input, {
            'targetModel': 'dalle',
            'features': ['shorten'],
            'target_language': 'fr'
        })
        results = r2['results']
        assert results
        assert len(results) == 2
        assert len(results[0]['output']) > 0
        assert len(results[1]['output']) > 0

def test_raw_output():
    with mock_post_method(jinaai.PPClient):
        input1 = 'Give me an Hello World function in Typescript'
        input2 = 'https://picsum.photos/200'
        r1 = jinaai.optimize(input1, { 'raw': True })
        assert r1['raw']['result']
        assert len(r1['raw']['result']) == 1
        assert r1['raw']['result'][0]['prompt'] == input1
        assert not r1['raw']['result'][0]['imagePrompt']
        assert len(r1['raw']['result'][0]['features']) == 0
        assert r1['raw']['result'][0]['targetModel'] == 'chatgpt'
        assert r1['raw']['result'][0]['promptOptimized']
        assert r1['raw']['result'][0]['language'] == 'en'
        assert not r1['raw']['result'][0]['targetLanguage']
        r2 = jinaai.optimize(input2, {
            'raw': True,
            'target_language': 'it',
            'targetModel': 'claude',
            'features': ['shorten', 'high_quality']
        })
        assert r2['raw']['result']
        assert len(r2['raw']['result']) == 1
        assert len(r2['raw']['result'][0]['prompt']) > 0
        assert r2['raw']['result'][0]['imagePrompt'] == input2
        assert len(r2['raw']['result'][0]['features']) == 2
        assert r2['raw']['result'][0]['targetModel'] == 'claude'
        assert r2['raw']['result'][0]['promptOptimized']
        assert r2['raw']['result'][0]['language'] == 'it'
        assert r2['raw']['result'][0]['targetLanguage'] == 'it'
