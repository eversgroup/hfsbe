import numpy as np
import sbe.dipole
from sbe.dipole import diagonalize, dipole_elements

def system_containers(P, sys, paths):
    class System():
        pass

    S = System()

    S.hnp = sys.numpy_hamiltonian()

    if P.system == 'ana':

        h_sym, ef_sym, wf_sym, _ediff_sym = sys.eigensystem(gidx=P.gidx)
        S.dipole = sbe.dipole.SymbolicDipole(h_sym, ef_sym, wf_sym)
        S.curvature = sbe.dipole.SymbolicCurvature(h_sym, S.dipole.Ax, S.dipole.Ay)
        P.n = 2

    if P.system == 'num':
        P.n = np.size(S.hnp(kx=0, ky=0)[:, 0])
        S.dipole_x, S.dipole_y = dipole_elements(P, S.hnp, paths)
        S.e, S.wf = diagonalize(P, S.hnp, paths)
        S.curvature = 0   
        S.dipole = 0

    S.dipole_in_path = np.zeros([P.Nk1, P.n, P.n], dtype=P.type_complex_np)
    
    S.dipole_ortho = np.zeros([P.Nk1, P.n, P.n], dtype=P.type_complex_np)
    
    S.e_in_path = np.zeros([P.Nk1, P.n], dtype=P.type_real_np)  

    S.wf_in_path = np.zeros([P.Nk1, P.n, P.n], dtype=P.type_complex_np)
    
    return S