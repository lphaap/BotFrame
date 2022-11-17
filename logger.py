from datetime import datetime;

# Log given msg to console
def log( msg: str) -> None:

    if(type(msg) is not str):
        msg = str(msg);

    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S");
    print(timestamp + ": " + msg);