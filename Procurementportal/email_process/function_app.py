import logging
import azure.functions as func
import traceback

# Fix import 
try:
    from .extraction import start_email_monitoring
except ImportError:
    from email_process.extraction import start_email_monitoring  # fallback

def main(mytimer: func.TimerRequest) -> None:
    logging.info("Timer trigger executed.")
    
    try:
        start_email_monitoring()  
    except Exception as e:
        logging.error(f"Error during email monitoring: {e}")
        logging.error("Traceback:\n" + traceback.format_exc())
