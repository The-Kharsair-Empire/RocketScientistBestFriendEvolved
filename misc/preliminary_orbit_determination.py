import krpc
from customMath import vec3d
from customMath.vec3d import Vec3D
from math import acos


def od_from_position_and_velocity(position: tuple[float, float, float], velocity: tuple[float, float, float],
                                  time: float, vessel):
    parent_body = vessel.orbit.body
    mu = parent_body.gravitational_parameter

    velocity = Vec3D(velocity[0], velocity[1], velocity[2])
    position = Vec3D(position[0], position[1], position[2])

    kci_z_axis = Vec3D(0, 0, 1)
    kci_x_axis = Vec3D(1, 0, 0)
    kci_y_axis = Vec3D(0, 1, 0)

    v = vec3d.l2_norm(velocity)
    r = vec3d.l2_norm(position)
    energy = v * v / 2 - mu / r
    semi_major_axis = -mu / 2 * energy

    angular_momentum_vector = vec3d.vec_crs(position, velocity)
    eccentricity_vector = (vec3d.vec_crs(velocity, angular_momentum_vector) / mu) - (position / r)
    eccentricity = vec3d.l2_norm(eccentricity_vector)

    inclination = acos(vec3d.vec_dot(angular_momentum_vector, kci_y_axis) / vec3d.l2_norm(angular_momentum_vector))

    n_vector = vec3d.vec_crs(kci_y_axis, angular_momentum_vector)
    longitude_of_ascending_node = acos(vec3d.vec_dot(kci_x_axis, n_vector) / vec3d.l2_norm(n_vector))

    if vec3d.vec_dot(n_vector, kci_z_axis) >= 0:
        print("0 <= LAN <= pi")
    elif vec3d.vec_dot(n_vector, kci_z_axis) < 0:
        print("pi < LAN < 2pi")

    argument_of_periapsis = acos(vec3d.vec_dot(n_vector, eccentricity_vector) / (vec3d.l2_norm(n_vector) * eccentricity))

    if vec3d.vec_dot(eccentricity_vector, kci_y_axis) >= 0:
        print("0 <= Arg Pe <= pi")
    elif vec3d.vec_dot(eccentricity_vector, kci_y_axis) < 0:
        print("pi < Arg Pe < 2pi")

    argument_of_latitude = acos(vec3d.vec_dot(n_vector, position) / (vec3d.l2_norm(n_vector) * r))
    print(argument_of_latitude)
    if vec3d.vec_dot(position, kci_y_axis) >= 0:
        print("0 <= u <= pi")
    elif vec3d.vec_dot(position, kci_y_axis) < 0:
        print("pi < u  < 2pi")

    true_anomaly = argument_of_latitude + argument_of_periapsis

    return semi_major_axis, eccentricity, inclination, longitude_of_ascending_node, argument_of_periapsis, true_anomaly
