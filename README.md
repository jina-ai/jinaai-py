# jinaai-py

The JinaAI Python SDK is a powerful tool that seamlessly integrates the capabilities of JinaAI's products, including SceneXplain, PromptPerfect, Rationale and JinaChat into Python applications. This SDK acts as a robust wrapper around JinaAI's APIs, empowering users to create and optimize prompts effectively.

## Installing

### Package Manager

Using pip:
```bash
$ pip install jinaai
```
## API Tokens

Authenticate on each platforms and go on the API tab to generate an API token:
- https://scenex.jina.ai
- https://promptperfect.jina.ai
- https://rationale.jina.ai
- https://chat.jina.ai

## Example Usage

Import the SDK and instantiate a new client with your authentication tokens:
```python
from jinaai import JinaAI

jinaai = new JinaAI(
    tokens = {
        'promptperfect-token': 'XXXXXX',
        'scenex-token': 'XXXXXX',
        'rationale-token': 'XXXXXX',
        'chatcat-token': 'XXXXXX',
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

Generate complex answer:
```python
output = jinaai.generate(
    'Give me a recipe for a pizza with pineapple'
)
```

Use APIs together
```python
situations = [toBase64(img) for img in [
    'factory-1.png',
    'factory-2.png',
    'factory-3.png',
    'factory-4.png',
]]

descriptions = jinaai.describe(situations)

prompt1 = [
    'Does any of those situations present a danger?',
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
```

## API Documentation

- JinaAi.describe

```python
output = JinaAI.describe(input, options)
```

| Variable                | Type              | Value 
|-------------------------|-------------------|----------
| input                   | str / str array   | Image URL or Base64

| options                 | dict              | 
| options['algorithm']    | None / str        | Aqua / Bolt / Comet / Dune / Ember / Flash
| options['features']     | None / str array  | high_quality, question_answer
| options['languages']    | None / str array  | en, cn, de, fr, it...
| options['question']     | None / str        | Question related to the picture(s)
| options['style']        | None / str        | default / concise / prompt

| output                  | dict              | results
| output['results']       | dict array        | 
| results['output']       | str               | The picture description
| results['i18n']         | dict              | Contains one key for each item in languages
| ...i18n['cn']           | str               | The translated picture description

- JinaAi.optimize

```python
output = JinaAI.optimize(input, options)
```

| Variable                               | Type              | Value 
|----------------------------------------|-------------------|----------
| input                                  | str / str array   | Prompt to optimize

| options                                | dict              | 
| options['targetModel']                 | None / str        | chatgpt / gpt-4 / stablelm-tuned-alpha-7b / claude / cogenerate / text-davinci-003 / dalle / sd / midjourney / kandinsky / lexica
| options['features']                    | None / str array  | preview, no_spam, shorten, bypass_ethics, same_language, always_en, high_quality, redo_original_image, variable_subs, template_run
| options['iterations']                  | None / number     | Default: 1
| options['previewSettings']             | None / dict       | Contains the settings for the preview
| ...previewSettings['temperature']      | number            | Example: 0.9
| ...previewSettings['topP']             | number            | Example: 0.9
| ...previewSettings['topK']             | number            | Example: 0
| ...previewSettings['frequencyPenalty'] | number            | Example: 0
| ...previewSettings['presencePenalty']  | number            | Example: 0
| options['previewVariables']            | None / dict       | Contains one key for each variables in the prompt
| ...previewVariables['var1']            | str               | The value of the variable
| options['timeout']                     | Number            | Default: 20000
| options['target_language']             | None / str        | en / cn / de / fr / it...

| output                                 | dict              | results
| output['results']                      | dict array        | 
| results['output']                      | str               | The optimized prompt

- JinaAi.decide

```python
output = JinaAI.decide(input, options)
```

| Variable                               | Type              | Value 
|----------------------------------------|-------------------|----------
| input                                  | str / str array   | Decision to evaluate
| options                                | dict              | 
| options['analysis']                    | None / str        | proscons / swot / multichoice / outcomes
| options['style']                       | None / str        | concise / professional / humor / sarcastic / childish / genZ
| options['profileId']                   | None / str        | The id of the Personas you want to use

| output                                 | dict              | results
| output['results']                      | dict array        | 
| results['proscons']                    | dict              |
