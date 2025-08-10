# 启动方法：
# 1. 打开命令行，进入本项目 src 目录：
#    cd c:\Users\13384\Desktop\game\python-web-game\src
# 2. 启动 Flask 服务：
#    python app.py
# 3. 在浏览器访问 http://127.0.0.1:5000/
# 即可在线游玩黄金矿工小游戏。

from flask import Flask, render_template, send_from_directory, request, jsonify
import os
from game.logic import start_game, update_game_state, get_game_status

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = False  # 禁用模板自动重载以启用缓存

# 全局游戏状态
game_state = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates/<path:filename>')
def serve_template(filename):
    # 验证文件路径
    if not os.path.exists(os.path.join('templates', filename)):
        return "File not found", 404
    return send_from_directory('templates', filename)

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # 启动服务器并启用调试模式