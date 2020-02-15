import tkinter
from tkinter import ttk


def main():
    root = tkinter.Tk()

    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    go_forward_button = ttk.Button(frame1, text='Forward')
    go_forward_button.grid()

    root.mainloop()

########################################################################
#
# EXPLANATION of the above:
#
# The 6 statements in main (above) do the following, respectively:
#
#   1. Constructs a tkinter.Tk.
#        This is the top-level window, traditionally called 'root'.
#
#   2. Constructs a widget (here, a ttk.Frame) on the root,
#        naming the Frame  frame1  for use in subsequent statements.
#
#        Use Frame objects to group other items.  Best practice is
#        to make a Frame and put all other widgets on the Frame.
#
#        This Frame has a "padding" of 10 pixels on each side.
#        Try removing the    padding=10    to see the effect of padding.
#
#   3. Displays the ttk.Frame, using a layout called 'grid'.
#         -- We'll learn more about controlling the layout later.
#         -- For now, simply apply the   grid   method to ANY widget
#            to make it appear on the screen.
#
#   4. Constructs a widget (here, a ttk.Button) on the Frame.
#         Set its text to 'Forward'.
#
#   5. Displays the ttk.Button, again using the 'grid' layout.
#
#   6. Runs the Event Loop.  tkinter maintains that loop.
#         This is a LOOP -- the code STAYS in here until the root window
#         is closed (by the user, or by the program itself).
#
# When you run the program, note that:
#   -- A window appears.
#   -- The window has the usual minimize, maximize and close buttons
#        in the window's title bar.
#   -- Those buttons work as expected.
#   -- There is also a button inside the window whose label is: Forward.
#   -- Pressing the Forward button causes visual feedback in the usual
#        way, but nothing else happens.  That's because we haven't told
#        tkinter/ttk what to do when the Forward button is pressed.
#        You'll see how to do that in the next examples.
########################################################################


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
