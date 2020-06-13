import astropy.table as tab
import numpy as np

def mean_igm_flux(paper = 'Becker13'):
    """
    :param paper: default is Becker13
    :return: z, mean flux, 1 sigma error
    """
    """
    exmaple: 
    z, f, e = mean_igm_flux()
    """
    if paper = 'Becker13':
        data = tab.Table.read('./igm/mean_flux_Becker13.fits')
        print('Cite: Becker et al 2013 paper (https://ui.adsabs.harvard.edu/abs/2007ApJ...662...72B/abstract)')

    return data['z'], data['mean_flux'], data['error']