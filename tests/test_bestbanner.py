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
        'bestbanner-secret': 'some-fake-secret',
    }
)

def test_default_input():
    with mock_post_method(jinaai.BBClient):
        input = [
            'In today\'s fast-paced environment, increasing productivity ...',
            'When you have two days to finish a task ...'
        ]
        r1 = jinaai.imagine({ "data": [
            {
                'text': i,
            }
            for i in input
        ]})
        results = r1['results']
        assert results
        assert len(results) == 2
        assert len(results[0]['output']) == 4
        assert len(results[1]['output']) == 4

def test_text_input():
    with mock_post_method(jinaai.BBClient):
        input = 'In todays fast-paced environment, increasing productivity ...'
        r1 = jinaai.imagine(input)
        results = r1['results']
        assert results
        assert len(results) == 1
        assert len(results[0]['output']) == 4
        r2 = jinaai.imagine(input, {
            'style': 'flat',
        })
        results = r2['results']
        assert results
        assert len(results) == 1
        assert len(results[0]['output']) == 4

def test_text_arr_input():
    with mock_post_method(jinaai.BBClient):
        input = [
            'In today\'s fast-paced environment, increasing productivity ...',
            'When you have two days to finish a task ...'
        ]
        r1 = jinaai.imagine(input)
        results = r1['results']
        assert results
        assert len(results) == 2
        assert len(results[0]['output']) == 4
        assert len(results[1]['output']) == 4
        r2 = jinaai.imagine(input, {
            'style': 'minimalist',
        })
        results = r2['results']
        assert results
        assert len(results) == 2
        assert len(results[0]['output']) == 4
        assert len(results[1]['output']) == 4

def test_raw_output():
    with mock_post_method(jinaai.BBClient):
        input = [
            'In today\'s fast-paced environment, increasing productivity ...',
            'When you have two days to finish a task ...'
        ]
        r1 = jinaai.imagine(input, { 'raw': True })
        r1_raw_result = r1['raw']['result']
        assert r1_raw_result
        assert len(r1_raw_result) == 2
        assert r1_raw_result[0]['text'] == input[0]
        assert r1_raw_result[1]['text'] == input[1]
        assert len(r1_raw_result[0]['banners']) == 4
        assert len(r1_raw_result[1]['banners']) == 4
        r2 = jinaai.imagine(input, {
            'style': 'photographic',
            'raw': True
        })
        r2_raw_result = r2['raw']['result']
        assert r2_raw_result
        assert len(r2_raw_result) == 2
        assert r2_raw_result[0]['text'] == input[0]
        assert r2_raw_result[1]['text'] == input[1]
        assert len(r2_raw_result[0]['banners']) == 4
        assert len(r2_raw_result[1]['banners']) == 4
