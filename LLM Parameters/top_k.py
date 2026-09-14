import contextlib
import os
import sys
import warnings
from datetime import datetime, timedelta, timezone

from TextGenerationClient import TextGenerationClient

# 屏蔽 verify=False 带来的安全警告
warnings.filterwarnings("ignore")


class Tee:
    """同时将写入内容转发到多个流（控制台 + 文件）"""

    def __init__(self, *streams):
        self.streams = streams

    def write(self, data):
        for s in self.streams:
            s.write(data)
            s.flush()

    def flush(self):
        for s in self.streams:
            s.flush()


if __name__ == '__main__':
    # 1. 实例化客户端（自动读取 .env 文件中的 KEY、URL 和 MODEL）
    client = TextGenerationClient()

    # 2. 定义要测试的 top_k 值
    test_top_k = [1, 5, 10]
    prompt = "介绍一下大语言模型"

    # 设定东八区 (UTC+8)
    china_tz = timezone(timedelta(hours=8))
    output_dir = "Test Result"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{datetime.now(china_tz):%m-%d-%H-%M-%S}.txt")

    # 4. 打开文件，把 print 输出同时写入文件和终端
    with (
        open(output_file, "w", encoding="utf-8") as f,
        contextlib.redirect_stdout(Tee(sys.stdout, f)),
    ):

        print(f"🚀 开始测试模型 top_k 值 (Model: {client.model_name})\n")

        # 5. 循环测试
        for k in test_top_k:
            print("\n" + "=" * 50)
            print(f"🔍 正在测试 Top-k = {k}")
            print("=" * 50)

            payload = {
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 100,
                "temperature": 0.6,         # 修正为浮点数
                "top_k": k,
                "top_p": 1,
                "ignore_eos": False,        # 修正为布尔值
                "stream": False
            }

            # 6. 调用类的方法获取结果
            result_text = client.generate_text(payload)
            print(result_text)

        print(f"\n✅ 测试完成，结果已保存至: {output_file}")

    print(f"📄 输出文件路径: {output_file}")