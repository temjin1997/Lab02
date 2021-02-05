from ncclient import manager


router = {"host": "10.50.50.20", "port": "22",
          "username": "cisco", "password": "cisco"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    m.close_session()