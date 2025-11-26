import tkinter as tk
from tkinter import filedialog
import pygame

# starts mixer for music
pygame.mixer.init()

# asks for and loads song from file explorer
def load_song():
    file = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")]
    )
    if file:
        song_label.config(text=file)
        pygame.mixer.music.load(file)

# tells mixer tp play loaded music
def play_song():
    pygame.mixer.music.play()

# tells mixer to pause music
def pause_song():
    pygame.mixer.music.pause()

# tells mixer to unpause
def resume_song():
    pygame.mixer.music.unpause()

# tells mixer to stop music
def stop_song():
    pygame.mixer.music.stop()

#GUI
root = tk.Tk()
root.title("Rob's Music Player")
root.geometry("600x200")
root.iconbitmap('C:/Users/rw513/Documents/GitHub/pythonMusicPlayer/13105.vresize.350.350.medium.85.ico')

song_label = tk.Label(root, text="No song loaded")
song_label.pack(pady=10)

# buttons
tk.Button(root, text="Load Song", command=load_song).pack()
tk.Button(root, text="Play", command=play_song).pack()
tk.Button(root, text="Pause", command=pause_song).pack()
tk.Button(root, text="Resume", command=resume_song).pack()
tk.Button(root, text="Stop", command=stop_song).pack()

root.mainloop()
