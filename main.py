import yaml
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from modules.orchestrator import Orchestrator

def load_config(path="config.yaml"):
    """Loads the YAML configuration file."""
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def main():
    """Main execution function."""
    print("--- Initializing The Poof Palace Engine ---")
    config = load_config()
    orchestrator = Orchestrator(config)
    
    scheduler = BlockingScheduler()
    
    # Schedule the main content job to run every 8 hours
    scheduler.add_job(orchestrator.run_daily_content_cycle, 'interval', hours=8, id='content_cycle')
    
    # Schedule the community analysis to run once a day
    scheduler.add_job(orchestrator.run_community_analysis_cycle, 'interval', hours=24, id='community_analysis')

    print("--- Scheduler Started. The Palace is now live. ---")
    try:
        next_run = scheduler.get_job('content_cycle').next_run_time
        if next_run:
            print("Next content cycle will run at:", next_run)
        else:
            print("Content cycle scheduled to run every 8 hours")
    except AttributeError:
        print("Content cycle scheduled to run every 8 hours")
        print("Community analysis scheduled to run every 24 hours")

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("--- Shutting down The Poof Palace Engine ---")
        scheduler.shutdown()

if __name__ == "__main__":
    main()
