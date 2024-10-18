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
    k_g6 = pars[5]
    k_g7 = pars[6]
    k_g8 = pars[7]
    l_p_g1 = pars[8]
    l_p_g2 = pars[9]
    l_p_g3 = pars[10]
    l_p_g4 = pars[11]
    l_p_g5 = pars[12]
    l_p_g6 = pars[13]
    l_p_g7 = pars[14]
    l_p_g8 = pars[15]
    l_x_g1 = pars[16]
    l_x_g2 = pars[17]
    l_x_g3 = pars[18]
    l_x_g4 = pars[19]
    l_x_g5 = pars[20]
    l_x_g6 = pars[21]
    l_x_g7 = pars[22]
    l_x_g8 = pars[23]
    m_g1 = pars[24]
    m_g2 = pars[25]
    m_g3 = pars[26]
    m_g4 = pars[27]
    m_g5 = pars[28]
    m_g6 = pars[29]
    m_g7 = pars[30]
    m_g8 = pars[31]
    n_g1 = pars[32]
    n_g2 = pars[33]
    n_g3 = pars[34]
    n_g4 = pars[35]
    n_g5 = pars[36]
    n_g6 = pars[37]
    n_g7 = pars[38]
    n_g8 = pars[39]
    omega_g1 = pars[40]
    omega_g2 = pars[41]
    omega_g3 = pars[42]
    omega_g4 = pars[43]
    omega_g5 = pars[44]
    omega_g6 = pars[45]
    omega_g7 = pars[46]
    omega_g8 = pars[47]
    r_g1 = pars[48]
    r_g2 = pars[49]
    r_g3 = pars[50]
    r_g4 = pars[51]
    r_g5 = pars[52]
    r_g6 = pars[53]
    r_g7 = pars[54]
    r_g8 = pars[55]
    sigmaH_g1 = pars[56]
    sigmaH_g2 = pars[57]
    sigmaH_g3 = pars[58]
    sigmaH_g4 = pars[59]
    sigmaH_g5 = pars[60]
    sigmaH_g6 = pars[61]
    sigmaH_g7 = pars[62]
    sigmaH_g8 = pars[63]
    w_g1_g2 = pars[64]
    w_g1_g2_g4 = pars[65]
    w_g1_g3 = pars[66]
    w_g1_g3_g2 = pars[67]
    w_g1_g3_g2_g4 = pars[68]
    w_g1_g3_g4 = pars[69]
    w_g1_g4 = pars[70]
    w_g1_g5 = pars[71]
    w_g1_g5_g2 = pars[72]
    w_g1_g5_g2_g4 = pars[73]
    w_g1_g5_g3 = pars[74]
    w_g1_g5_g3_g2 = pars[75]
    w_g1_g5_g3_g2_g4 = pars[76]
    w_g1_g5_g3_g4 = pars[77]
    w_g1_g5_g4 = pars[78]
    w_g2_g1 = pars[79]
    w_g2_g3 = pars[80]
    w_g2_g3_g1 = pars[81]
    w_g2_g6 = pars[82]
    w_g2_g6_g1 = pars[83]
    w_g2_g6_g3 = pars[84]
    w_g2_g6_g3_g1 = pars[85]
    w_g2_g7 = pars[86]
    w_g2_g7_g1 = pars[87]
    w_g2_g7_g3 = pars[88]
    w_g2_g7_g3_g1 = pars[89]
    w_g2_g7_g6 = pars[90]
    w_g2_g7_g6_g1 = pars[91]
    w_g2_g7_g6_g3 = pars[92]
    w_g2_g7_g6_g3_g1 = pars[93]
    w_g3_g1 = pars[94]
    w_g3_g2 = pars[95]
    w_g3_g2_g1 = pars[96]
    w_g3_g8 = pars[97]
    w_g3_g8_g1 = pars[98]
    w_g3_g8_g2 = pars[99]
    w_g3_g8_g2_g1 = pars[100]
    w_g4_g1 = pars[101]
    w_g4_g3 = pars[102]
    w_g4_g3_g1 = pars[103]
    w_g4_g5 = pars[104]
    w_g4_g5_g1 = pars[105]
    w_g4_g5_g3 = pars[106]
    w_g4_g5_g3_g1 = pars[107]
    w_g5_g1 = pars[108]
    w_g5_g1_g4 = pars[109]
    w_g5_g2 = pars[110]
    w_g5_g2_g1 = pars[111]
    w_g5_g2_g1_g4 = pars[112]
    w_g5_g2_g4 = pars[113]
    w_g5_g4 = pars[114]
    w_g5_g6 = pars[115]
    w_g5_g6_g1 = pars[116]
    w_g5_g6_g1_g4 = pars[117]
    w_g5_g6_g2 = pars[118]
    w_g5_g6_g2_g1 = pars[119]
    w_g5_g6_g2_g1_g4 = pars[120]
    w_g5_g6_g2_g4 = pars[121]
    w_g5_g6_g4 = pars[122]
    w_g6_g3 = pars[123]
    w_g6_g5 = pars[124]
    w_g6_g5_g3 = pars[125]
    w_g6_g5_g7 = pars[126]
    w_g6_g5_g7_g3 = pars[127]
    w_g6_g5_g7_g8 = pars[128]
    w_g6_g5_g7_g8_g3 = pars[129]
    w_g6_g5_g8 = pars[130]
    w_g6_g5_g8_g3 = pars[131]
    w_g6_g7 = pars[132]
    w_g6_g7_g3 = pars[133]
    w_g6_g7_g8 = pars[134]
    w_g6_g7_g8_g3 = pars[135]
    w_g6_g8 = pars[136]
    w_g6_g8_g3 = pars[137]
    w_g7_g1 = pars[138]
    w_g7_g2 = pars[139]
    w_g7_g2_g1 = pars[140]
    w_g7_g6 = pars[141]
    w_g7_g6_g1 = pars[142]
    w_g7_g6_g2 = pars[143]
    w_g7_g6_g2_g1 = pars[144]
    w_g8_g2 = pars[145]
    w_g8_g2_g4 = pars[146]
    w_g8_g4 = pars[147]
    w_g8_g6 = pars[148]
    w_g8_g6_g2 = pars[149]
    w_g8_g6_g2_g4 = pars[150]
    w_g8_g6_g4 = pars[151]
    w_g8_g7 = pars[152]
    w_g8_g7_g2 = pars[153]
    w_g8_g7_g2_g4 = pars[154]
    w_g8_g7_g4 = pars[155]
    w_g8_g7_g6 = pars[156]
    w_g8_g7_g6_g2 = pars[157]
    w_g8_g7_g6_g2_g4 = pars[158]
    w_g8_g7_g6_g4 = pars[159]
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
    x_g6 = Y[10]
    p_g6 = Y[11]
    x_g7 = Y[12]
    p_g7 = Y[13]
    x_g8 = Y[14]
    p_g8 = Y[15]
    dx_g1 = m_g1*(1./(1. + np.exp(np.sign(- sigmaH_g1*( omega_g1 + w_g1_g5*p_g5 + w_g1_g3*p_g3 + w_g1_g2*p_g2 + w_g1_g4*p_g4 + w_g1_g5_g3*p_g5*p_g3 + w_g1_g5_g2*p_g5*p_g2 + w_g1_g5_g4*p_g5*p_g4 + w_g1_g3_g2*p_g3*p_g2 + w_g1_g3_g4*p_g3*p_g4 + w_g1_g2_g4*p_g2*p_g4 + w_g1_g5_g3_g2*p_g5*p_g3*p_g2 + w_g1_g5_g3_g4*p_g5*p_g3*p_g4 + w_g1_g5_g2_g4*p_g5*p_g2*p_g4 + w_g1_g3_g2_g4*p_g3*p_g2*p_g4 + w_g1_g5_g3_g2_g4*p_g5*p_g3*p_g2*p_g4))*min(10.,abs(- sigmaH_g1*( omega_g1 + w_g1_g5*p_g5 + w_g1_g3*p_g3 + w_g1_g2*p_g2 + w_g1_g4*p_g4 + w_g1_g5_g3*p_g5*p_g3 + w_g1_g5_g2*p_g5*p_g2 + w_g1_g5_g4*p_g5*p_g4 + w_g1_g3_g2*p_g3*p_g2 + w_g1_g3_g4*p_g3*p_g4 + w_g1_g2_g4*p_g2*p_g4 + w_g1_g5_g3_g2*p_g5*p_g3*p_g2 + w_g1_g5_g3_g4*p_g5*p_g3*p_g4 + w_g1_g5_g2_g4*p_g5*p_g2*p_g4 + w_g1_g3_g2_g4*p_g3*p_g2*p_g4 + w_g1_g5_g3_g2_g4*p_g5*p_g3*p_g2*p_g4))))))-l_x_g1*x_g1
    dp_g1 = r_g1*x_g1- l_p_g1*p_g1
    dx_g2 = m_g2*(1./(1. + np.exp(np.sign(- sigmaH_g2*( omega_g2 + w_g2_g7*p_g7 + w_g2_g6*p_g6 + w_g2_g3*p_g3 + w_g2_g1*p_g1 + w_g2_g7_g6*p_g7*p_g6 + w_g2_g7_g3*p_g7*p_g3 + w_g2_g7_g1*p_g7*p_g1 + w_g2_g6_g3*p_g6*p_g3 + w_g2_g6_g1*p_g6*p_g1 + w_g2_g3_g1*p_g3*p_g1 + w_g2_g7_g6_g3*p_g7*p_g6*p_g3 + w_g2_g7_g6_g1*p_g7*p_g6*p_g1 + w_g2_g7_g3_g1*p_g7*p_g3*p_g1 + w_g2_g6_g3_g1*p_g6*p_g3*p_g1 + w_g2_g7_g6_g3_g1*p_g7*p_g6*p_g3*p_g1))*min(10.,abs(- sigmaH_g2*( omega_g2 + w_g2_g7*p_g7 + w_g2_g6*p_g6 + w_g2_g3*p_g3 + w_g2_g1*p_g1 + w_g2_g7_g6*p_g7*p_g6 + w_g2_g7_g3*p_g7*p_g3 + w_g2_g7_g1*p_g7*p_g1 + w_g2_g6_g3*p_g6*p_g3 + w_g2_g6_g1*p_g6*p_g1 + w_g2_g3_g1*p_g3*p_g1 + w_g2_g7_g6_g3*p_g7*p_g6*p_g3 + w_g2_g7_g6_g1*p_g7*p_g6*p_g1 + w_g2_g7_g3_g1*p_g7*p_g3*p_g1 + w_g2_g6_g3_g1*p_g6*p_g3*p_g1 + w_g2_g7_g6_g3_g1*p_g7*p_g6*p_g3*p_g1))))))-l_x_g2*x_g2
    dp_g2 = r_g2*x_g2- l_p_g2*p_g2
    dx_g3 = m_g3*(1./(1. + np.exp(np.sign(- sigmaH_g3*( omega_g3 + w_g3_g8*p_g8 + w_g3_g2*p_g2 + w_g3_g1*p_g1 + w_g3_g8_g2*p_g8*p_g2 + w_g3_g8_g1*p_g8*p_g1 + w_g3_g2_g1*p_g2*p_g1 + w_g3_g8_g2_g1*p_g8*p_g2*p_g1))*min(10.,abs(- sigmaH_g3*( omega_g3 + w_g3_g8*p_g8 + w_g3_g2*p_g2 + w_g3_g1*p_g1 + w_g3_g8_g2*p_g8*p_g2 + w_g3_g8_g1*p_g8*p_g1 + w_g3_g2_g1*p_g2*p_g1 + w_g3_g8_g2_g1*p_g8*p_g2*p_g1))))))-l_x_g3*x_g3
    dp_g3 = r_g3*x_g3- l_p_g3*p_g3
    dx_g4 = m_g4*(1./(1. + np.exp(np.sign(- sigmaH_g4*( omega_g4 + w_g4_g5*p_g5 + w_g4_g3*p_g3 + w_g4_g1*p_g1 + w_g4_g5_g3*p_g5*p_g3 + w_g4_g5_g1*p_g5*p_g1 + w_g4_g3_g1*p_g3*p_g1 + w_g4_g5_g3_g1*p_g5*p_g3*p_g1))*min(10.,abs(- sigmaH_g4*( omega_g4 + w_g4_g5*p_g5 + w_g4_g3*p_g3 + w_g4_g1*p_g1 + w_g4_g5_g3*p_g5*p_g3 + w_g4_g5_g1*p_g5*p_g1 + w_g4_g3_g1*p_g3*p_g1 + w_g4_g5_g3_g1*p_g5*p_g3*p_g1))))))-l_x_g4*x_g4
    dp_g4 = r_g4*x_g4- l_p_g4*p_g4
    dx_g5 = m_g5*(1./(1. + np.exp(np.sign(- sigmaH_g5*( omega_g5 + w_g5_g6*p_g6 + w_g5_g2*p_g2 + w_g5_g1*p_g1 + w_g5_g4*p_g4 + w_g5_g6_g2*p_g6*p_g2 + w_g5_g6_g1*p_g6*p_g1 + w_g5_g6_g4*p_g6*p_g4 + w_g5_g2_g1*p_g2*p_g1 + w_g5_g2_g4*p_g2*p_g4 + w_g5_g1_g4*p_g1*p_g4 + w_g5_g6_g2_g1*p_g6*p_g2*p_g1 + w_g5_g6_g2_g4*p_g6*p_g2*p_g4 + w_g5_g6_g1_g4*p_g6*p_g1*p_g4 + w_g5_g2_g1_g4*p_g2*p_g1*p_g4 + w_g5_g6_g2_g1_g4*p_g6*p_g2*p_g1*p_g4))*min(10.,abs(- sigmaH_g5*( omega_g5 + w_g5_g6*p_g6 + w_g5_g2*p_g2 + w_g5_g1*p_g1 + w_g5_g4*p_g4 + w_g5_g6_g2*p_g6*p_g2 + w_g5_g6_g1*p_g6*p_g1 + w_g5_g6_g4*p_g6*p_g4 + w_g5_g2_g1*p_g2*p_g1 + w_g5_g2_g4*p_g2*p_g4 + w_g5_g1_g4*p_g1*p_g4 + w_g5_g6_g2_g1*p_g6*p_g2*p_g1 + w_g5_g6_g2_g4*p_g6*p_g2*p_g4 + w_g5_g6_g1_g4*p_g6*p_g1*p_g4 + w_g5_g2_g1_g4*p_g2*p_g1*p_g4 + w_g5_g6_g2_g1_g4*p_g6*p_g2*p_g1*p_g4))))))-l_x_g5*x_g5
    dp_g5 = r_g5*x_g5- l_p_g5*p_g5
    dx_g6 = m_g6*(1./(1. + np.exp(np.sign(- sigmaH_g6*( omega_g6 + w_g6_g5*p_g5 + w_g6_g7*p_g7 + w_g6_g8*p_g8 + w_g6_g3*p_g3 + w_g6_g5_g7*p_g5*p_g7 + w_g6_g5_g8*p_g5*p_g8 + w_g6_g5_g3*p_g5*p_g3 + w_g6_g7_g8*p_g7*p_g8 + w_g6_g7_g3*p_g7*p_g3 + w_g6_g8_g3*p_g8*p_g3 + w_g6_g5_g7_g8*p_g5*p_g7*p_g8 + w_g6_g5_g7_g3*p_g5*p_g7*p_g3 + w_g6_g5_g8_g3*p_g5*p_g8*p_g3 + w_g6_g7_g8_g3*p_g7*p_g8*p_g3 + w_g6_g5_g7_g8_g3*p_g5*p_g7*p_g8*p_g3))*min(10.,abs(- sigmaH_g6*( omega_g6 + w_g6_g5*p_g5 + w_g6_g7*p_g7 + w_g6_g8*p_g8 + w_g6_g3*p_g3 + w_g6_g5_g7*p_g5*p_g7 + w_g6_g5_g8*p_g5*p_g8 + w_g6_g5_g3*p_g5*p_g3 + w_g6_g7_g8*p_g7*p_g8 + w_g6_g7_g3*p_g7*p_g3 + w_g6_g8_g3*p_g8*p_g3 + w_g6_g5_g7_g8*p_g5*p_g7*p_g8 + w_g6_g5_g7_g3*p_g5*p_g7*p_g3 + w_g6_g5_g8_g3*p_g5*p_g8*p_g3 + w_g6_g7_g8_g3*p_g7*p_g8*p_g3 + w_g6_g5_g7_g8_g3*p_g5*p_g7*p_g8*p_g3))))))-l_x_g6*x_g6
    dp_g6 = r_g6*x_g6- l_p_g6*p_g6
    dx_g7 = m_g7*(1./(1. + np.exp(np.sign(- sigmaH_g7*( omega_g7 + w_g7_g6*p_g6 + w_g7_g2*p_g2 + w_g7_g1*p_g1 + w_g7_g6_g2*p_g6*p_g2 + w_g7_g6_g1*p_g6*p_g1 + w_g7_g2_g1*p_g2*p_g1 + w_g7_g6_g2_g1*p_g6*p_g2*p_g1))*min(10.,abs(- sigmaH_g7*( omega_g7 + w_g7_g6*p_g6 + w_g7_g2*p_g2 + w_g7_g1*p_g1 + w_g7_g6_g2*p_g6*p_g2 + w_g7_g6_g1*p_g6*p_g1 + w_g7_g2_g1*p_g2*p_g1 + w_g7_g6_g2_g1*p_g6*p_g2*p_g1))))))-l_x_g7*x_g7
    dp_g7 = r_g7*x_g7- l_p_g7*p_g7
    dx_g8 = m_g8*(1./(1. + np.exp(np.sign(- sigmaH_g8*( omega_g8 + w_g8_g7*p_g7 + w_g8_g6*p_g6 + w_g8_g2*p_g2 + w_g8_g4*p_g4 + w_g8_g7_g6*p_g7*p_g6 + w_g8_g7_g2*p_g7*p_g2 + w_g8_g7_g4*p_g7*p_g4 + w_g8_g6_g2*p_g6*p_g2 + w_g8_g6_g4*p_g6*p_g4 + w_g8_g2_g4*p_g2*p_g4 + w_g8_g7_g6_g2*p_g7*p_g6*p_g2 + w_g8_g7_g6_g4*p_g7*p_g6*p_g4 + w_g8_g7_g2_g4*p_g7*p_g2*p_g4 + w_g8_g6_g2_g4*p_g6*p_g2*p_g4 + w_g8_g7_g6_g2_g4*p_g7*p_g6*p_g2*p_g4))*min(10.,abs(- sigmaH_g8*( omega_g8 + w_g8_g7*p_g7 + w_g8_g6*p_g6 + w_g8_g2*p_g2 + w_g8_g4*p_g4 + w_g8_g7_g6*p_g7*p_g6 + w_g8_g7_g2*p_g7*p_g2 + w_g8_g7_g4*p_g7*p_g4 + w_g8_g6_g2*p_g6*p_g2 + w_g8_g6_g4*p_g6*p_g4 + w_g8_g2_g4*p_g2*p_g4 + w_g8_g7_g6_g2*p_g7*p_g6*p_g2 + w_g8_g7_g6_g4*p_g7*p_g6*p_g4 + w_g8_g7_g2_g4*p_g7*p_g2*p_g4 + w_g8_g6_g2_g4*p_g6*p_g2*p_g4 + w_g8_g7_g6_g2_g4*p_g7*p_g6*p_g2*p_g4))))))-l_x_g8*x_g8
    dp_g8 = r_g8*x_g8- l_p_g8*p_g8
    dY = np.array([dx_g1,dp_g1,dx_g2,dp_g2,dx_g3,dp_g3,dx_g4,dp_g4,dx_g5,dp_g5,dx_g6,dp_g6,dx_g7,dp_g7,dx_g8,dp_g8,])
    return(dY)
#####################################################