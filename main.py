from customtkinter import * 
from tkinter import ttk
from ig_scraper import IGBot

colors = (
    '#4564dc', # azul [0]
    '#aa2cc0', # roxo [1]
    '#ec0075', # rosa [2]
    '#ff6903', #laranja [3]
    '#ffd366', # amarelo [4]

)


def run_bot():
    user = user_value.get()
    password = pass_word_value.get()
    target = target_value.get()

    ibot = IGBot(user, password, target)
    ibot.login()


app = CTk()
# app.grid(padx=20, pady=10)
app.geometry('300x300')
app.resizable(0, 0)
app.title('Insta Scraper')
set_appearance_mode('light')

label_title = CTkLabel(master=app, text='Instagram profile scraper')
label_title.pack(pady=20)

# dec frames
input_frame = ttk.Frame(master=app)
input_frame1 = ttk.Frame(master=app)
input_frame2 = ttk.Frame(master=app)

# dec labels
label_user = CTkLabel(master=input_frame, text='user', width=100, anchor='w', padx=10)
label_pass = CTkLabel(master=input_frame1, text='password', width=100, anchor='w', padx=10)
label_target = CTkLabel(master=input_frame2, text='target', width=100, anchor='w', padx=10)

# dec inputs
user_value = StringVar()
input_user = CTkEntry(master=input_frame, placeholder_text='login', 
    textvariable=user_value)

pass_word_value = StringVar()
input_pass = CTkEntry(master=input_frame1, placeholder_text='password',
    textvariable=pass_word_value)

target_value = StringVar()
input_target = CTkEntry(master=input_frame2, placeholder_text='target',
    textvariable=target_value)

# scrap button
scrap_button = CTkButton(master=app, text='scrape', command=run_bot,
    fg_color=colors[1],
    hover_color=colors[2],
    corner_radius=5,)

# packs
    # frames
input_frame.pack(pady=10, fill='x')
input_frame1.pack(pady=10, fill='x')
input_frame2.pack(pady=10, fill='x')

    # grid
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)

input_frame1.columnconfigure(0, weight=1)
input_frame1.columnconfigure(1, weight=1)

input_frame2.columnconfigure(0, weight=1)
input_frame2.columnconfigure(1, weight=1)

    # inputs
input_user.grid(row=0, column=0, sticky=E)
input_pass.grid(row=1, column=0, sticky=E)
input_target.grid(row=2, column=0, sticky=E)

    # labels
label_user.grid(row=0, column=1, sticky=W)
label_pass.grid(row=1, column=1, sticky=W)
label_target.grid(row=2, column=1, sticky=W)

# button
scrap_button.pack()

app.mainloop()
