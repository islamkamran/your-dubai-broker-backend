import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

"""**********INFORM USER ABOUT APPROVAL*************"""
def send_user_details_to_client(fname, lname, email,uid,password, role):
    try:

        sender_email = "info@bigstaruae.com"
        sender_password = "j9PYrxJ3eCZt"
        receiver_email = [email]

        # Create a MIME message
        message = MIMEMultipart()
        message["From"] = sender_email
        # message["To"] = receiver_email
        message["To"] = ",".join(receiver_email)
        message["Subject"] = "Account Status Updated"
        # Create the email body
        body = f"Dear User {fname} {lname},\n\nYour account status is created.\nYou have been assigned the role of: {role}.\nKindly use the Following credentials for logging into your Account.\nPassword: {password}\nWebsite: https://test.com\n\n Best Regards,\n Your Dubai Broker."
        message.attach(MIMEText(body, "plain"))
        try:
            # Set up the SMTP server and send the email
            with smtplib.SMTP("smtp.zoho.com", 587) as server:
                server.starttls()  # Secure the connection
                server.login(sender_email, sender_password)  # Log in to your email
                # server.sendmail(sender_email, receiver_email, message.as_string())
                server.sendmail(sender_email, receiver_email, message.as_string())
            print("Requesting Approval email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")
    except Exception as e:
        print(f"Error: {str(e)}")
