import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pygame import mixer

# Initialize the mixer
mixer.init()

# Function to add songs to the playlist
def add_songs():
    songs = filedialog.askopenfilenames(initialdir='/', title='Select Songs', filetypes=(('MP3 Files', '*.mp3'),))
    for song in songs:
        playlist.insert(tk.END, song)

# Function to play the selected song
def play_song():
    try:
        song = playlist.get(tk.ACTIVE)
        if song:
            mixer.music.load(song)
            mixer.music.play()
        else:
            messagebox.showerror("Error", "No song selected")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to stop the song
def stop_song():
    mixer.music.stop()

# Function to pause the song
def pause_song():
    mixer.music.pause()

# Function to resume the song
def resume_song():
    mixer.music.unpause()

# Function to remove a song from the playlist
def remove_song():
    try:
        selected_song = playlist.curselection()
        if selected_song:
            playlist.delete(selected_song)
        else:
            messagebox.showerror("Error", "No song selected")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title('Simple Music Player')

# Create the playlist box
playlist = tk.Listbox(root, selectmode=tk.SINGLE, bg='black', fg='white', font=('arial', 15), width=40)
playlist.grid(columnspan=5)

# Create buttons
add_button = tk.Button(root, text='Add Songs', command=add_songs)
play_button = tk.Button(root, text='Play', command=play_song)
pause_button = tk.Button(root, text='Pause', command=pause_song)
resume_button = tk.Button(root, text='Resume', command=resume_song)
stop_button = tk.Button(root, text='Stop', command=stop_song)
remove_button = tk.Button(root, text='Remove Song', command=remove_song)

# Place buttons on the grid
add_button.grid(row=1, column=0)
play_button.grid(row=1, column=1)
pause_button.grid(row=1, column=2)
resume_button.grid(row=1, column=3)
stop_button.grid(row=1, column=4)
remove_button.grid(row=1, column=5)

# Run the main loop
root.mainloop()
