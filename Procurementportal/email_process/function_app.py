import logging
import azure.functions as func
import sys
import os
import traceback

# Ensure main.py is importable
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
#from email_process.extraction import start_email_monitoring  # assuming function is in main.py
try:
    from email_process.extraction import fetch_sap_data
    print("✅ Imported successfully")
except Exception as e:
    import traceback
    print("❌ Import failed:", e)
    traceback.print_exc()



def main(mytimer: func.TimerRequest) -> None:
    logging.info("Timer trigger executed.")
    
    try:
        start_email_monitoring()
    except Exception as e:
        logging.error(f"Error during email monitoring: {e}")
        logging.error("Traceback:\n" + traceback.format_exc())
