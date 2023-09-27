#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 05:19:43 2023

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

# Line plot
plt.figure(figsize=(12, 6))
plt.plot(dki_jakarta, label='DKI Jakarta')
plt.plot(jawa_barat, label='Jawa Barat')
plt.plot(jawa_tengah, label='Jawa Tengah')
plt.plot(jawa_timur, label='Jawa Timur')
plt.plot(banten, label='Banten')
plt.plot(yogyakarta, label='Yogyakarta')
plt.plot(bali, label='Bali')

plt.xlabel('Data ke-')
plt.ylabel('Suhu (°C)')
plt.title('Line Plot Suhu di Tujuh Provinsi')
plt.legend()
plt.grid(True)
plt.show()
