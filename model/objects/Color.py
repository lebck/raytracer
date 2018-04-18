from model.linalg.Vector import Vector

CA = Vector(50, 50, 50)
CIN = Vector(255, 255, 255)

KA = 0.1
KD = 0.3
KS = 0.3


def phuong(l, n, d):
    lr = l.orthogonal().normalize()

    l = l.normalize()
    n = n.normalize()
    d = d.normalize()

    print(CA.scale(KA) + CIN.scale(KD) * (l * n) + CIN.scale(KS) * (lr * d.scale(-1)))

    return CA.scale(KA) + CIN.scale(KD) * (l * n) + CIN.scale(KS) * (lr * d.scale(-1))


if __name__ == "__main__":

    v1 = Vector(1, 1, 0)

    print(v1.orthogonal())