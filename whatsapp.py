import pywhatkit as pwk

phone_number = "+916363275937"

message = "Hello this is an automated message sent using python! Please Dont reply It"
hour = 13
minute = 3

pwk.sendwhatmsg(phone_number,message,hour,minute)