import os
import smtplib

#email_address = os.environ.get("email_user")
#email_password = os.environ.get("email_pass")
email_address = "info@solucionesepsilon.com"
email_password = "EPSILONsrm2017"

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_address, email_password)

    subject = "Mensaje del formulario de la web"
    body = "Prueba"

    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail(email_address, "leojrpaniagua@gmail.com", msg)
