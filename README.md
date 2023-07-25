# JinaAI Python SDK

The JinaAI Python SDK is an efficient instrument that smoothly brings the power of JinaAI's products — [SceneXplain](https://scenex.jina.ai), [PromptPerfect](https://promptperfect.jina.ai/), [Rationale](https://rationale.jina.ai/), [BestBanner](https://bestbanner.jina.ai/), and [JinaChat](https://chat.jina.ai/) — into Python applications. Acting as a sturdy interface for JinaAI's APIs, this SDK lets you effortlessly formulate and fine-tune prompts, thus streamlining application development.

## Installing

### Package manager

Using pip:
```bash
$ pip install jinaai
```

## API secrets

To generate an API secret, you need to authenticate on each respective platform's API tab:

- [SceneXplain API](https://scenex.jina.ai/api)
- [PromptPerfect API](https://promptperfect.jina.ai/api)
- [Rationale API](https://rationale.jina.ai/api)
- [JinaChat API](https://chat.jina.ai/api)
- [BestBanner API](https://bestbanner.jina.ai/api)

> **Note:** Each secret is product-specific and cannot be interchanged. If you're planning to use multiple products, you'll need to generate a separate secret for each.

## Example usage


Import the SDK and instantiate a new client with your authentication secrets:

```python
from jinaai import JinaAI

jinaai = JinaAI(
    secrets = {
        'promptperfect-secret': 'XXXXXX',
        'scenex-secret': 'XXXXXX',
        'rationale-secret': 'XXXXXX',
        'jinachat-secret': 'XXXXXX',
        'bestbanner-secret': 'XXXXXX',
    }
)
```

Describe images:

```python
descriptions = jinaai.describe(
    'https://picsum.photos/200'
)
```

Evaluate situations:

```python
decisions = jinaai.decide(
    'Going to Paris this summer', 
    { 'analysis': 'proscons' }
)
```

Optimize prompts:

```python
prompts = jinaai.optimize(
    'Write an Hello World function in Python'
)
```

Generate complex answers:

```python
output = jinaai.generate(
    'Give me a recipe for a pizza with pineapple'
)
```

Create images from text:

```python
output = jinaai.imagine(
    'A controversial fusion of sweet pineapple and savory pizza.'
)
```

Use APIs together:

```python
situations = [toBase64(img) for img in [
    'factory-1.png',
    'factory-2.png',
    'factory-3.png',
    'factory-4.png',
]]

descriptions = jinaai.describe(situations)

prompt1 = [
    'Do any of those situations present a danger?',
    'Reply with [YES] or [NO] and explain why',
    *['SITUATION:\n' + desc['output'] for i, desc in enumerate(descriptions['results'])]
]

analysis = jinaai.generate('\n'.join(prompt1))

prompt2 = [
    'What should be done first to make those situations safer?',
    'I only want the most urgent situation',
    *['SITUATION:\n' + desc['output'] for i, desc in enumerate(descriptions['results'])]
]

recommendation = jinaai.generate('\n'.join(propmt2))

swot = jinaai.decide(
    recommendation['output'],
    { 'analysis': 'swot' }
)

banners = jinaai.imagine(
    *[desc['output'] for i, desc in enumerate(descriptions['results'])]
)
```

## Raw Output

You can retrieve the raw output of each APIs by passing `raw: True` in the options:

```python
descriptions = jinaai.describe(
    'https://picsum.photos/200',
    { 'raw': True }
)

print(descriptions['raw'])
```

## API Documentation

### JinaAi.describe

```python
output = JinaAI.describe(input, options)
```

- Input

>| VARIABLE                              | TYPE              | VALUE 
>|---------------------------------------|-------------------|----------
>| input                                 | str / str array   | Image URL or Base64

- Options

>| VARIABLE                               | TYPE              | VALUE 
>|----------------------------------------|-------------------|----------
>| options                                | dict              | 
>| options['algorithm']                   | None / str        | Aqua / Bolt / Comet / Dune / Ember / Flash
>| options['features']                    | None / str array  | high_quality, question_answer, tts, opt-out
>| options['languages']                   | None / str array  | en, cn, de, fr, it...
>| options['question']                    | None / str        | Question related to the picture(s)
>| options['style']                       | None / str        | default / concise / prompt

- Output

>| VARIABLE                               | TYPE              | VALUE 
>|----------------------------------------|-------------------|----------
>| output                                 | dict              | 
>| output['results']                      | dict array        | 
>| results[0]['output']                   | str               | The picture description
>| results[0]['i18n']                     | dict              | Contains one key for each item in languages
>| ...i18n['cn']                          | str               | The translated picture description

<br/>

### JinaAi.optimize

```python
output = JinaAI.optimize(input, options)
```

- Input

>| VARIABLE                               | TYPE              | VALUE 
>|----------------------------------------|-------------------|----------
>| input                                  | str / str array   | Image URL or Base64 / prompt to optimize

- Options

>| VARIABLE                               | TYPE              | VALUE 
>|----------------------------------------|-------------------|----------
>| options                                | dict              | 
>| options['targetModel']                 | None / str        | chatgpt / gpt-4 / stablelm-tuned-alpha-7b / claude / cogenerate / text-davinci-003 / dalle / sd / midjourney / kandinsky / lexica
>| options['features']                    | None / str array  | preview, no_spam, shorten, bypass_ethics, same_language, always_en, high_quality, redo_original_image, variable_subs, template_run
>| options['iterations']                  | None / number     | Default: 1
>| options['previewSettings']             | None / dict       | Contains the settings for the preview
>| ...previewSettings['temperature']      | number            | Example: 0.9
>| ...previewSettings['topP']             | number            | Example: 0.9
>| ...previewSettings['topK']             | number            | Example: 0
>| ...previewSettings['frequencyPenalty'] | number            | Example: 0
>| ...previewSettings['presencePenalty']  | number            | Example: 0
>| options['previewVariables']            | None / dict       | Contains one key for each variables in the prompt
>| ...previewVariables['var1']            | str               | The value of the variable
>| options['timeout']                     | Number            | Default: 20000
>| options['target_language']             | None / str        | en / cn / de / fr / it...

- Output

>| VARIABLE                               | TYPE              | VALUE 
>|----------------------------------------|-------------------|----------
>| output                                 | dict              | 
>| output['results']                      | dict array        | 
>| results[0]['output']                   | str               | The optimized prompt

<br/>

### JinaAi.decide

```python
output = JinaAI.decide(input, options)
```

- Input

>| VARIABLE                               | TYPE              | VALUE 
>|----------------------------------------|-------------------|----------
>| input                                  | str / str array   | Decision to evaluate

- Options

>| VARIABLE                               | TYPE              | VALUE 
>|----------------------------------------|-------------------|----------
>| options                                | dict              | 
>| options['analysis']                    | None / str        | proscons / swot / multichoice / outcomes
>| options['style']                       | None / str        | concise / professional / humor / sarcastic / childish / genZ
>| options['profileId']                   | None / str        | The id of the Personas you want to use

- Output

>| VARIABLE                               | TYPE              | VALUE 
>|----------------------------------------|-------------------|----------
>| output                                 | dict              | 
>| output['results']                      | dict array        | 
>| results[0]['proscons']                 | None / dict       |
>| ...proscons['pros']                    | dict              | Contains one key for each pros
>| ...proscons['pros']['pros1']           | str               | The explanation of the pros
>| ...proscons['cons']                    | dict              | Contains one key for each cons
>| ...proscons['cons']['cons1']           | str               | The explanation of the cons
>| ...proscons['bestChoice']              | str               | 
>| ...proscons['conclusion']              | str               | 
>| ...proscons['confidenceScore']         | number            | 
>| results[0]['swot']                     | None / dict       |
>| ...swot['strengths']                   | dict              | Contains one key for each strength
>| ...swot['strengths']['str1']           | str               | The explanation of the strength
>| ...swot['weaknesses']                  | dict              | Contains one key for each weakness
>| ...swot['weaknesses']['weak1']         | str               | The explanation of the weakness
>| ...swot['opportunities']               | dict              | Contains one key for each opportunity
>| ...swot['opportunities']['opp1']       | str               | The explanation of the opportunity
>| ...swot['threats']                     | dict              | Contains one key for each threat
>| ...swot['threats']['thre1']            | str               | The explanation of the threat
>| ...swot['bestChoice']                  | str               | 
>| ...swot['conclusion']                  | str               | 
>| ...swot['confidenceScore']             | number            | 
>| results[0]['multichoice']              | None / dict       | Contains one key for each choice
>| ...multichoice['choice1']              | str               | The value of the choice
>| results[0]['outcomes']                 | None / dict array |
>| ...outcomes[0]['children']             | None / dict array | a recursive array of results['outcomes']
>| ...outcomes[0]['label']                | str               | 
>| ...outcomes[0]['sentiment']            | str               | 

<br/>

### JinaAi.generate

```python
output = JinaAI.generate(input, options)
```

- Input

>| VARIABLE                               | TYPE                   | VALUE 
>|----------------------------------------|------------------------|----------
>| input                                  | str / str array        | Image URL or Base64 / prompt

- Options

>| VARIABLE                               | TYPE                   | VALUE 
>|----------------------------------------|------------------------|----------
>| options                                | dict                   | 
>| options['role']                        | None / str             | user / assistant
>| options['name']                        | None / str             | The name of the author of this message
>| options['chatId']                      | None / str             | The id of the conversation to continue
>| options['stream']                      | None / boolean         | Whether to stream back partial progress, Default: false
>| options['temperature']                 | None / number          | Default: 1
>| options['top_p']                       | None / str             | Default: 1
>| options['stop']                        | None / str / str array | Up to 4 sequences where the API will stop generating further tokens
>| options['max_tokens']                  | None / number          | Default: infinite
>| options['presence_penalty']            | None / number          | Number between -2.0 and 2.0, Default: 0
>| options['frequency_penalty']           | None / number          | Number between -2.0 and 2.0, Default: 0
>| options['logit_bias']                  | None / dict            | The likelihood for a token to appear in the completion
>| ...logit_bias['tokenId']               | number                 | Bias value from -100 to 100

- Output

>| VARIABLE                               | TYPE              | VALUE 
>|----------------------------------------|-------------------|----------
>| output                                 | dict              | 
>| output['output']                       | str               | The generated answer
>| output['chatId']                       | str               | The chatId to continue the conversation

<br/>

### JinaAi.imagine

```python
output = JinaAI.imagine(input, options)
```

- Input

>| VARIABLE                               | TYPE                   | VALUE 
>|----------------------------------------|------------------------|----------
>| input                                  | str / str array        | Prompt

- Options

>No options available

- Output

>| VARIABLE                               | TYPE              | VALUE 
>|----------------------------------------|-------------------|----------
>| output                                 | dict              | 
>| output['results']                      | dict array        |
>| results[0]['output']                   | array             | array of 4 image urls

<br/>

### JinaAi.utils

```python
outout = JinaAI.utils.image_to_base64(input)
```

>| VARIABLE                              | TYPE              | VALUE 
>|---------------------------------------|-------------------|----------
>| input                                 | str               | Image path on disk
>| output                                | str               | Base64 image

```python
outout = JinaAI.utils.is_url(input)
```

>| VARIABLE                              | TYPE              | VALUE 
>|---------------------------------------|-------------------|----------
>| input                                 | str               | 
>| output                                | boolean           | 

```python
outout = JinaAI.utils.is_base64(input)
```

>| VARIABLE                              | TYPE              | VALUE 
>|---------------------------------------|-------------------|----------
>| input                                 | str               | 
>| output                                | boolean           | 
