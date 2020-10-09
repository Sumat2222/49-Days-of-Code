from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from main import send_msg

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_msg, 'interval', seconds=10)

sched.start()