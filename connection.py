class Connection:

    def __init__(self,
                 client_name,
                 ip='127.0.0.1',
                 rpc_port=50000,
                 stream_port=50001):
        import krpc
        self.conn = krpc.connect(client_name, ip, rpc_port, stream_port)

    def get_active_vessel(self):
        return self.conn.space_center.active_vessel

    def get_connection_object(self):
        return self.conn
