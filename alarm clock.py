import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import time

def set_alarm():
    print("Alarm set for:", hours.get(), ":", minutes.get())
    print("Selected song:", selected_song.get())

def select_song():
    filename = filedialog.askopenfilename(title="Select Song", filetypes=[("Audio Files", "*.mp3 *.wav")])
    if filename:
        selected_song.set(filename)

def update_time():
    current_time = time.strftime("%H:%M:%S")
    current_time_label.config(text=current_time)
    root.after(1000, update_time)  # Schedule update_time to be called again in 1000ms (1 second)

root = tk.Tk()
root.title("Snoozer")
root.geometry("550x400")

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

time_label = ttk.Label(main_frame, text="Current Time:",font=('Arial', 40, 'bold', 'italic'),)
time_label.grid(column=0, row=0, sticky=tk.W,)

current_time_label = ttk.Label(main_frame, text="",font=('Arial', 40, 'bold', 'italic'))
current_time_label.grid(column=1, row=0, sticky=tk.W)

update_time()  # Start the function to update time

hours_label = ttk.Label(main_frame, text="Hours:",font=('Arial', 40, 'bold', 'italic'),)
hours_label.grid(column=0, row=1, sticky=tk.W)

hours = tk.StringVar()
hours_entry = ttk.Entry(main_frame, textvariable=hours,font=('Arial', 20, 'bold', 'italic'))
hours_entry.grid(column=1, row=1)

minutes_label = ttk.Label(main_frame, text="Minutes:",font=('Arial', 40, 'bold', 'italic'),)
minutes_label.grid(column=0, row=3, sticky=tk.W)

minutes = tk.StringVar()
minutes_entry = ttk.Entry(main_frame, textvariable=minutes,font=('Arial', 20, 'bold', 'italic'))
minutes_entry.grid(column=1, row=3,)

song_label = ttk.Label(main_frame, font=('Arial', 40, 'bold', 'italic'), text="Select Song:")
song_label.grid(column=0, row=5, sticky=tk.W)

selected_song = tk.StringVar()
selected_song_entry = ttk.Entry(main_frame, textvariable=selected_song, state="readonly", font=('Arial', 20, 'bold', 'italic'))
selected_song_entry.grid(column=1, row=5)

select_song_button = ttk.Button(main_frame, text="Browse", command=select_song)
select_song_button.grid(column=2, row=5)

set_button = ttk.Button(main_frame, text="Set Alarm", command=set_alarm)
set_button.grid(column=0, row=6, columnspan=3, pady=10)

root.mainloop()
