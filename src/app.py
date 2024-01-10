from flask import Flask, request, render_template, send_from_directory
import os
import youtube_dl

app = Flask(__name__)

def descargar_video(url, carpeta_destino):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    opciones = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(carpeta_destino, '%(title)s.%(ext)s'),
    }

    with youtube_dl.YoutubeDL(opciones) as ydl:
        ydl.download([url])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/descargar', methods=['POST'])
def descargar():
    url_video = request.form['url']
    carpeta_destino = 'descargas'
    try:
        descargar_video(url_video, carpeta_destino)
        return send_from_directory(directory=carpeta_destino, filename=os.listdir(carpeta_destino)[0], as_attachment=True)
    except Exception as e:
        return f"Ocurrió un error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
