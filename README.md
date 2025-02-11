# YouTube Downloader Flask App

This is a simple Flask application that allows users to download YouTube videos in MP4 or MP3 format.  It uses the `pytubefix` library for interacting with YouTube and provides a basic web interface for selecting the video and download format.

## Features

* Downloads YouTube videos in MP4 format (various resolutions).
* Downloads YouTube audio in MP3 format.
* Asynchronous file deletion after download.
* Simple and easy-to-use web interface.

## Installation

1. **Clone the repository:**

  ```bash
  git clone https://github.com/ItzjustElias/Yt-Downloader.git
  ```

  ```bash
  cd Yt-Downloader
  ```

2. **Install required dependencies:**

  ```bash
  pip install flask pytubefix
  ```

## Usage

1. **Run the Flask app:**

  ```Bash
  python app.py
  ```

2. **Paste the YouTube video URL into the input field.**

3. **Select the desired file type (MP4 or MP3).**

4. **Click the "Download" button.**

The downloaded file will be saved in the downloads folder within the project directory.

## Code Explanation

**pytubefix:** This library is used to extract video and audio streams from YouTube.
**Flask:** This web framework is used to create the web interface and handle requests.
**send_from_directory:** This Flask function is used to send the downloaded file to the user's browser.
**threading:** This module is used to create a separate thread for deleting the downloaded file, allowing the main thread to handle other requests.
**os:** This module is used for file system operations, such as creating the download directory and deleting files.
**Templates:** The index.html template (shown below) provides the user interface for the application. This file should be placed in a templates folder within your project.

  ```HTML

  <!DOCTYPE html>
  <html>
  <head>
      <title>YouTube Downloader</title>
  </head>
  <body>
      <h1>YouTube Downloader</h1>
      <form method="POST">
          <label for="url">YouTube URL:</label>
          <input type="text" name="url" id="url" required><br><br>

          <label for="file_type">File Type:</label>
          <select name="file_type" id="file_type">
              <option value="mp4">MP4</option>
              <option value="mp3">MP3</option>
          </select><br><br>

          <button type="submit">Download</button>
      </form>
  </body>
  </html>
  ```

## Further Improvements

**More robust error handling:** Implement more specific error messages and handle edge cases more effectively.
**Download progress:** Add a progress bar to show the download progress.
**Support for other video/audio formats:** Expand the supported formats beyond MP4 and MP3.
**Deployment:** Deploy the application to a web server for public access.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

Licensed under the MIT license.
