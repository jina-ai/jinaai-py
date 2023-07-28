import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.append(root_dir)
from jinaai import JinaAI

# THIS TEST USES REAL CREDITS

jinaai = JinaAI(
    secrets = {
        'jinachat-secret': os.environ.get('JINACHAT_SECRET', '')
    }
)

def test_jinachat_email_direct_response():
    prompt = 'Compose a professional and courteous email to our valued customer, expressing sincere gratitude for their use of our products. Your email should convey appreciation and highlight specific reasons why their choice to utilize our products is valued and important. Please provide a warm and personalized message that makes the customer feel valued and appreciated. Additionally, be sure to include any relevant details or information about upcoming promotions, new products, or customer loyalty programs that may be of interest to the customer. Your email should be well-written, concise, and focused, while still conveying genuine gratitude and fostering a positive relationship with the customer.'
    email = jinaai.generate(prompt)
    print('EMAIL: ', email['output'])
    assert email['output']
    assert len(email['output']) > 0
    assert email['chatId']

def test_jinachat_email_stream_response():
    prompt = 'Compose a professional and courteous email to our valued customer, expressing sincere gratitude for their use of our products. Your email should convey appreciation and highlight specific reasons why their choice to utilize our products is valued and important. Please provide a warm and personalized message that makes the customer feel valued and appreciated. Additionally, be sure to include any relevant details or information about upcoming promotions, new products, or customer loyalty programs that may be of interest to the customer. Your email should be well-written, concise, and focused, while still conveying genuine gratitude and fostering a positive relationship with the customer.'
    stream = jinaai.generate(prompt, { 'stream': True })
    print('STREAM: ', stream)
    loopCounter = 0
    for line in stream.iter_lines():
        if line:
            print('CHUNK: ', line.decode('utf-8'))
            loopCounter = loopCounter + 1
    assert loopCounter > 1
