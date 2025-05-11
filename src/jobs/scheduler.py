from apscheduler.schedulers.background import BackgroundScheduler
from src.jobs.monitor_collections import CollectionMonitor
from src.jobs.train_docs import TrainDocsJob
from src.config import AppConfig

scheduler = BackgroundScheduler()
collectionMonitorJob = CollectionMonitor()
trainJob = TrainDocsJob()
config = AppConfig()

query = "Find the PR ratio of RPPInfra"
scheduler.add_job(lambda: trainJob.process(config.collectionName), 'cron', minute='*')
scheduler.add_job(lambda: collectionMonitorJob.query_by_tag(query, collection_name= config.collectionName), 'cron', minute='*')
scheduler.start()

try:
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()