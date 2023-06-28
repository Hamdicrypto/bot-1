
from func_connections import connect_dydx

if __name__=="__main__":


# Connect to clint

    try:
        client = connect_dydx()
    except Exception as e:
        print(e)
        print("Error connecting to client:", e)
        exit(1)
