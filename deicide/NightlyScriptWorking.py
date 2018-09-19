#!/usr/bin/python3

import smtplib
import sqlite3
import schedule
import time
from CredData import *

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sqlite_file = '/home/lojoho/mozillaDjango/db.sqlite3'    # name of the sqlite database file

me = "lojoho@gmail.com"
you = "logan@bringg.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "¨Finally!"
msg['From'] = me
msg['To'] = you


def job():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('select count() from deicide_deicidelist')
    count_results = c.fetchall()

    cr_2 = [item for resp in count_results for item in resp]
    cr_2 = int(cr_2[0])

    if cr_2 > 0:
        c.execute('SELECT Gods_Name FROM deicide_deicidelist')
        all_rows = c.fetchall()

        data1 = ["<li>" + item for resp in all_rows for item in resp]
        data_new = "</li>".join(data1)

        # Create the body of the message (a plain-text and an HTML version).
        text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
        html = ("""\
        <html>
          <head></head>
          <body>
            <p>Holy Shit,<br>
               This Finally worked.<br>
               <h1 style="text-align: center;">
        <ol>{}</ol>
        </h1>
            </p>
          </body>
        </html>
        """.format(data_new))

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred. 
        msg.attach(part1)
        msg.attach(part2)
        # Send the message via local SMTP server.
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        mail.ehlo()

        mail.starttls()

        mail.login(mailU, mailP)
        mail.sendmail(me, you, msg.as_string())

        c.execute('INSERT INTO deicide_deicidelistarchive (Gods_Name, Accusation, created_date) SELECT Gods_Name, Accusation, created_date FROM deicide_deicidelist')
        conn.commit()

        c.execute('DELETE FROM deicide_deicidelist')
        conn.commit()

        conn.close()
        mail.quit()

    else:
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('INSERT INTO deicide_deicidelistarchive (Gods_Name, Accusation, created_date) VALUES ("Nothing entered on This date", "Nothing entered on This date", CURRENT_TIMESTAMP)')
        conn.commit()

        conn.close()

schedule.every().day.at("07:30").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
