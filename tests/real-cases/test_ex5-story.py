import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.append(root_dir)
from jinaai import JinaAI

# THIS TEST USES REAL CREDITS

jinaai = JinaAI(
    secrets = {
        'scenex-secret': os.environ.get('SCENEX_SECRET', ''),
    }
)

fridge = [jinaai.utils.image_to_base64(f"../../examples/images/{img}") for img in [
    'fridge-1.png',
]]

def test_scenex_get_descriptions():
    descriptions = jinaai.describe(
        fridge,
        { 'question': 'What ingredients are in the fridge?', 'algorithm': 'Hearth','languages': ['en'] }
    )
    print('DESCRIPTION:\n', descriptions['results'][0]['output'])
    assert descriptions['results']
    assert len(descriptions['results']) == 1
    assert len(descriptions['results'][0]['output']) > 0
    assert descriptions["results"][0]["tts"].get("en")
    assert descriptions["results"][0]["ssml"].get("en")
    print("TTS: ", descriptions["results"][0]["tts"]["en"])
    print("SSML: ", descriptions["results"][0]["ssml"]["en"])
    assert descriptions["results"][0]["i18n"]["en"]
    assert len(descriptions["results"][0]["i18n"]["en"]) > 0
    assert descriptions["results"][0]["i18n"]["en"][0]['message']
    for line in descriptions["results"][0]["i18n"]["en"]:
        print(line["name"], ": ", line["message"])
