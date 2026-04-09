# twilio login

"""
twillo
datetime module
time
1. twilio client setup
2. user inputs
3. scheduling logic
4. send message
"""

# step-1 install required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# step-2 twilio credentials
account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

# step-3 degine send message function

def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from = ''
            body = message_body,
            to = f'whatsapp:{recipient_number}'
            )
        print(f'Message sent successfully ! message sid{message.sid})
              except Exception as e:
                  print('an error occurred')


# step-4 user input

name = input('enter the recipient name =')
recipient_number = input('enter the recipient whatsapp number with country code( eg. +19)')
message_body = input(f'enter the message you want to send to {name}:')


# step-5 parse data/time and calculate delay

date_str = input('enter the date to send the message (YYY-MM-DD):')
time_str = input('enter the time to send the message (HH:MM in 24hour format):')

# datetime
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# calculate delay

time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print(' The specified time is in the past. Please enter a future date and time: ')
else:
    print(f' Message scheduled scheduled to be sent to {name} at {schedule_datetime}. ')
    
    # wait until the scheduled time
    time.sleep(delay_seconds)

    # send the message
    send_whatsapp_message(recipient_number, message_body)
                  
