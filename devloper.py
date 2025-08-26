from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_images\dev.jpg")
        img_top=img_top.resize((1530,720),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=250,y=0,width=1100,height=650)

        img_top1=Image.open(r"college_images\raj.jpg")
        img_top1=img_top1.resize((450,550),Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=5,y=0,width=450,height=550)

        dev_label = Label(main_frame, text="✤ Hello My Name Is Raj", font=("times new roman", 20, "bold"))
        dev_label.place(x=480, y=5)

        dev_label = Label(main_frame, text="✤ I am a beginner developer", font=("times new roman", 20, "bold"))
        dev_label.place(x=480, y=40)

        # Additional Information - Skills and Technologies
        skills_label = Label(main_frame, text="✤ Skills and Technologies:", font=("times new roman", 20, "bold"))
        skills_label.place(x=480, y=75)

        skills_info = Label(main_frame, text="➥ Python, HTML, CSS, JavaScript, PHP, etc.", font=("times new roman", 16))
        skills_info.place(x=500, y=110)

        # Additional Information - Education and Background
        education_label = Label(main_frame, text="✤ Education and Background:", font=("times new roman", 20, "bold"))
        education_label.place(x=480, y=145)

        education_info = Label(main_frame, text="➥ BCA, Saurashtra University", font=("times new roman", 16))
        education_info.place(x=500, y=180)

        # Additional Information - Projects
        projects_label = Label(main_frame, text="✤ Projects:", font=("times new roman", 20, "bold"))
        projects_label.place(x=480, y=215)

        project1_info = Label(main_frame, text="➥ Project 1: E-LEARNING", font=("times new roman", 16))
        project1_info.place(x=500, y=250)

        project2_info = Label(main_frame, text="➥ Project 2: FACE RECOGNITION ATTENDANCE SOFTWARE", font=("times new roman", 16))
        project2_info.place(x=500, y=285)

    


       





if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()