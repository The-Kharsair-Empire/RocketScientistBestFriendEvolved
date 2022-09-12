def main():
    import krpc
    conn = krpc.connect(
        name='client me',
        address='127.0.0.1',
        rpc_port=50000,
        stream_port=50001
    )
    vessel = conn.space_center.active_vessel
    print(vessel.name)
    print('({})'.format(vessel.position(vessel.orbit.body.reference_frame)))


if __name__ == '__main__':
    main()
