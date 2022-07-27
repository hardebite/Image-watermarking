from tkinter import *
from tkinter import filedialog
from PIL import ImageDraw,ImageFont,Image,ImageTk
import cv2
#------functions-----
def add_text():
    word= text.get()
    text2 = canvas.create_text(160, 165,fill="white", text=f"{word}", font=("Ariel", 10, "bold"))
def savefile():
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    edge.save(filename)

window = Tk()
window.title("Image Watermarking  App")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
#------main-------
img= cv2.imread("pic.png")
edge=Image.fromarray(img)
image =ImageTk.PhotoImage(edge)
canvas.create_image(100,100,image=image)
canvas.grid(row=1,column=2)
text= Entry(width=20)
text.focus()
text_label=Label(text="watermark word")
button=Button(text="submit",command=add_text)
save=Button(text="save",command=savefile)


text_label.grid(row=2,column=1)
text.grid(row=2,column=2)
button.grid(row=2,column=3)
save.grid(row=3,column=2)


window.mainloop()