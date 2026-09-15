# Prompt工程技术控制模型输出

## Prompt engineering techniques for controlling model output.

## 样本提示 Example Prompt

payload = {
    "model": "deepseek-v4-flash",
    "messages": [
    {"role": "system", "content": f"\
    指令：你是一个文本阅读器，读取文章的内容并按照用户的要求输出对于文章的回答，\
    上下文：“文章：a,b,c,d,e是五个人物，他们之间是亲属关系；提问：文章的6个人物，他们是什么关系；回答：文章中只有五个人物，他们是亲属关系” \
    以下是文章{content}"},
    {"role": "user", "content": "根据文章回答：文中的4个人物是什么关系"}
    ],
    "max_tokens": 200,
    "top_p": 1,
    "temperature": 1,
}
generated_text = client.generate_text(payload)
print(generated_text)

## 思维链提示 CoT Prompting

payload = {
    "model": "deepseek-v4-flash",
    "messages": [
    {"role": "system", "content": f"\
    指令：你是一个文本阅读器，读取文章的内容并按照用户的要求输出对于文章的回答，\
    你需要逐步思考用户提出问题并逐一回答 \
    以下是文章{content}"},
    {"role": "user", "content": "根据文章回答：文中的四个主角是什么关系"}
    ],
    "max_tokens": 200,
    "top_p": 1,
    "temperature": 1,
}
generated_text = client.generate_text(payload)
print(generated_text)

## 链式提示-1 Prompt Chaining-1

payload = {
    "model": "deepseek-v4-flash",
    "messages": [
    {"role": "system", "content": f"\
    指令：你是一个文本阅读器，读取文章的内容并按照用户的要求输出对于文章的回答，\
    以下是文章{content}"},
    {"role": "user", "content": "根据文章回答：文中有几个人物，他们是什么关系"}
    ],
    "max_tokens": 200,
    "top_p": 1,
    "temperature": 1,
}
generated_text = client.generate_text(payload)
print(generated_text)
info = generated_text #提取的信息

## 链式提示-2 Prompt Chaining-2

payload = {
    "model": "deepseek-v4-flash",
    "messages": [
    {"role": "system", "content": f"\
    指令：根据提问对比已知的信息，找出提问的错误，并输出错误的点”\
    以下是已知的信息{info}"},
    {"role": "user", "content": "提问的问题是：“文中的四个主角是什么关系”"}
    ],
    "max_tokens": 200,
    "top_p": 1,
    "temperature": 0.3,
}
generated_text = client.generate_text(payload)
print(generated_text)
error = generated_text  #提问的错误

## 链式提示-3 Prompt Chaining-3

payload = {
    "model": "deepseek-v4-flash",
    "messages": [
    {"role": "system", "content": f"\
    指令：你是一个文本阅读器，读取文章的内容并按照用户的要求输出对于文章的回答，\
    以下是文章{content}"},
    {"role": "user", "content": "根据文章回答：文中的四个主角是什么关系"}
    ],
    "max_tokens": 200,
    "top_p": 1,
    "temperature": 1,
}
generated_text = client.generate_text(payload)
print(generated_text)
answer = generated_text

## 链式提示-4 Prompt Chaining-4

payload = {
    "model": "deepseek-v4-flash",
    "messages": [
    {"role": "system", "content": f"\
    指令：根据错误信息，并修改错误的回答，并按照输出格式化输出正确的回复 \
    上下文：以下是错误信息{error}， \
            以下是需要修改的错误的回答{answer} \
    输出格式化：问题：\
                正确的答案应该是：\
    "},
    {"role": "user", "content": ""}
    ],
    "max_tokens": 200,
    "top_p": 1,
    "temperature": 1,
}
generated_text = client.generate_text(payload)
print(generated_text)

## 接来下串起整个流程，在新的执行框中输入如下代码并运行

## Next, to string the entire workflow together, enter the following code in a new execution cell and run it.

Q = "根据文章回答：文中的四个主角是什么关系"
payload = {
    "model": "deepseek-v4-flash",
    "messages": [
    {"role": "system", "content": f"\
    指令：你是一个文本阅读器，读取文章的内容并按照用户的要求输出对于文章的回答，\
    以下是文章{content}"},
    {"role": "user", "content": f"{Q}"}
    ],
    "max_tokens": 200,
    "top_p": 1,
    "temperature": 1,
}
generated_text = client.generate_text(payload)
info = generated_text #提取的信息
payload = {
    "model": "deepseek-v4-flash",
    "messages": [
    {"role": "system", "content": f"\
    指令：根据提问对比已知的信息，找出提问的错误，并输出错误的点”\
    以下是已知的信息{info}"},
    {"role": "user", "content": f"提问的问题是：“{Q}”"}
    ],
    "max_tokens": 200,
    "top_p": 1,
    "temperature": 0.3,
}
generated_text = client.generate_text(payload)
error = generated_text  #提问的错误
payload = {
    "model": "deepseek-v4-flash",
    "messages": [
    {"role": "system", "content": f"\
    指令：你是一个文本阅读器，读取文章的内容并按照用户的要求输出对于文章的回答，\
    以下是文章{content}"},
    {"role": "user", "content": f"{Q}"}
    ],
    "max_tokens": 200,
    "top_p": 1,
    "temperature": 1,
}
generated_text = client.generate_text(payload)
answer = generated_text
payload = {
    "model": "deepseek-v4-flash",
    "messages": [
    {"role": "system", "content": f"\
    指令：根据错误信息，并修改错误的回答，并按照输出格式化输出正确的回复 \
    上下文：以下是错误信息{error}， \
            以下是需要修改的错误的回答{answer} \
    输出格式化：问题：\
                正确的答案应该是：\
    "},
    {"role": "user", "content": ""}
    ],
    "max_tokens": 200,
    "top_p": 1,
    "temperature": 1,
}
generated_text = client.generate_text(payload)
print(generated_text)