


def main():
    import krpc
    conn = krpc.connect(
        name='client me',
        address='127.0.0.1',
        rpc_port=50000,
        stream_port=50001
    )

    vessel = conn.space_center.active_vessel
    from maths.vec3d import l2_norm, Vec3D
    vessel_position = vessel.position(vessel.orbit.body.non_rotating_reference_frame)
    x_axis_visual_end = (l2_norm(Vec3D(vessel_position[0], vessel_position[1], vessel_position[2])), 0, 0)

    conn.drawing.add_direction(x_axis_visual_end, vessel.orbital_reference_frame)
    print(x_axis_visual_end)

    print(vessel.name)
    print('({})'.format(vessel.position(vessel.orbit.body.reference_frame)))
    from misc.preliminary_orbit_determination import od_from_position_and_velocity
    orbital_elements = od_from_position_and_velocity(vessel.position(vessel.orbit.body.non_rotating_reference_frame),
                                                     vessel.velocity(vessel.orbit.body.non_rotating_reference_frame),
                                                     0, vessel)
    print("Semi-Major Axis (km): {}, Eccentricity: {}, Inclination: {}, LAN: {}, ARG Pe: {}, Ture Anomaly: {}".format(orbital_elements[0] / 1000000
                                                                                                                 , orbital_elements[1]
                                                                                                                 , orbital_elements[2]
                                                                                                                 , orbital_elements[3]
                                                                                                                 , orbital_elements[4]
                                                                                                                 , orbital_elements[5]))

    while True:
        pass



if __name__ == '__main__':
    main()
