import smtplib
import datetime as dt
import string
import random
import re
import ssl



#--DEBUGGING EMAILS----
g_regex = r'\b[A-Za-z0-9._%+-]+@[GMAIL|gmail]+\.[COM|com]{2,}\b'	#gmail regix only
h_regex = r'\b[A-Za-z0-9._%+-]+@[HOTMAIL|hotmail]+\.[COM|com]{2,}\b'	#hotmail regix only
y_regex = r'\b[A-Za-z0-9._%+-]+@[YAHOO|yahoo]+\.[COM|com]{2,}\b'

#---------------------


#FINAL VALUES
SMTP_SERVER = "smtp.gmail.com"
PORT = 465  			# For SSL
CONFIRMATION_NUMBER_LEN = 16


# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#method for validating email
def validate_email_adress(email):
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        print("Valid Email")
        return True

    else:
        print("Invalid Email")
        exit(1)

#method for confirmation number for user
def get_confirmation_number(length):
    rnd_list = []
    for i in range(length):
        rnd_list.append(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase))
    return ''.join(rnd_list)


current_time = dt.datetime.now()

confirmation_number = get_confirmation_number(CONFIRMATION_NUMBER_LEN)

#get user email from database
test_email = "rojas.depot@gmail.com"
test_pass = "H2oco2hcl@"
message = f"""\
Subject: Purchase Comfirmation

Here is your Confirmation number: {confirmation_number}
Thank You for shopping with Rojas Depot
{current_time}"""

is_valid_email = validate_email_adress(test_email)

context = ssl.create_default_context()

#send from_address to reciever address with message 
with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context ) as server:
    server.login(test_email, test_pass)
    server.sendmail(test_email,'powerboy_2200@hotmail.com' , message)           #sendmail(rojasDepotDummyEmail, 'emailFromDataBase')


