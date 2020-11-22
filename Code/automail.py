import yagmail
import os

receiver = "mygmail@gmail.com"  # receiver email address
body = "Attendence File"  # email body
filename = "Attendance"+os.sep+"Attendance_2020-08-29_17-05-04.csv" 

yag = yagmail.SMTP("mymail@gmail.com", "my_password")

yag.send(
    to=receiver,
    subject="Attendance Report", 
    contents=body, 
    attachments=filename, 
)

