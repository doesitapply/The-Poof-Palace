import time
from apscheduler.schedulers.blocking import BlockingScheduler
from modules.orchestrator import Orchestrator
from modules.secure_config import load_secure_config

def main():
    """Main execution function."""
    print("--- Initializing The Poof Palace Engine ---")
    
    # Load secure configuration
    try:
        config = load_secure_config()
        print("✅ Secure configuration loaded successfully")
    except Exception as e:
        print(f"❌ Failed to load secure configuration: {e}")
        print("Please run: python setup_security.py")
        return
    
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
