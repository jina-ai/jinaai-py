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

def test_scenex_analyse_video():
    descriptions = jinaai.describe(
        'https://guillaume-public.s3.us-east-2.amazonaws.com/videos/superman.mp4',
        {
            'algorithm': 'Inception',
            'languages': ['en'],
        }
    )
    assert len(descriptions['results'][0]['output']) > 0
    assert descriptions['results'][0]["i18n"]["en"]
    assert descriptions['results'][0]["i18n"]["en"]['summary']
    assert len(descriptions['results'][0]["i18n"]["en"]['events']) > 0
    print('SUMMARY: ', descriptions['results'][0]["i18n"]["en"]['summary'])
    print('EVENTS: ', descriptions['results'][0]["i18n"]["en"]['events'])
