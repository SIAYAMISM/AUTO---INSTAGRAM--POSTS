import tkinter as tk
from tkinter import font
import instabot

def post_insta(username, password, image_path, caption):
    try:
        bot = instabot.Bot()
        bot.login(username=username, password=password)
        bot.upload_photo(image_path=image_path, caption=caption)
    except Exception as e:
        print(f"Some error occurred: {e}")

def screen():
    app = tk.Tk()
    app.title("LET'S POST!")
    app.geometry("400x400")
    app.configure(bg="lightblue")

    custom_font = font.Font(family="Sitka", size=12, weight="bold")

    # Stylish Labels
    tk.Label(app, text="Username:", bg="lightblue", font=custom_font, fg="darkblue").pack(pady=(10, 0))
    username_entry = tk.Entry(app, width=30, font=custom_font, bd=2, relief="solid")
    username_entry.pack(pady=5)

    tk.Label(app, text="Password:", bg="lightblue", font=custom_font, fg="darkblue").pack(pady=(10, 0))
    password_entry = tk.Entry(app, width=30, font=custom_font, show='*', bd=2, relief="solid")
    password_entry.pack(pady=5)

    tk.Label(app, text="Image Path:", bg="lightblue", font=custom_font, fg="darkblue").pack(pady=(10, 0))
    image_entry = tk.Entry(app, width=30, font=custom_font, bd=2, relief="solid")
    image_entry.pack(pady=5)

    tk.Label(app, text="Caption:", bg="lightblue", font=custom_font, fg="darkblue").pack(pady=(10, 0))
    caption_entry = tk.Entry(app, width=30, font=custom_font, bd=2, relief="solid")
    caption_entry.pack(pady=5)

    def onPost():
        username = username_entry.get()
        password = password_entry.get()
        image_path = image_entry.get()
        caption = caption_entry.get()
        post_insta(username, password, image_path, caption)

    post_button = tk.Button(app, text="POST", command=onPost, font=custom_font, bg="lightgreen", fg="darkblue", bd=2, relief="raised")
    post_button.pack(pady=20)

    app.mainloop()

screen()
