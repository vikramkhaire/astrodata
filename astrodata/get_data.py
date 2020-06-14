import astropy.table as tab
import numpy as np
import os

def mean_igm_flux(paper = 'Becker13'):
    """
    :param paper: default is Becker13
    :return: z, mean flux, 1 sigma error
    """
    """
    exmaple: 
    z, f, e = mean_igm_flux()
    """

    path_of_this_file =  os.path.dirname(__file__)

    if paper == 'Becker13':
        data = tab.Table.read(path_of_this_file +'/igm/mean_flux_Becker13.fits')
        print('Cite: Becker et al 2013 paper (https://ui.adsabs.harvard.edu/abs/2013MNRAS.430.2067B/abstract)')


    return data['z'], data['mean_flux'], data['error']
