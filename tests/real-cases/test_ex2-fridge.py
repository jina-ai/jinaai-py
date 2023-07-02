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
        'jinachat-secret': os.environ.get('JINACHAT_SECRET', '')
    }
)

fridge = [jinaai.utils.image_to_base64(f"../../examples/images/{img}") for img in [
    'fridge-1.png',
]]

descriptions = None
prompt = None
recipe = None
swot = None

def test_scenex_get_descriptions():
    global descriptions
    descriptions = jinaai.describe(
        fridge,
        { 'question': 'What ingredients are in the fridge?', 'languages': ['en'] }
    )
    print('DESCRIPTION:\n', descriptions['results'][0]['output'])
    assert descriptions['results']
    assert len(descriptions['results']) == 1
    assert len(descriptions['results'][0]['output']) > 0

def test_promptperfect_get_optiprompt():
    global prompt
    assert descriptions
    prompt = jinaai.optimize('\n'.join([
        'Give me one recipe based on this list for ingredients',
        *['INGREDIENTS:\n' + desc['output'] for i, desc in enumerate(descriptions['results'])]
    ]))
    print('PROMPT:\n', prompt['results'][0]['output'])
    results = prompt['results']
    assert results
    assert len(results) == 1
    assert len(results[0]['output']) > 0

def test_jinachat_get_recipe():
    global recipe
    assert prompt
    recipe = jinaai.generate(prompt['results'][0]['output'])
    print('RECIPE:\n', recipe['output'])
    assert recipe['output']
    assert len(recipe['output']) > 0
    assert recipe['chatId']

def test_rationale_get_swot():
    global swot
    assert recipe
    swot = jinaai.decide(
        recipe['output'],
        { 'analysis': 'swot' }
    )
    print('SWOT:\n', swot['results'][0]['swot'])
    results = swot['results']
    assert results
    assert len(results) == 1
    assert results[0]['swot']
