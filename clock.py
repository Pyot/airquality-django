from apscheduler.schedulers.background import BackgroundScheduler

import StationDataImport

sched = BackgroundScheduler()
dataImport = StationDataImport.GetStationData()

sched.add_job(dataImport, trigger='cron', day_of_week='mon-sun', hour='0-23')

sched.start()
