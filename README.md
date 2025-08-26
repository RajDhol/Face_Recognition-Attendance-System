# 🎯 Face Recognition Attendance System  

An automated **attendance management system** built with **Python & OpenCV** that uses **Haar Cascade** for face detection and **LBPH recognizer** for face recognition.  
It eliminates manual roll calls by marking attendance **in real-time** and storing records in **CSV files** and a **SQLite database**.  

---

## ✨ Features
✅ **Real-Time Face Detection** – Detects faces using Haar Cascade classifier  
✅ **Face Recognition** – Recognizes registered students using LBPH algorithm  
✅ **Automated Attendance Logging** – Stores name, ID, date & time in CSV/Database  
✅ **Database Integration** – SQLite-based student data and credentials  
✅ **User Management** – Add new students and train recognizer easily  
✅ **Simple & Lightweight** – Runs smoothly without heavy GPU/AI requirements  

---

## 🛠️ Technologies Used
- **Language**: Python  
- **Libraries**: OpenCV, NumPy, Pandas  
- **Database**: SQLite + CSV Export  
- **Tools**: Git, Visual Studio Code  

---

## ⚙️ How It Works
1. **Register Student**  
   - Capture multiple face images and save them in `college_images/`.  

2. **Train Recognizer**  
   - Run `train.py` to train LBPH model on captured faces.  

3. **Mark Attendance**  
   - Run `attendance.py` → Recognizes faces via webcam.  
   - Logs attendance into `exportfile.csv` and `user_credentials.db`.  

4. **View Attendance**  
   - Attendance records can be accessed via CSV or Database.  

---

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/Face_Recognition-Attendance-System.git
   cd Face_Recognition-Attendance-System
2.**Install dependencies**
   ```bash
   pip install -r requirements.txt
```
3.**Run the application
   ```bash
  python main.py
  ```

---

## 📊 Example Attendance Log
| Student ID | Name        | Date       | Time     |
|------------|------------|------------|----------|
| 101        | Raj Dhol    | 2025-03-30 | 10:05 AM |
| 102        | Meera Joshi | 2025-03-30 | 10:07 AM |

---

## 🔮 Future Enhancements
- 📌 GUI for Admin/Student management  
- 📌 Export reports to Excel & PDF  
- 📌 Email/SMS notification system  
- 📌 Web-based dashboard  

---

## 👨‍💻 Author
Developed by **Raj Dhol**  and **Komal Ghevariya**
Contributions & suggestions are welcome! 🎉  

---

## 📜 License
Licensed under the **MIT License** – Free to use and modify.  


