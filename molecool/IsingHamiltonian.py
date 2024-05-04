import numpy as np
from .bitstring import *


class IsingHamiltonian:
    """Class for an Ising Hamiltonian of arbitrary dimensionality

    .. math::
        H = \\sum_{\\left<ij\\right>} J_{ij}\\sigma_i\\sigma_j + \\sum_i\\mu_i\\sigma_i

    """

    def __init__(self, Num, J=[[()]], mu=np.zeros(1)):
        """Constructor

        Parameters
        ----------
        J: list of lists of tuples, optional
            Strength of coupling, e.g,
            [(4, -1.1), (6, -.1)]
            [(5, -1.1), (7, -.1)]
        mu: vector, optional
            local fields
        """
        self.N = Num
        self.J = J
        self.mu = mu

    def energy(self, config):
        """Compute energy of configuration, `config`

            .. math::
                E = \\left<\\hat{H}\\right>

        Parameters
        ----------
        config   : BitString
            input configuration

        Returns
        -------
        energy  : float
            Energy of the input configuration
        """
        if len(config.config) != len(self.J):
            pass
            # error("wrong dimension")

        e = 0.0

        for i in range(config.N):
            # print()
            # print(i)
            for j in self.J[i]:
                if j[0] < i:
                    continue
                # print(j)
                if config.config[i] == config.config[j[0]]:
                    e += j[1]
                else:
                    e -= j[1]

        e += np.dot(self.mu, 2 * config.config - 1)
        return e

    def delta_e_for_flip(self, i, config):
        """Compute the energy change incurred if one were to flip the spin at site i

        Parameters
        ----------
        i        : int
            Index of site to flip
        config   : :class:`BitString`
            input configuration

        Returns
        -------
        energy  : list[BitString, float]
            Returns both the flipped config and the energy change

        """
        pass
        # return del_e

    def metropolis_sweep(self, conf, T=1.0):
        """Perform a single sweep through all the sites and return updated configuration

        Parameters
        ----------
        conf   : :class:`BitString`
            input configuration
        T      : int
            Temperature

        Returns
        -------
        conf  : :class:`BitString`
            Returns updated config
        """

    def compute_average_values(self, T):
        """Compute Average values exactly

        Parameters
        ----------
        T      : int
            Temperature

        Returns
        -------
        E  : float
            Energy
        M  : float
            Magnetization
        HC : float
            Heat Capacity
        MS : float
            Magnetic Susceptability
        """
        E = 0.0
        M = 0.0
        Z = 0.0
        EE = 0.0
        MM = 0.0

        conf = BitString(self.N)

        for i in range(2**conf.N):
            conf.set_int_config(i)
            Ei = self.energy(conf)
            Zi = np.exp(-Ei / T)
            E += Ei * Zi
            EE += Ei * Ei * Zi
            Mi = np.sum(2 * conf.config - 1)
            M += Mi * Zi
            MM += Mi * Mi * Zi
            Z += Zi

        E = E / Z
        M = M / Z
        EE = EE / Z
        MM = MM / Z

        HC = (EE - E * E) / (T * T)
        MS = (MM - M * M) / T
        return E, M, HC, MS
    def get_lowest_energy_config(self):

        """the lowest energy config using naive minimization

        
        Returns
        -------
        emin  : double
            minimum energy
        cmin  : BitString
            lowest energy bitstring configuration
        
        """
        emin = 0

        my_bs = BitString(self.N)
        cmin = BitString(self.N)
        for i in range (0, 2**(len(my_bs))):
            my_bs.set_int_config(i)
            
            currentEn = self.energy(my_bs)
            
            if currentEn < emin:
                emin = currentEn
                cmin.set_int_config(i)
            #print(str(currentEn) + " " + str(my_bs))
        return emin, cmin