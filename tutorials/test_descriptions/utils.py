import numpy as np

def convert_nanoJansky_to_mag(flux):
    """Convert calibrated nanoJansky flux to AB mag.
    """
    AB_mag_zp_wrt_Jansky = 8.90  # Definition of AB
    # 9 is from nano=10**(-9)
    AB_mag_zp_wrt_nanoJansky = 2.5 * 9 + AB_mag_zp_wrt_Jansky

    return -2.5 * np.log10(flux) + AB_mag_zp_wrt_nanoJansky

def e(ixx,ixy,iyy):
    ixx = np.complex128(ixx)
    ixy = np.complex128(ixy)
    iyy = np.complex128(iyy)
    denom = (ixx+iyy + 2.*np.sqrt(ixx*iyy-ixy**2))
    e = (ixx-iyy+2*ixy*1j)/denom
    return e
