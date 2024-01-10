from flask import Flask, request, render_template, jsonify
import youtube_dl

app = Flask(__name__)

def obtener_url_video(url):
    opciones = {
        'format': 'bestvideo+bestaudio/best',
        'quiet': True
    }

    with youtube_dl.YoutubeDL(opciones) as ydl:
        info = ydl.extract_info(url, download=False)
        url_video = info['url']
        return url_video

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/obtener_url', methods=['POST'])
def obtener_url():
    url_video = request.form['url']
    try:
        url_directa = obtener_url_video(url_video)
        return jsonify({'url_directa': url_directa})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
