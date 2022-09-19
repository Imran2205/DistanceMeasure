import math


def air_density(p, t, rh):
    pv_sat = 611 * math.exp(17.27 * t / (t + 237.3))
    p_v = pv_sat * rh
    p_da = p - p_v
    t_k = t + 273.15  # - 273.15
    dens = (p_da / (287.058 * t_k)) + (p_v / (461.495 * t_k))
    return dens


def speed_of_sound_in_air(p, t, rh):
    d_a = air_density(p, t, rh)
    v = math.sqrt(1.399 * (p / d_a))
    return v


def distance_calculator(pressure_pascal, temp_cel, rh_perc, t_ms):
    rh_frac = rh_perc/100
    vel_of_sound = speed_of_sound_in_air(
        p=pressure_pascal,
        t=temp_cel,
        rh=rh_frac
    )
    distance = vel_of_sound * (t_ms / 1000)
    distance = float("{:.1f}".format(distance))
    return distance, vel_of_sound


if __name__ == '__main__':
    dist_, v_s = distance_calculator(70000, 25, 60, 2040)
    print(dist_, v_s)
    dist_, v_s = distance_calculator(121325, 25, 60, 2040)
    print(dist_, v_s)
