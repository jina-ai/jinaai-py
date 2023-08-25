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
    with mock_post_method(jinaai.SXClient):
        input = ['https://picsum.photos/200']
        r1 = jinaai.describe({ "data": [
            {
                'image': i,
                'features': [],
                'algorithm': 'Ember',
                'languages': ['it'],
                'style': 'concise'
            } for i in input
        ]})
        results = r1['results']
        assert results
        assert len(results) == 1
        assert len(results[0]['output']) > 0
        assert results[0]['i18n'].get('it')

def test_image_url_input():
    with mock_post_method(jinaai.SXClient):
        input = 'https://picsum.photos/200'
        r1 = jinaai.describe(input)
        results = r1['results']
        assert results
        assert len(results) == 1
        assert len(results[0]['output']) > 0
        r2 = jinaai.describe(input, {
            'features': ['high_quality'],
            'algorithm': 'Comet',
            'languages': ['fr', 'de']
        })
        results = r2['results']
        assert results
        assert len(results) == 1
        assert len(results[0]['output']) > 0
        assert results[0]['i18n'].get('fr')
        assert results[0]['i18n'].get('de')

def test_image_url_input_shortened_answer():
    with mock_post_method(jinaai.SXClient):
        input = 'https://picsum.photos/200'
        r1 = jinaai.describe(input, { 'output_length': 50 })
        results = r1['results']
        assert results
        assert len(results) == 1
        assert len(results[0]['output']) > 0
        assert len(results[0]['output']) > 50
        assert results[0]['i18n'].get('en')
        assert len(results[0]['i18n']['en']) == 50
        r2 = jinaai.describe(input, {
            'output_length': 50,
            'languages': ['fr', 'de']
        })
        results = r2['results']
        assert results
        assert len(results) == 1
        assert len(results[0]['output']) > 0
        assert len(results[0]['output']) > 50
        assert results[0]['i18n'].get('fr')
        assert len(results[0]['i18n']['fr']) == 50
        assert results[0]['i18n'].get('de')
        assert len(results[0]['i18n']['de']) == 50

def test_image_url_arr_input():
    with mock_post_method(jinaai.SXClient):
        input = ['https://picsum.photos/200', 'https://picsum.photos/300']
        r1 = jinaai.describe(input)
        results = r1['results']
        assert results
        assert len(results) == 2
        assert len(results[0]['output']) > 0
        assert len(results[1]['output']) > 0
        r2 = jinaai.describe(input, {
            'features': ['high_quality'],
            'algorithm': 'Dune',
            'languages': ['fr']
        })
        results = r2['results']
        assert results
        assert len(results) == 2
        assert len(results[0]['output']) > 0
        assert len(results[1]['output']) > 0
        assert results[0]['i18n'].get('fr')
        assert results[1]['i18n'].get('fr')

def test_raw_output():
    with mock_post_method(jinaai.SXClient):
        input = ['https://picsum.photos/200', 'https://picsum.photos/300']
        r1 = jinaai.describe(input, { 'raw': True })
        r1_raw_result = r1['raw']['result']
        assert r1_raw_result
        assert len(r1_raw_result) == 2
        assert r1_raw_result[0]['image'] == input[0]
        assert r1_raw_result[1]['image'] == input[1]
        assert len(r1_raw_result[0]['features']) == 0
        assert r1_raw_result[0]['algorithm'] == 'Aqua'
        assert r1_raw_result[1]['algorithm'] == 'Aqua'
        assert r1_raw_result[0]['text']
        assert r1_raw_result[1]['text']
        assert not r1_raw_result[0]['answer']
        assert not r1_raw_result[1]['answer']
        assert r1_raw_result[0]['i18n'].get('en')
        assert r1_raw_result[1]['i18n'].get('en')
        r2 = jinaai.describe(input, {
            'question': 'How many people are on this photo?',
            'features': ['high_quality'],
            'algorithm': 'Dune',
            'languages': ['fr'],
            'raw': True
        })
        r2_raw_result = r2['raw']['result']
        assert r2_raw_result
        assert len(r2_raw_result) == 2
        assert r2_raw_result[0]['image'] == input[0]
        assert r2_raw_result[1]['image'] == input[1]
        assert len(r2_raw_result[0]['features']) == 2
        assert len(r2_raw_result[1]['features']) == 2
        assert r2_raw_result[0]['features'][0] == 'high_quality'
        assert r2_raw_result[0]['features'][1] == 'question_answer'
        assert r2_raw_result[1]['features'][0] == 'high_quality'
        assert r2_raw_result[1]['features'][1] == 'question_answer'
        assert r2_raw_result[0]['algorithm'] == 'Dune'
        assert r2_raw_result[1]['algorithm'] == 'Dune'
        assert r2_raw_result[0]['text']
        assert r2_raw_result[1]['text']
        assert r2_raw_result[0]['answer']
        assert r2_raw_result[1]['answer']
        assert not r2_raw_result[0]['i18n'].get('en')
        assert not r2_raw_result[1]['i18n'].get('en')
        assert r2_raw_result[0]['i18n'].get('fr')
        assert r2_raw_result[1]['i18n'].get('fr')
