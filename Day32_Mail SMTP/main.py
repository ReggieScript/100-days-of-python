import smtplib
import datetime as dt

# test_email=""
# pwd_email=""
# real_email=""

# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#     connection.starttls()
#     connection.login(user=test_email,password=pwd_email)

#     connection.sendmail(from_addr=test_email, to_addrs=real_email, msg="Subject: Hola amorcito\n\nMira lo logre!!! in yo face!!")

#     connection.close()

now=dt.datetime.now()
now.year