import tkinter
from tkinter import ttk


def main():
    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    # The image file must be GIF (or one of several other unhelpful
    # formats). To convert a JPG or anything else, use an outside tool.
    # Note that the image file must be in the same folder as this
    # module, if you use this way to refer to the image file.
    photo = tkinter.PhotoImage(file='gif1.gif')

    button1 = ttk.Button(main_frame, image=photo)
    # The next line is necessary when your root.mainloop() call is outside the
    # current method. Tkinter has a bug that makes it think the image is ready for
    # garbage collection, which makes the image fully transparent.
    # See: http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
    button1.image = photo
    button1.grid()
    button1['command'] = lambda: print('hello')

    root.mainloop()


main()
