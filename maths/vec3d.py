from __future__ import annotations

from math import sqrt


class Vec3D:

    def __init__(self, x: float, y: float, z: float):
        self.vec = (x, y, z)
        self.x = x
        self.y = y
        self.z = z

    def __truediv__(self, scalar: float) -> Vec3D:
        return Vec3D(self.vec[0] / scalar, self.vec[1] / scalar, self.vec[2] / scalar)

    def __sub__(self, other_vec3d: Vec3D) -> Vec3D:
        return Vec3D(self.x - other_vec3d.x, self.y - other_vec3d.y, self.z - other_vec3d.z)


def l2_norm(vec3d: Vec3D) -> float:
    return sqrt(vec3d.vec[0] * vec3d.vec[0] + vec3d.vec[1] * vec3d.vec[1] + vec3d.vec[2] * vec3d.vec[2])


def vec_crs(vec1: Vec3D, vec2: Vec3D) -> Vec3D:
    x = vec1.vec[1] * vec2.vec[2] - vec1.vec[2] * vec2.vec[1]
    y = vec1.vec[2] * vec2.vec[0] - vec1.vec[0] * vec2.vec[2]
    z = vec1.vec[0] * vec2.vec[1] - vec1.vec[1] * vec2.vec[0]
    return Vec3D(x, y, z)


def vec_dot(vec1: Vec3D, vec2: Vec3D) -> float:
    return vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z
