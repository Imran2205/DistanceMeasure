
def air_density(p, t, rh):
    t = t + 273.15
    pv_sat = 6.0178 * 10**((7.5 * t) / (t + 237.3))
    p_v = pv_sat * rh
    p_da = p - p_v
    dens = (p_da/(287.058*t)) + (p_v/(461.495*t))
    print(dens)


