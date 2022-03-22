from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import PIL.Image ,PIL.ImageTk
import cv2

class Videogui :
    def __init__(self,window,window_title):
        self.window=window
        self.window_title=window_title

        top_frame=Frame(self.window)
        top_frame.pack(side=TOP,pady=5)

        bottom_frame = Frame(self.window)
        bottom_frame.pack(side=BOTTOM, pady=5)
        self.pauce=False # parameter that control pause button
        self.canvas=Canvas(top_frame)
        self.canvas.pack()

        # select button
        self_button_select=Button(bottom_frame,text="Select video file",width=15,command=self.open_file)
        self_button_select.grid(row=0,column=0)

        # play  button
        self_button_play = Button(bottom_frame, text="Play", width=15, command=self.play_video)
        self_button_play.grid(row=0, column=1)

        # pause button
        self_button_pause = Button(bottom_frame, text="pause", width=15, command=self.pause_video)
        self_button_pause.grid(row=0, column=2)

        # Resume button
        self_button_resume = Button(bottom_frame, text="Resume", width=15, command=self.resume_video)
        self_button_resume.grid(row=0, column=3)


        self.delay=15# ms
        self.window.mainloop()

    def open_file(self):
        self.pause=False
        self.filename=filedialog.askopenfilename(title="Select file",filetype=(("MP4 files","*.mp4"),("WMV files","*.mvw"),("AVI file","*.avi")))
        print(self.filename)

        # open the video file
        self.cap=cv2.VideoCapture(self.filename)
        self.width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas.config(width=self.width,height=self.height)
    def get_frame(self):
        try:
            if self.cap.isOpened():
                ret,frame=self.cap.read()
                return (ret,cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
        except:
            messagebox.showerror(title="video file is not found",massage='Please select a video file')
    def play_video(self):

        # get a frame from the videon source and go to the next frame automatically

        ret,frame=self.get_frame()
        if ret:
            self.photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0,0,image=self.photo,anchor=NW)
            if not self.pause:
                self.window.after(self.delay,self.play_video)

    def pause_video(self):
        self.pause=True

    def resume_video(self):
        self.pause=False
        self.play_video()

        # release the video source when the  object is destroyed
        def __del__(self):
            if self.cap.isOpend():
                self.cap.release()


    # end class
# crete a window and pass it to videoGui class
Videogui(Tk(),"Enjapan")


