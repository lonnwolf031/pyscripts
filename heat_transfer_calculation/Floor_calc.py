#
# Dit betreft berekeningen voor een horizontale vlakke plaat die warmer is dan de omgeving
##
# 60 W/m2 – Een erg goed geïsoleerde ruimte en andere gunstige factoren zoals minimum ventilatieverlies,
# oriëntatie op het zuiden. Het gebouw komt overheen met een energieklasse A.
#
import air_properties

Ts_arr = [20,30,40,50,60,70,80,90]

# Tinf is kamertemperatuur, of: moet worden
Tinf_arr = [0,5,10,15,20]

def berekenOpwarmingRuimte(m, c, Tinf, Ts):
    Q = m * c * (Tinf-Ts)
    return Q

def berekenConductie(materiaaldikte, A, Ts, Tinf):
    k = air_properties.air_properties_df.loc[lambda df: df['tempC'] == Ts]
    Warmteflux = -k * A * ((Ts - Tinf)/materiaaldikte)
    return Warmteflux

def berekenAenp(lengte, breedte):
    A = lengte * breedte
    p = 2 * lengte + 2 * breedte
    return A, p

def berekenConvectie(rho, mu, prandtl, Ts, Tinf):

    # p is omtrek, A is oppervlak, Lc karakteristieke lengtemaat hier voor een horizontale plaat
    Lc = A / p
    # nu is kinematische viscositeit
    nu = mu / rho
    beta = 2 / (Ts + Tinf)
    grashof = (9.81 * beta * (Ts-Tinf) * Lc^3) / (nu^2)

    rayleigh = grashof * prandtl

    if rayleigh in range(10^4, 10^7):
        nusselt = 0.54 * rayleigh^(1/4)
    elif rayleigh in range(10^7, 10^11):
        nusselt = 0.15 * rayleigh^(1/3)
    else:
        print("Could not find Nusselt, Rayleigh is: " + rayleigh)

def berekenStraling():


# Voor 1 vierkante meter

opp = berekenAenp(1, 1)
A = opp[0]
p = opp[1]
