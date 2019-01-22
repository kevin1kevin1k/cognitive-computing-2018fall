#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from img_utils import mls_rigid_deformation, mls_rigid_deformation_inv

def demo(fun, fun_inv, name, parts):
    left_wrist, right_wrist, left_knee, right_knee, left_ankle, right_ankle, xc_yc_ = parts
    xc_, yc_ = xc_yc_
    p = np.array([
        [30, 155], [125, 155], [225, 155],
        [100, 235], [160, 235], [85, 295], [180, 293]
    ])
    #
    # q = np.array([
    #     [42, 211], [125, 155], [235, 150],
    #     [80, 235], [140, 235], [85, 295], [180, 295]
    # ])

    xc, yc = [125, 155]
    h, w = 315, 285
    # h_, w_ = 720, 1080
    h_, w_ = 480, 640

    def xy(x_y_):
        x_, y_ = x_y_
        x = xc + (x_ - xc_) * w // w_
        y = yc + (y_ - yc_) * h // h_
        return x, y

    q = np.array([
        xy(right_wrist), [xc, yc], xy(left_wrist),
        xy(right_knee), xy(left_knee), xy(right_ankle), xy(left_ankle)
    ])

    image = plt.imread(os.path.join(sys.path[0], "mr_big_ori.jpg"))

    transformed_image = fun(image, p, q, alpha=1, density=1)
    plt.imshow(transformed_image)
    plt.savefig(name)

    transformed_image = fun_inv(image, p, q, alpha=1, density=1)
    plt.imshow(transformed_image)
    plt.savefig(name + '_inv')

if __name__ == "__main__":
    demo(mls_rigid_deformation, mls_rigid_deformation_inv, "Rigid")
