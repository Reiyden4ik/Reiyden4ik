import vlc

def play_mp4(file_path):
    player = vlc.MediaPlayer(file_path)
    player.play()

# Usage
play_mp4("/path/to/your/video.mp4")