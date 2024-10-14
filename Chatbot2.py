import os
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

# 创建 Flask 应用
app = Flask(__name__)
client = OpenAI()

# 根路径，返回 HTML 页面
@app.route('/')
def home():
    return render_template('index.html')

# 聊天接口，处理用户输入并返回模型响应
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return jsonify({"response": completion.choices[0].message})

# 运行 Flask 应用
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)