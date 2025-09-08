def connect(**options):
    conn_params = {
        'host': options.get('host', '172.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
    }
    print(conn_params)

connect()
connect(host='172.0.0.1', port=5433)
connect(port=5431, user='shahin', pwd='Password123')