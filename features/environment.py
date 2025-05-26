import sys
from process_handler import ProcessHandler 


def before_all(context):

    server_ip = context.config.userdata.get("server_ip", "127.0.0.1")

    try:
        context.process = ProcessHandler(server_ip)
        if (not context.process.is_connection_successful()):
            print("Error: Connection to the server failed.")
            sys.exit(1) 
    except Exception as e:
        print(f"Error while connecting to the server: {e}")
        sys.exit(1) 
