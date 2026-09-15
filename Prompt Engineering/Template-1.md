# 构建基础问答Prompt

## Build a basic Q&A prompt.

payload = {
    "model": "deepseek-v4-flash",
    "messages": [
    {"role": "system", "content": f"你是一个文本阅读器，读取文章的内容并按照用户的要求输出对于文章的回答，以下是文章{content}"},
    {"role": "user", "content": "根据文章回答段誉干了什么"}
    ],
    "max_tokens": 200,
    "top_p": 1,
    "temperature": 0.3,
}
generated_text = client.generate_text(payload)
print(generated_text)


payload = {
    "model": "deepseek-v4-flash",
    "messages": [
    {"role": "system", "content": f"你是一个文本阅读器，读取文章的内容并按照用户的要求输出对于文章的回答，以下是文章{content}"},
    {"role": "user", "content": "根据文章回答：文章中有几个人物"}
    ],
    "max_tokens": 200,
    "top_p": 1,
    "temperature": 1,
}
generated_text = client.generate_text(payload)
print(generated_text)


payload = {
    "model": "deepseek-v4-flash",
    "messages": [
    {"role": "system", "content": f"你是一个文本阅读器，读取文章的内容并按照用户的要求输出对于文章的回答，以下是文章{content}"},
    {"role": "user", "content": "根据文章回答：文中的四个主角是什么关系"}
    ],
    "max_tokens": 200,
    "top_p": 1,
    "temperature": 1,
}
generated_text = client.generate_text(payload)
print(generated_text)