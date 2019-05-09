def sync_stock_items(system):
    if system == "system1":
        print("running stock sync between local and remote system1")
        print("retrieving remote stock items from system1")
        print("updating local items")
        print("sending update to third party system1")
    elif system == "system2":
        print("running stock sync between local and remote system2")
        print("retrieving remote stock items from system2")
        print("updating local items")
        print("sending update to third party system2")
    elif system == "system3":
        print("running stock sync between local and remote system3")
        print("retrieving remote stock items from system3")
        print("updating local items")
        print("sending update to third party system3")
    else:
        print("no valid system")

def send_transaction(transaction, system):
    if system == "system1":
        print("send transaction to system1:{0!r}".format(transaction))
    elif system == "system2":
        print("send transaction to system2:{0!r}".format(transaction))
    elif system == "system3":
        print("send transaction to system3:{0!r}".format(transaction))
    else:
        print("no valid system")

def main():
    sync_stock_items("system1")
    transaction = {
            "id": 1,
            "items": [
                {
                    "item_id": 1,
                    "amount_purchased": 3,
                    "value": 238
                }
            ]
        }
    send_transaction(transaction, "system1")

if __name__ == "__main__":
    main()