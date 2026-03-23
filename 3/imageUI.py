import customtkinter as ctk
from PIL import Image
import os
import pygame


pygame.mixer.init()


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def is_leap_year(year):
    if year < 1:
        return "invalid"
    elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "leap"
    else:
        return "not_leap"


def update_image(filename):
    try:
        path = os.path.join(BASE_DIR, "images", filename)
        img = ctk.CTkImage(Image.open(path), size=(150, 150))
        image_label.configure(image=img)
        image_label.image = img
    except Exception as e:
        result_label.configure(text=f"Image error: {e}")



def play_sound(file_path):
    try:
        pygame.mixer.music.stop()  # stop previous sound
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except Exception as e:
        print("Sound error:", e)



def check_year():
    user_input = entry.get()

    try:
        year = int(user_input)
        result = is_leap_year(year)

        if result == "leap":
            result_label.configure(text=f"{year} is a Leap Year ")
            update_image("leap.jpg")

        elif result == "not_leap":
            result_label.configure(text=f"{year} is NOT a Leap Year ")
            update_image("not_leap.png")

        else:
            result_label.configure(text="Invalid Year ")
            update_image("error.png")

    except ValueError:
        result_label.configure(text="Invalid Input ")
        update_image("error.png")


        play_sound(os.path.join(BASE_DIR, "images", "faa.mp3"))



app = ctk.CTk()
app.title("Leap Year Checker")
app.geometry("350x420")
app.resizable(False, False)


frame = ctk.CTkFrame(app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = ctk.CTkLabel(frame, text="Enter a year", anchor="w")
label.pack(fill="x", padx=10, pady=(10, 0))


entry = ctk.CTkEntry(frame, placeholder_text="e.g. 2024")
entry.pack(fill="x", padx=10, pady=10)


button = ctk.CTkButton(frame, text="Check", command=check_year)
button.pack(pady=10)


result_label = ctk.CTkLabel(frame, text="")
result_label.pack(pady=10)


image_label = ctk.CTkLabel(frame, text="")
image_label.pack(pady=10)


app.mainloop()