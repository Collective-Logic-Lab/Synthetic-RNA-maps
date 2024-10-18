#####################################################
import numpy as np
# This file is created automatically
def Model(Y,t,pars):
    # Parameters
    k_g1 = pars[0]
    k_g2 = pars[1]
    k_g3 = pars[2]
    k_g4 = pars[3]
    k_g5 = pars[4]
    l_p_g1 = pars[5]
    l_p_g2 = pars[6]
    l_p_g3 = pars[7]
    l_p_g4 = pars[8]
    l_p_g5 = pars[9]
    l_x_g1 = pars[10]
    l_x_g2 = pars[11]
    l_x_g3 = pars[12]
    l_x_g4 = pars[13]
    l_x_g5 = pars[14]
    m_g1 = pars[15]
    m_g2 = pars[16]
    m_g3 = pars[17]
    m_g4 = pars[18]
    m_g5 = pars[19]
    n_g1 = pars[20]
    n_g2 = pars[21]
    n_g3 = pars[22]
    n_g4 = pars[23]
    n_g5 = pars[24]
    omega_g1 = pars[25]
    omega_g2 = pars[26]
    omega_g3 = pars[27]
    omega_g4 = pars[28]
    omega_g5 = pars[29]
    r_g1 = pars[30]
    r_g2 = pars[31]
    r_g3 = pars[32]
    r_g4 = pars[33]
    r_g5 = pars[34]
    sigmaH_g1 = pars[35]
    sigmaH_g2 = pars[36]
    sigmaH_g3 = pars[37]
    sigmaH_g4 = pars[38]
    sigmaH_g5 = pars[39]
    w_g1_g3 = pars[40]
    w_g1_g3_g4 = pars[41]
    w_g1_g4 = pars[42]
    w_g2_g1 = pars[43]
    w_g2_g1_g3 = pars[44]
    w_g2_g1_g3_g4 = pars[45]
    w_g2_g1_g4 = pars[46]
    w_g2_g3 = pars[47]
    w_g2_g3_g4 = pars[48]
    w_g2_g4 = pars[49]
    w_g2_g5 = pars[50]
    w_g2_g5_g1 = pars[51]
    w_g2_g5_g1_g3 = pars[52]
    w_g2_g5_g1_g3_g4 = pars[53]
    w_g2_g5_g1_g4 = pars[54]
    w_g2_g5_g3 = pars[55]
    w_g2_g5_g3_g4 = pars[56]
    w_g2_g5_g4 = pars[57]
    w_g3_g2 = pars[58]
    w_g3_g2_g3 = pars[59]
    w_g3_g2_g3_g4 = pars[60]
    w_g3_g2_g4 = pars[61]
    w_g3_g3 = pars[62]
    w_g3_g3_g4 = pars[63]
    w_g3_g4 = pars[64]
    w_g4_g2 = pars[65]
    w_g4_g2_g3 = pars[66]
    w_g4_g3 = pars[67]
    w_g5_g1 = pars[68]
    w_g5_g1_g4 = pars[69]
    w_g5_g2 = pars[70]
    w_g5_g2_g1 = pars[71]
    w_g5_g2_g1_g4 = pars[72]
    w_g5_g2_g4 = pars[73]
    w_g5_g4 = pars[74]
    # Variables
    x_g1 = Y[0]
    p_g1 = Y[1]
    x_g2 = Y[2]
    p_g2 = Y[3]
    x_g3 = Y[4]
    p_g3 = Y[5]
    x_g4 = Y[6]
    p_g4 = Y[7]
    x_g5 = Y[8]
    p_g5 = Y[9]
    dx_g1 = m_g1*(1./(1. + np.exp(np.sign(- sigmaH_g1*( omega_g1 + w_g1_g3*p_g3 + w_g1_g4*p_g4 + w_g1_g3_g4*p_g3*p_g4))*min(10.,abs(- sigmaH_g1*( omega_g1 + w_g1_g3*p_g3 + w_g1_g4*p_g4 + w_g1_g3_g4*p_g3*p_g4))))))-l_x_g1*x_g1
    dp_g1 = r_g1*x_g1- l_p_g1*p_g1
    dx_g2 = m_g2*(1./(1. + np.exp(np.sign(- sigmaH_g2*( omega_g2 + w_g2_g5*p_g5 + w_g2_g1*p_g1 + w_g2_g3*p_g3 + w_g2_g4*p_g4 + w_g2_g5_g1*p_g5*p_g1 + w_g2_g5_g3*p_g5*p_g3 + w_g2_g5_g4*p_g5*p_g4 + w_g2_g1_g3*p_g1*p_g3 + w_g2_g1_g4*p_g1*p_g4 + w_g2_g3_g4*p_g3*p_g4 + w_g2_g5_g1_g3*p_g5*p_g1*p_g3 + w_g2_g5_g1_g4*p_g5*p_g1*p_g4 + w_g2_g5_g3_g4*p_g5*p_g3*p_g4 + w_g2_g1_g3_g4*p_g1*p_g3*p_g4 + w_g2_g5_g1_g3_g4*p_g5*p_g1*p_g3*p_g4))*min(10.,abs(- sigmaH_g2*( omega_g2 + w_g2_g5*p_g5 + w_g2_g1*p_g1 + w_g2_g3*p_g3 + w_g2_g4*p_g4 + w_g2_g5_g1*p_g5*p_g1 + w_g2_g5_g3*p_g5*p_g3 + w_g2_g5_g4*p_g5*p_g4 + w_g2_g1_g3*p_g1*p_g3 + w_g2_g1_g4*p_g1*p_g4 + w_g2_g3_g4*p_g3*p_g4 + w_g2_g5_g1_g3*p_g5*p_g1*p_g3 + w_g2_g5_g1_g4*p_g5*p_g1*p_g4 + w_g2_g5_g3_g4*p_g5*p_g3*p_g4 + w_g2_g1_g3_g4*p_g1*p_g3*p_g4 + w_g2_g5_g1_g3_g4*p_g5*p_g1*p_g3*p_g4))))))-l_x_g2*x_g2
    dp_g2 = r_g2*x_g2- l_p_g2*p_g2
    dx_g3 = m_g3*(1./(1. + np.exp(np.sign(- sigmaH_g3*( omega_g3 + w_g3_g2*p_g2 + w_g3_g3*p_g3 + w_g3_g4*p_g4 + w_g3_g2_g3*p_g2*p_g3 + w_g3_g2_g4*p_g2*p_g4 + w_g3_g3_g4*p_g3*p_g4 + w_g3_g2_g3_g4*p_g2*p_g3*p_g4))*min(10.,abs(- sigmaH_g3*( omega_g3 + w_g3_g2*p_g2 + w_g3_g3*p_g3 + w_g3_g4*p_g4 + w_g3_g2_g3*p_g2*p_g3 + w_g3_g2_g4*p_g2*p_g4 + w_g3_g3_g4*p_g3*p_g4 + w_g3_g2_g3_g4*p_g2*p_g3*p_g4))))))-l_x_g3*x_g3
    dp_g3 = r_g3*x_g3- l_p_g3*p_g3
    dx_g4 = m_g4*(1./(1. + np.exp(np.sign(- sigmaH_g4*( omega_g4 + w_g4_g2*p_g2 + w_g4_g3*p_g3 + w_g4_g2_g3*p_g2*p_g3))*min(10.,abs(- sigmaH_g4*( omega_g4 + w_g4_g2*p_g2 + w_g4_g3*p_g3 + w_g4_g2_g3*p_g2*p_g3))))))-l_x_g4*x_g4
    dp_g4 = r_g4*x_g4- l_p_g4*p_g4
    dx_g5 = m_g5*(1./(1. + np.exp(np.sign(- sigmaH_g5*( omega_g5 + w_g5_g2*p_g2 + w_g5_g1*p_g1 + w_g5_g4*p_g4 + w_g5_g2_g1*p_g2*p_g1 + w_g5_g2_g4*p_g2*p_g4 + w_g5_g1_g4*p_g1*p_g4 + w_g5_g2_g1_g4*p_g2*p_g1*p_g4))*min(10.,abs(- sigmaH_g5*( omega_g5 + w_g5_g2*p_g2 + w_g5_g1*p_g1 + w_g5_g4*p_g4 + w_g5_g2_g1*p_g2*p_g1 + w_g5_g2_g4*p_g2*p_g4 + w_g5_g1_g4*p_g1*p_g4 + w_g5_g2_g1_g4*p_g2*p_g1*p_g4))))))-l_x_g5*x_g5
    dp_g5 = r_g5*x_g5- l_p_g5*p_g5
    dY = np.array([dx_g1,dp_g1,dx_g2,dp_g2,dx_g3,dp_g3,dx_g4,dp_g4,dx_g5,dp_g5,])
    return(dY)
#####################################################