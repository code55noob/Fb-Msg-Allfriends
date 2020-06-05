# -*- coding: utf-8 -*-
import sys
from fbchat import Client
from fbchat.models import *
user= "username"
pas= "password"
client = Client(user,pas)
users = client.fetchAllUsers()
listuser=[user.uid for user in users if user.uid!="0"] # ดึง uid หรือ id ของทุกคนสำหรับใช้ส่งข้อความ
on=input("input to send : ") # กดพิมพ์อะไรก็ได้เพื่อเริ่มส่ง
if on=="exit": # กดพิมพ์ exit คือออก
    client.logout() # ออกจากระบบ
    sys.exit() #ออกจากโปรแกรม
for id in listuser: # ลูป id เพื่อนทุกคนในเฟส
    client.send(Message(text='Demo Send Meassage with Python'), thread_id=id, thread_type=ThreadType.USER) 
print("hello world :D")
client.logout() # ออกจากระบบ