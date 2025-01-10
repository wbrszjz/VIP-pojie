from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import validators

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.get_json()

    # 从 JSON 数据中提取所需的值
    line_selection = data.get('line1')
    choose_mode = data.get('choose_mode')
    website_box = data.get('web1')

    if not (line_selection and choose_mode and website_box):
        return jsonify({
            "message": "请粘贴视频链接至输入框。",
            "status": "error"
        }), 400  # 如果输入不完整，返回 400 错误

    # 检查网址是否有效
    if not validators.url(website_box):
        return jsonify({
            "message": "请输入有效视频网址。",
            "status": "error"
        }), 400  # 如果网址无效，返回错误消息

    # 根据线路选择生成对应的链接
    if line_selection == "line1":
        web = "https://jx.xmflv.cc/" + "?url=" + website_box
    elif line_selection == "line2":
        web = website_box
    else:
        return jsonify({'valid': False, 'message': '无效的线路选择。'}), 400  # 如果线路选择无效，返回错误

    # 返回生成的链接
    return jsonify({
        "status": "success",
        "generated_link": web,  # 返回生成的链接
    })


@app.route('/check_url', methods=['POST'])
def check_url():
    data2 = request.get_json()
    url = data2['url']
    if validators.url(url):
        return jsonify({'valid': True, 'url': url})
    else:
        return jsonify({'valid': False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
