from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("UTK Image Viewer")
root.geometry("300x400+350+150")
root.minsize(260, 360)
root.iconbitmap("icon11.ico")

Im1 = ImageTk.PhotoImage(Image.open("icon1.ico"))
Im2 = ImageTk.PhotoImage(Image.open("icon2.ico"))
Im3 = ImageTk.PhotoImage(Image.open("icon3.ico"))
Im4 = ImageTk.PhotoImage(Image.open("icon4.ico"))

Image_list = [Im1, Im2, Im3, Im4]

index_list = 0


def back():
    global index_list
    index_list-=1
    window.destroy()
    frame_make()

def forward():
    global index_list
    index_list += 1
    window.destroy()
    frame_make()


def frame_make():
    global window
    window = Frame(root)
    window.pack(expand=True, fill=BOTH)

    c_image = Image_list[index_list]

    Label(window, image=c_image).pack()
    Label(window, text="Image {0} of {1}".format(index_list + 1, len(Image_list)),
          bd=1, relief=SUNKEN, font='-size 18', anchor=CENTER).pack()

    back_btn = Button(window, text="<<", font='-size 18', cursor='hand2', command=back)
    exit_btn = Button(window, text="EXIT", font='-size 18', cursor='hand2', command=root.destroy)
    fwd_btn = Button(window, text=">>", font='-size 18', cursor='hand2', command=forward)

    if index_list == 0:
        back_btn.config(state=DISABLED)
    if index_list == (len(Image_list) - 1):
        fwd_btn.config(state=DISABLED)

    back_btn.place(relx=0.2, rely=0.9, anchor=CENTER)
    exit_btn.place(relx=0.5, rely=0.9, anchor=CENTER)
    fwd_btn.place(relx=0.8, rely=0.9, anchor=CENTER)


frame_make()

root.mainloop()
