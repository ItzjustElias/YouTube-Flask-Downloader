from pytubefix import YouTube
import os

def download_video(url, file_type):
    try:
        yt = YouTube(url)

        if file_type == "mp4":
            stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
            folder = "videos"
        elif file_type == "mp3":
            stream = yt.streams.filter(only_audio=True).first()
            folder = "music"
        else:
            print("Invalid choice. Please enter 'mp3' or 'mp4'.")
            return

        if not stream:
            print("No suitable stream found.")
            return

        download_folder = os.path.join(os.getcwd(), folder)
        os.makedirs(download_folder, exist_ok=True)

        file_path = stream.download(output_path=download_folder)

        if file_type == "mp3":
            base, ext = os.path.splitext(file_path)
            new_file = base + ".mp3"
            os.rename(file_path, new_file)
            file_path = new_file

        print(f"Downloaded successfully: {file_path}")

    except Exception as e:
        print("An error occurred while downloading the video.")
        print(e)

while True:
    url = input("\nEnter the video URL: ")
    choice = input("Choose format (mp3/mp4): ").strip().lower()

    download_video(url, choice)

    again = input("\nDo you want to download another video? (yes/no): ").strip().lower()
    if again != "yes":
        print("Exiting program. Have a great day!")
        break
