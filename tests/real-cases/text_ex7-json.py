import json
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

def test_scenex_json_output():
    descriptions = jinaai.describe(
        'https://picsum.photos/200',
        {
            'algorithm': 'Jelly',
            'languages': ['en'],
            'json_schema': {
                    'type': 'object',
                    'properties': {
                        'headcount':{
                            'type': 'number',
                            'description': 'How many people in this image'
                        },
                        'location':{
                            'type': 'string',
                            'description': 'Short description of the location'
                        }
                    }
                }
        }
    )
    assert len(descriptions['results'][0]['output']) > 0
    assert descriptions['results'][0]["i18n"]["en"]
    assert json.loads(descriptions['results'][0]["i18n"]["en"])
    print('JSON: ', json.loads(descriptions['results'][0]["i18n"]["en"]))
