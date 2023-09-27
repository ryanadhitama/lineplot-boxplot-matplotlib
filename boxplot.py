#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 05:31:03 2023

@author: ryanadhitama
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)  # Untuk membuat hasil yang dapat direproduksi
n_data = 1000

dki_jakarta = np.random.normal(30, 5, n_data)
jawa_barat = np.random.normal(28, 4, n_data)
jawa_tengah = np.random.normal(32, 6, n_data)
jawa_timur = np.random.normal(27, 3, n_data)
banten = np.random.normal(31, 5, n_data)
yogyakarta = np.random.normal(29, 4, n_data)
bali = np.random.normal(33, 6, n_data)

data = [dki_jakarta, jawa_barat, jawa_tengah, jawa_timur, banten, yogyakarta, bali]
labels = ["DKI", "Jabar", "Jateng", "Jatim", "Banten", "DIY", "Bali"]
 
plt.boxplot(data, patch_artist = True, labels = labels)

plt.show()