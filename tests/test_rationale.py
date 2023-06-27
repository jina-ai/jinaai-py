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
    with mock_post_method(jinaai.RAClient):
        input = ['Going to Paris this summer']
        r1 = jinaai.decide({ "data": [
            {
                'decision': i,
                'analysis': 'swot',
                'style': 'concise'
            } for i in input
        ]})
        results = r1['results']
        assert results
        assert len(results) == 1
        assert not r1['results'][0]['proscons']
        assert r1['results'][0]['swot']
        assert not r1['results'][0]['multichoice']
        assert not r1['results'][0]['outcomes']
        r1KeyResults = r1['results'][0]['swot']
        assert r1KeyResults['strengths']
        assert r1KeyResults['weaknesses']
        assert r1KeyResults['opportunities']
        assert r1KeyResults['threats']

def test_text_input():
    with mock_post_method(jinaai.RAClient):
        input = 'Going to Paris this summer'
        r1 = jinaai.decide(input)
        assert r1['results']
        assert len(r1['results']) == 1
        assert r1['results'][0]['proscons']
        assert not r1['results'][0]['swot']
        assert not r1['results'][0]['multichoice']
        assert not r1['results'][0]['outcomes']
        r1KeyResults = r1['results'][0]['proscons']
        assert r1KeyResults['pros']
        assert r1KeyResults['cons']
        r2 = jinaai.decide(input, {
            'analysis': 'multichoice',
            'style': 'genZ'
        })
        assert r2['results']
        assert len(r2['results']) == 1
        assert not r2['results'][0]['proscons']
        assert not r2['results'][0]['swot']
        assert r2['results'][0]['multichoice']
        assert not r2['results'][0]['outcomes']
        r2KeyResults = r2['results'][0]['multichoice']
        assert len(r2KeyResults) == 3


def test_arr_input():
    with mock_post_method(jinaai.RAClient):
        input = ['Going to Paris this summer', 'Going to Beijing this winter']
        r1 = jinaai.decide(input)
        assert r1['results']
        assert len(r1['results']) == 2
        assert r1['results'][0]['proscons']
        assert not r1['results'][0]['swot']
        assert not r1['results'][0]['multichoice']
        assert not r1['results'][0]['outcomes']
        assert r1['results'][1]['proscons']
        assert not r1['results'][1]['swot']
        assert not r1['results'][1]['multichoice']
        assert not r1['results'][1]['outcomes']
        r1KeyResults1 = r1['results'][0]['proscons']
        assert r1KeyResults1['pros']
        assert r1KeyResults1['cons']
        r1KeyResults2 = r1['results'][1]['proscons']
        assert r1KeyResults2['pros']
        assert r1KeyResults2['cons']
        r2 = jinaai.decide(input, {
            'analysis': 'multichoice',
            'style': 'genZ'
        })
        assert r2['results']
        assert len(r2['results']) == 2
        assert not r2['results'][0]['proscons']
        assert not r2['results'][0]['swot']
        assert r2['results'][0]['multichoice']
        assert not r2['results'][0]['outcomes']
        assert not r2['results'][1]['proscons']
        assert not r2['results'][1]['swot']
        assert r2['results'][1]['multichoice']
        assert not r2['results'][1]['outcomes']
        r2KeyResults1 = r2['results'][0]['multichoice']
        assert len(r2KeyResults1) == 3
        r2KeyResults2 = r2['results'][1]['multichoice']
        assert len(r2KeyResults2) == 3


def test_raw_output():
    with mock_post_method(jinaai.RAClient):
        input = ['Going to Paris this summer', 'Going to Beijing this winter']
        r1 = jinaai.decide(input, { 'raw': True })
        assert r1['raw']['result']
        assert r1['raw']['result']['result']
        assert len(r1['raw']['result']['result']) == 2
        assert r1['raw']['result']['result'][0]['decision'] == input[0]
        assert r1['raw']['result']['result'][1]['decision'] == input[1]
        assert r1['raw']['result']['result'][0]['writingStyle'] == 'concise'
        assert r1['raw']['result']['result'][1]['writingStyle'] == 'concise'
        assert r1['raw']['result']['result'][0]['analysis'] == 'proscons'
        assert r1['raw']['result']['result'][1]['analysis'] == 'proscons'
        r1KeyResults1 = r1['raw']['result']['result'][0]['keyResults']
        assert r1KeyResults1['pros']
        assert r1KeyResults1['cons']
        r1KeyResults2 = r1['raw']['result']['result'][1]['keyResults']
        assert r1KeyResults2['pros']
        assert r1KeyResults2['cons']
        r2 = jinaai.decide(input, {
            'analysis': 'multichoice',
            'style': 'genZ',
            'raw': True
        })
        assert r2['raw']['result']
        assert r2['raw']['result']['result']
        assert len(r2['raw']['result']['result']) == 2
        assert r2['raw']['result']['result'][0]['decision'] == input[0]
        assert r2['raw']['result']['result'][1]['decision'] == input[1]
        assert r2['raw']['result']['result'][0]['writingStyle'] == 'genZ'
        assert r2['raw']['result']['result'][1]['writingStyle'] == 'genZ'
        assert r2['raw']['result']['result'][0]['analysis'] == 'multichoice'
        assert r2['raw']['result']['result'][1]['analysis'] == 'multichoice'
        r2KeyResults1 = r2['raw']['result']['result'][0]['keyResults']
        assert len(r2KeyResults1) == 3
        r2KeyResults2 = r2['raw']['result']['result'][1]['keyResults']
        assert len(r2KeyResults2) == 3
