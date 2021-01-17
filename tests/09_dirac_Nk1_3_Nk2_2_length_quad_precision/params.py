# Input parameters for SBE.py
import numpy as np


class params:
    # System parameters
    #########################################################################
    a                   = 8.304       # Lattice spacing in atomic units (4.395 A)
    e_fermi             = 0.0         # Fermi energy in eV
    temperature         = 0.0         # Temperature in eV

    # Model Hamiltonian parameters
    # Brillouin zone parameters
    ##########################################################################
    # Type of Brillouin zone
    # 'full' for full hexagonal BZ, '2line' for two lines with adjustable size
    BZ_type = '2line'

    # 2line BZ parameters
    # for Fig. 1b in Paper one has to set Nk1 = 1200 and Nk2 = number of paths
    Nk1                 = 3          # Number of kpoints in each of the paths
    Nk2                 = 2          # Number of paths

    rel_dist_to_Gamma   = 0.008      # relative distance (in units of 2pi/a) of both paths to Gamma
    length_path_in_BZ   = 1500*0.00306  # Length of path in BZ K-direction
    angle_inc_E_field   = 0          # incoming angle of the E-field in degree

    # Driving field parameters
    ##########################################################################
    E0                  = 5.00        # Pulse amplitude (MV/cm)
    w                   = 25.0        # Pulse frequency (THz)
    chirp               = 0.00        # Pulse chirp ratio (chirp = c/w) (THz)
    alpha               = 25.0        # Gaussian pulse width (femtoseconds)
    phase               = 0.0
    dk_order            = 2           # only use second order because we only use three k-points in each path
    solver_method       = 'rk4'       # Runge-Kutta 4th order solver
    precision           = 'quadruple' # quadruple precision, only working with rk4

    # Time scales (all units in femtoseconds)
    ##########################################################################
    T1    = 1000     # Phenomenological diagonal damping time
    T2    = 1        # Phenomenological polarization damping time
    t0    = -1000    # Start time *pulse centered @ t=0, use t0 << 0
    dt    = 0.01    # Time step

    # Flags for testing and features
    ##########################################################################
    gauge         = 'length'   # Gauge of the system
    do_semicl     = False      # Turn all dipoles to 0 and use Berry curvature in emission
    user_out      = True       # Set to True to get user plotting and progress output
    save_approx   = True
    save_full     = False
    save_txt      = False

