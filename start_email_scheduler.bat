@echo off
echo Starting Email Scheduler in background...
start /B pythonw %~dp0\email_scheduler.py
echo Email Scheduler started! Check email_scheduler.log for status. 
