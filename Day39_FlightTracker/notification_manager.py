import smtplib

test_email = "regina.crespo.018@gmail.com" #Fill this with your email
pwd_email = "reggie.dev.testing@gmail.com" #Email password

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self,) -> None:
        self.test_email= test_email
        self.pwd_email = pwd_email

    def send_email(self, letter):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=test_email, password=pwd_email)
            connection.sendmail(from_addr=test_email, to_addrs=self.test_email,
                        msg=letter)
            connection.close()