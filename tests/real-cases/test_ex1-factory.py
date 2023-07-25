import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.append(root_dir)
from jinaai import JinaAI

# THIS TEST USES REAL CREDITS

jinaai = JinaAI(
    secrets = {
        'promptperfect-secret': os.environ.get('PROMPTPERFECT_SECRET', ''),
        'scenex-secret': os.environ.get('SCENEX_SECRET', ''),
        'rationale-secret': os.environ.get('RATIONALE_SECRET', ''),
        'jinachat-secret': os.environ.get('JINACHAT_SECRET', ''),
        'bestbanner-secret': os.environ.get('BESTBANNER_SECRET', '')
    }
)

situations = [jinaai.utils.image_to_base64(f"../../examples/images/{img}") for img in [
    'factory-2.png',
    'factory-3.png',
    'factory-4.png',
]]

descriptions = None
analysis = None
recommendation = None
swot = None
banners = None

def test_scenex_get_descriptions():
    global descriptions
    descriptions = jinaai.describe(situations)
    results = descriptions['results']
    assert results
    assert len(results) == 3
    for i, desc in enumerate(descriptions['results']):
        assert len(results[i]['output']) > 0
        print(f"DESCRIPTION {i + 1}:\n{desc['output']}\n")

def test_jinachat_get_analysis():
    global analysis
    assert descriptions
    analysis = jinaai.generate('\n'.join([
        'Does any of those situations present a danger?',
        'Reply with [SITUATION_NUMBER] [YES] or [NO] and explain why',
        *['SITUATION ' + str(i + 1) + ':\n' + desc['output'] for i, desc in enumerate(descriptions['results'])]
    ]))
    print('ANALYSIS:\n', analysis['output'])
    assert analysis['output']
    assert len(analysis['output']) > 0
    assert analysis['chatId']

def test_jinachat_get_recommendation():
    global recommendation
    assert descriptions
    recommendation = jinaai.generate('\n'.join([
        'According to those situations, what should be done first to make everything safer?',
        'I only want the most urgent situation',
        *['SITUATION ' + str(i + 1) + ':\n' + desc['output'] for i, desc in enumerate(descriptions['results'])]
    ]))
    print('RECOMMENDATION:\n', recommendation['output'])
    assert recommendation['output']
    assert len(recommendation['output']) > 0
    assert recommendation['chatId']


def test_rationale_get_swot():
    global swot
    assert recommendation
    swot = jinaai.decide(
        recommendation['output'],
        { 'analysis': 'swot' }
    )
    print('SWOT:\n', swot['results'][0]['swot'])
    results = swot['results']
    assert results
    assert len(results) == 1
    assert results[0]['swot']

def test_bestbanner_get_banners():
    global banners
    assert descriptions
    banners = jinaai.imagine(descriptions['results'][0]['output'])
    print('BANNERS:\n', banners['results'])
    assert banners['results']
    assert len(banners['results']) == 1
    assert len(banners['results'][0]['output']) == 4
