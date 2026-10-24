from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/get')
def get_video():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "no url"}), 400
    ydl_opts = {'quiet': True, 'skip_download': True, 'format': 'best'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        direct = info.get('url')
        if not direct and 'formats' in info:
            direct = info['formats'][-1]['url']
        return jsonify({"direct_url": direct, "title": info.get('title')})

@app.route('/')
def home():
    return "YR API is running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
