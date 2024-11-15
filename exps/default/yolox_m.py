#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.67
        self.width = 0.75
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]
        self.num_classes = 12
        # seed
        self.seed = 241113
        
        # Define yourself dataset path
        self.data_dir = None
        self.train_ann = "train.json"
        self.val_ann = "test.json"
        self.test_ann = "validation.json"

        self.max_epoch = 300
        self.data_num_workers = 4
        self.eval_interval = 1