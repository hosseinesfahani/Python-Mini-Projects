import customtkinter as ctk
import hashlib

app = ctk.CTk()
app.title("Text To Hash Application")
app.geometry("650x500")
app.resizable(False, False)

label_txt = ctk.CTkLabel(app, text="Your Text")
label_txt.pack(pady = (25, 10))

txt_box = ctk.CTkTextbox(app, width=500, height=100, wrap="word")
txt_box.pack(pady = (0, 20))

label_hash = ctk.CTkLabel(app, text="Hash Of Your Text")
label_hash.pack(pady = 10)

output = ctk.CTkTextbox(app, width=500, height=150)
output.configure(state="disabled")
output.pack(pady = (0, 20))

def hash_func():
    user_txt = txt_box.get("1.0", "end-1c")
    hashed_txt = hashlib.md5(user_txt.encode()).hexdigest()
    output.configure(state="normal")
    output.delete("1.0", "end")
    output.insert("1.0", hashed_txt)
    output.configure(state="disabled")

btn = ctk.CTkButton(app, text="Hashing", width=300, height=40, command=hash_func)
btn.pack(pady = (20, 0))

app.mainloop()