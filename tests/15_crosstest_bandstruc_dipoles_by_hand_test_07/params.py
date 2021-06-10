# Input parameters for SBE.py
import numpy as np

class params:
    # System parameters
    #########################################################################
    e_fermi             = 0.0                    # Fermi energy in eV
    temperature         = 0.0                    # Temperature in eV

    # Model Hamiltonian parameters
    # Brillouin zone parameters
    ##########################################################################
    # Type of Brillouin zone
    BZ_type             = 'rectangle'            # rectangle or hexagon
    Nk1                 = 600                     # Number of kpoints in each of the paths
    Nk2                 = 1                      # Number of paths
    length_BZ_E_dir     = 2*np.pi/6.0            # length of BZ in E-field direction
    length_BZ_ortho     = 0.1                    # length of BZ orthogonal to E-field direction
    angle_inc_E_field   = 0                      # incoming angle of the E-field in degree

    # Driving field parameters
    ##########################################################################
    E0                  = 10.0                   # Pulse amplitude (MV/cm)
    f                   = 25.0                   # Pulse frequency (THz)
    chirp               = np.linspace(-1.4,1.4,15)                   # Pulse chirp ratio (chirp = c/w) (THz)
    sigma               = 45.0                   # Gaussian pulse width (femtoseconds)
    phase               = np.linspace(0,2*np.pi,96)
    solver_method       = 'rk4'

    # Time scales (all units in femtoseconds)
    ##########################################################################
    T1                  = 1000                   # Phenomenological diagonal damping time
    T2                  = 1                      # Phenomenological polarization damping time
    t0                  = -1000                  # Start time *pulse centered @ t=0, use t0 << 0
    dt                  = 0.01                   # Time step

    # Flags for testing and features
    ##########################################################################
    gauge                   = 'length'           # Gauge of the system
    solver                  = '2band'
    fourier_window_function = 'gaussian'
    factor_freq_resolution  = 10
    user_out                = True
    path_parallelization    = False
