#-----------------------------------------------------------------------
#Copyright 2019 Centrum Wiskunde & Informatica, Amsterdam
#
#Author: Daniel M. Pelt
#Contact: D.M.Pelt@cwi.nl
#Website: http://dmpelt.github.io/foam_ct_phantom/
#License: MIT
#
#This file is part of foam_ct_phantom, a Python package for generating
#foam-like phantoms for CT.
#-----------------------------------------------------------------------

"""
Example 06: Generate a 4D moving phantom
========================================
"""

import foam_ct_phantom
import h5py
import numpy as np
import pylab as pl
pl.gray()

random_seed = 9876

foam_ct_phantom.MovingFoamPhantom.generate('test_moving.h5','test_phantom.h5',random_seed,-0.75,0.75)

moving_phantom = foam_ct_phantom.MovingFoamPhantom('test_moving.h5')

vol_geom = foam_ct_phantom.VolumeGeometry(256,256,1,3/256)

moving_phantom.generate_volume('test_moving_vol_start.h5', vol_geom, time=0)
moving_phantom.generate_volume('test_moving_vol_end.h5', vol_geom, time=1)

vol0 = foam_ct_phantom.load_volume('test_moving_vol_start.h5')
vol1 = foam_ct_phantom.load_volume('test_moving_vol_end.h5')
pl.imshow(vol0[0])
pl.figure()
pl.imshow(vol1[0])
pl.show()


proj_geom = foam_ct_phantom.ParallelGeometry(256,128,np.linspace(0,4*np.pi,128,False),3/256)
moving_phantom.generate_projections('test_moving_projs.h5', proj_geom)


projs = foam_ct_phantom.load_projections('test_moving_projs.h5')

pl.imshow(projs[0])
pl.figure()
pl.imshow(projs[-1])
pl.show()