from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title= "*** Take Rest ***",
            message= "Rest is vital for better mental health, increased concentration , reduced stress, improved mood and even a better metabolism.",
            app_icon= "path for image add forward slash",
            timeout= 5)
        time.sleep(60*60)

# pythonw file.py

    
