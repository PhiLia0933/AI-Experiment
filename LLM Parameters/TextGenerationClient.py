import json
import os
import sys

import requests
from dotenv import load_dotenv

# 自动加载 .env 文件
load_dotenv()

class TextGenerationClient:
    def __init__(self, api_url=None, api_key=None, model_name=None):
        """
        初始化客户端。如果不传参数，则自动从环境变量读取。
        """
        self.api_url = api_url or os.getenv("API_URL", "https://api.modelarts-maas.com/v2/chat/completions")
        self.api_key = api_key or os.getenv("API_KEY")
        self.model_name = model_name or os.getenv("MODEL", "deepseek-v4-flash")

        if not self.api_key:
            raise ValueError("❌ 错误：未检测到 API Key。请设置 API_KEY 环境变量或在初始化时传入。")

    def generate_text(self, payload):
        """
        发送请求并返回生成的文本。
        :param payload: 包含 messages, temperature 等参数的字典
        :return: 生成的文本字符串，或错误信息
        """
        # 如果 payload 里没有指定 model，就使用默认的模型
        if "model" not in payload:
            payload["model"] = self.model_name

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

        try:
            # 注意：verify=False 存在安全风险，生产环境建议去掉该参数或设为 True
            response = requests.post(self.api_url, headers=headers, data=json.dumps(payload), verify=False)
            
            # 如果 HTTP 状态码不是 200，抛出异常
            response.raise_for_status()
            
            res_data = response.json()
            
            # 解析大模型返回的内容 (兼容 OpenAI 格式)
            try:
                return res_data["choices"][0]["message"]["content"]
            except (KeyError, IndexError):
                return f"⚠️ 无法解析返回内容，原始响应如下：\n{response.text}"
                
        except requests.exceptions.RequestException as e:
            return f"⚠️ 请求发生异常: {e}"


# 如果你直接运行这个文件，它依然会作为脚本执行一次测试
if __name__ == '__main__':
    try:
        client = TextGenerationClient()
        test_payload = {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "你好"}
            ],
            "thinking": {"type": "enabled"}
        }
        print("测试连接中...")
        result = client.generate_text(test_payload)
        print(result)
    except ValueError as e:
        print(e)
        sys.exit(1)