from flask import Flask, request, send_file
from flask import send_from_directory
from flask_cors import CORS
import os
import subprocess

python_script_path = 'fsm.py'

bash_script_path = 'run.sh'
app = Flask(__name__)
CORS(app)  # 解决跨域问题

# 假设有三个新闻文件
news_files = {
    'news1': 'News/news1.json',
    'news2': 'News/news2.json',
    'news3': 'News/news3.json',
}


@app.route('/download_news', methods=['GET'])
def download_news():
    # 获取前端传递的参数
    news_key = request.args.get('news_key')
    print(news_key)
    # 检查参数是否合法
    if news_key not in news_files:
        print("no")
        return 'Invalid news_key', 400

    # 获取文件路径
    file_path = news_files[news_key]

    # 提供文件下载
    return send_file(file_path, as_attachment=True)


@app.route('/upload', methods=["POST"])
def upload():
    try:
        if 'image' not in request.files:
            return "未上传文件"

        file_obj = request.files['image']

        upload_folder = os.path.join(os.getcwd(), "uploads")
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        file_path = os.path.join(upload_folder, file_obj.filename)
        file_obj.save(file_path)

        # 返回文件路径
        return file_path

        # 或者如果你想返回文件内容，取消注释下面这部分

        response = send_file(file_path, as_attachment=True)
        response.headers["Access-Control-Allow-Origin"] = "*"  # 允许跨域
        return response

    except Exception as e:
        print(f"处理上传文件时发生错误: {e}")
        return "处理上传文件时发生错误"


@app.route('/create_image', methods=['GET'])
def create_image():
    print("开始")
    subprocess.run(['python', python_script_path], check=True)
    print("执行完")
    return True


@app.route('/get_image', methods=['GET'])
def get_image():
    try:
        image_filename = 'SensitiveMap.png'
        image_directory = os.path.join(os.getcwd(), "")  # 修改为你的图片所在目录

        # 返回图片
        return send_from_directory(image_directory, image_filename)

    except Exception as e:
        print(f"处理获取图片时发生错误: {e}")
        return "处理获取图片时发生错误"


if __name__ == "__main__":
    app.run(debug=True)
