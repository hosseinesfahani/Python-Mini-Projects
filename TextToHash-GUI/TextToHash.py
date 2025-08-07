import customtkinter as ctk

app = ctk.CTk()
app.title("Text To Hash Application")
app.geometry("650x500")
app.resizable(False, False)

label_txt = ctk.CTkLabel(app, text="Your Text")
label_txt.pack(pady = (20, 10))

txt_box = ctk.CTkTextbox(app, width=500, height=100, wrap="word")
txt_box.pack(pady = (0, 20))

label_hash = ctk.CTkLabel(app, text="Hash Of Your Text")
label_hash.pack(pady = 10)

out_hash = ctk.CTkTextbox(app, width=500, height=150)
out_hash.configure(state="disabled")
out_hash.pack(pady = (0, 20))

btn = ctk.CTkButton(app, text="Hashing", width=300, height=40)
btn.pack(pady = (20, 0))

app.mainloop()