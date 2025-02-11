from flask import Flask, render_template, request, send_from_directory
from pytubefix import YouTube
import os
import time
import threading

app = Flask(__name__)

DOWNLOAD_FOLDER = os.path.join(os.getcwd(), 'downloads')
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

def delete_file_async(file_path):
    time.sleep(2)
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error deleting file: {e}")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        file_type = request.form.get("file_type")

        try:
            yt = YouTube(url)
            stream = None

            if file_type == "mp4":
                for res in ["highest", "720p", "480p", "360p"]:
                    stream = yt.streams.filter(progressive=True, file_extension="mp4", res=res).first()
                    if stream:
                        break

                if not stream:
                    for res in ["highest", "720p", "480p", "360p"]:
                        stream = yt.streams.filter(adaptive=True, file_extension="mp4", res=res).first()
                        if stream:
                            break

                if not stream and file_type == "mp4":
                    for res in ["highest", "720p", "480p", "360p"]:
                        stream = yt.streams.filter(progressive=True, file_extension="webm", res=res).first()
                        if stream:
                            break

            elif file_type == "mp3":
                stream = yt.streams.filter(only_audio=True).first()
            else:
                return "Invalid file type."

            if not stream:
                return "No suitable stream found. Please try another video or format."

            file_path = stream.download(output_path=app.config['DOWNLOAD_FOLDER'])

            if file_type == "mp3":
                base, ext = os.path.splitext(file_path)
                new_file = base + ".mp3"
                os.rename(file_path, new_file)
                file_path = new_file

            filename = os.path.basename(file_path)
            response = send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)

            # Start a new thread to delete the file asynchronously
            thread = threading.Thread(target=delete_file_async, args=(file_path,))
            thread.start()

            return response

        except Exception as e:
            return f"An error occurred: {e}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)