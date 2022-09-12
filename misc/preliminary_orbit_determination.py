import krpc
from krpc.SpaceCenter import SpaceCenter
from maths import vec3d
from maths.vec3d import Vec3D
from math import acos


def od_from_position_and_velocity(position: tuple[float, float, float], velocity: tuple[float, float, float],
                                  time: float, vessel: SpaceCenter.Vessel):
    parent_body = vessel.orbit.body
    mu = parent_body.gravitational_parameter

    velocity = Vec3D(velocity[0], velocity[1], velocity[2])
    position = Vec3D(position[0], position[1], position[2])

    v = vec3d.l2_norm(velocity)
    r = vec3d.l2_norm(position)
    energy = v * v / 2 - mu / r
    semi_major_axis = -mu / 2 * energy

    angular_momentum_vector = vec3d.vec_crs(position, velocity)
    eccentricity_vector = (vec3d.vec_crs(velocity, angular_momentum_vector) / mu) - (position / r)
    eccentricity = vec3d.l2_norm(eccentricity_vector)

    inclination = acos(vec3d.vec_dot(angular_momentum_vector, Vec3D(0, 1, 0)) / vec3d.l2_norm(angular_momentum_vector))

    return semi_major_axis, eccentricity, inclination
