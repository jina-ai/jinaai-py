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
    with mock_post_method(jinaai.CCClient):
        input_data = ['Give me an Hello World function in Typescript']
        r1_input_messages = [{'role': 'user', 'content': i} for i in input_data]
        r1 = jinaai.generate({'messages': r1_input_messages})
        assert r1['output']
        assert len(r1['output']) > 0
        assert r1['chatId'] == 'aaaaaaaaaaaaaaaaaaaaaaaaaaa'
        r2_input_messages = [{'role': 'user', 'content': i} for i in input_data]
        r2 = jinaai.generate({'messages': r2_input_messages, 'chatId': '1234567890'})
        assert r2['output']
        assert len(r2['output']) > 0
        assert r2['chatId'] == '1234567890'

def test_text_input():
    with mock_post_method(jinaai.CCClient):
        input_data = 'Give me an Hello World function in Typescript'
        r1 = jinaai.generate(input_data)
        assert r1['output']
        assert len(r1['output']) > 0
        assert r1['chatId'] == 'aaaaaaaaaaaaaaaaaaaaaaaaaaa'
        r2 = jinaai.generate(input_data, {'chatId': '1234567890'})
        assert r2['output']
        assert len(r2['output']) > 0
        assert r2['chatId'] == '1234567890'

def test_text_with_img_input():
    with mock_post_method(jinaai.CCClient):
        input_data = 'What could I do with this?'
        url = 'https://picsum.photos/200'
        r1 = jinaai.generate(input_data, { 'image': url })
        assert r1['output']
        assert len(r1['output']) > 0
        assert r1['chatId'] == 'aaaaaaaaaaaaaaaaaaaaaaaaaaa'

def test_text_arr_input():
    with mock_post_method(jinaai.CCClient):
        input_data = [
            'Give me an Hello World function in Typescript',
            'Make it take an optional param NAME and replace world by NAME if set'
        ]
        r1 = jinaai.generate(input_data)
        assert r1['output']
        assert len(r1['output']) > 0
        assert r1['chatId'] == 'aaaaaaaaaaaaaaaaaaaaaaaaaaa'
        r2 = jinaai.generate(input_data, {'chatId': '1234567890'})
        assert r2['output']
        assert len(r2['output']) > 0
        assert r2['chatId'] == '1234567890'

def test_raw_output():
    with mock_post_method(jinaai.CCClient):
        input_data = 'Give me an Hello World function in Typescript'
        r1 = jinaai.generate(input_data, {'raw': True})
        raw_response = r1['raw']
        assert raw_response['choices']
        assert len(raw_response['choices']) > 0
        assert len(raw_response['choices'][0]['message']['content']) > 0
        assert len(raw_response['choices'][0]['finish_reason']) > 0
        assert raw_response['usage']
        assert raw_response['usage']['prompt_tokens']
        assert raw_response['usage']['completion_tokens']
        assert raw_response['usage']['total_tokens']
        assert raw_response['chatId'] == 'aaaaaaaaaaaaaaaaaaaaaaaaaaa'
