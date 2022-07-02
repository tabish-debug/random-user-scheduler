from apscheduler.schedulers.background import BackgroundScheduler
from web.connector.trigger import add_data
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

import pytz
import atexit

executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

scheduler = BackgroundScheduler(executors=executors, job_defaults=job_defaults, timezone=pytz.utc)

scheduler.add_jobstore('sqlalchemy', url='sqlite:///web/database/demicon.db')
job = scheduler.add_job(add_data.save_data, 'interval', seconds=20)

atexit.register(scheduler.remove_job, job_id=job.id)
 