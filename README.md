# Email-Scheduler

A Python script that sends an automated email every 15 minutes.

## Setup

1. Edit `email_scheduler.py` and update the following configuration:
   - `SMTP_SERVER`: Your email provider's SMTP server (e.g., "smtp.gmail.com" for Gmail)
   - `SMTP_PORT`: SMTP port (typically 587 for TLS)
   - `SENDER_EMAIL`: Your email address
   - `SENDER_PASSWORD`: Your email password or app password
   - `RECIPIENT_EMAIL`: The email address that will receive the automated emails
   - `EMAIL_SUBJECT`: Subject line for the emails
   - `EMAIL_BODY`: Content of the emails

2. If using Gmail:
   - You may need to enable "Less secure app access" or create an App Password
   - For Google accounts with 2FA: Create an App Password at https://myaccount.google.com/apppasswords

## Running the Script

```bash
python email_scheduler.py
```

The script will run continuously, sending an email every 15 minutes.

## Running as a Background Service

### Windows

1. Create a batch file `start_email_scheduler.bat` with:
```
@echo off
start /B pythonw scripts/email_scheduler.py
```

2. Add to Windows Task Scheduler to run at system startup

### Linux/Mac

1. Create a systemd service or use cron to run at startup

## Logs

The script creates a log file `email_scheduler.log` in the same directory, which tracks:
- When the script starts
- Each successful email sent
- Any errors encountered 
