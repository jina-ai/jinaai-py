from jinaai import JinaAI
import os

jinaai = JinaAI(
    secrets = {
        'promptperfect-secret': os.environ.get('PROMPTPERFECT_SECRET', ''),
        'scenex-secret': os.environ.get('SCENEX_SECRET', ''),
        'rationale-secret': os.environ.get('RATIONALE_SECRET', ''),
        'jinachat-secret': os.environ.get('JINACHAT_SECRET', '')
    }
)

def toBase64(img: str) -> str:
    return jinaai.utils.image_to_base64(f"images/{img}")

fridge = toBase64('fridge-1.png')

def generate():
    try:
        # 1. get a description of the fridge content
        descriptions = jinaai.describe(
            fridge,
            { 'question': 'What ingredients are in the fridge?', 'languages': ['en'] }
        )
        print('DESCRIPTION:\n', descriptions['results'][0]['output'])
        # 2. get an optmised prompt
        prompt = jinaai.optimize('\n'.join([
            'Give me one recipe based on this list for ingredients',
            *['INGREDIENTS:\n' + desc['output'] for i, desc in enumerate(descriptions['results'])]
        ]))
        print('PROMPT:\n', prompt['results'][0]['output'])
        # 3. get a recipe based on the descriptions
        recipe = jinaai.generate(prompt['results'][0]['output'])
        print('RECIPE:\n', recipe['output'])
        # 4. get a swot analysis of the recommendation
        swot = jinaai.decide(
            recipe['output'],
            { 'analysis': 'swot' }
        )
        print('SWOT:\n', swot['results'][0]['swot'])
    except Exception as e:
        print("Error:", str(e))

generate()
