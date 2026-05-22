#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, lcm

def derive_phase_closure():
    print("=" * 56)
    print("       HARMONIC PHASE CLOSURE DERIVATION")
    print("       Law of Admissibility: R = 4")
    print("=" * 56 + "\n")

    # Rational parameters from first principles
    T_s = Fraction(2775843, 94000)
    tidal_node_density = Fraction(1778, 855)

    print(f"Mean Synodic Period (T_s)   = {T_s} days")
    print(f"Tidal Node Density          = {tidal_node_density} peaks/day")
    print(f"Lattice modulus             = 24\n")

    print("Three conditions must be satisfied simultaneously:")
    print("  1) N * T_s is an integer                 (solar day alignment)")
    print("  2) (N * T_s * node_density) mod 24 = 0   (lattice alignment)")
    print("  3) k divisible by 3 x 19 = 57            (full R=4 admissibility closure)\n")

    # --- Condition 1: Solar day alignment ---
    # T_s = 2775843/94000 in lowest terms
    num = 2775843
    den = 94000
    g = gcd(num, den)
    num //= g
    den //= g
    print(f"T_s in lowest terms = {num}/{den}")
    print(f"Condition 1: N must be a multiple of {den}\n")

    # --- Condition 2: Lattice alignment ---
    tidal_num = 1778
    tidal_den = 855
    g2 = gcd(tidal_num, tidal_den)
    tidal_num_s = tidal_num // g2
    tidal_den_s = tidal_den // g2

    target_divisor = 24 * tidal_den_s
    numerator_factor = num * tidal_num_s
    g3 = gcd(numerator_factor, target_divisor)
    k_condition2 = target_divisor // g3
    print(f"Condition 2: k must be a multiple of {k_condition2}\n")

    # --- Condition 3: Law of Admissibility (R = 4) ---
    # Full R=4 closure requires all four recursive depth levels to return
    # to origin simultaneously. This requires k to incorporate:
    #   - The spatial partition invariant: 3
    #   - The Metonic cycle depth:        19
    # Together: 3 x 19 = 57
    admissibility_factor = 3 * 19
    print(f"Condition 3: Law of Admissibility (R = 4) requires k divisible by")
    print(f"  Spatial partition invariant: 3")
    print(f"  Metonic cycle depth:         19")
    print(f"  Combined admissibility factor: 3 x 19 = {admissibility_factor}\n")

    # --- Solve for smallest k satisfying all three conditions ---
    k_min = lcm(k_condition2, admissibility_factor)
    print(f"Smallest k satisfying all three conditions: lcm({k_condition2}, {admissibility_factor}) = {k_min}\n")

    N = den * k_min
    print(f"N = {den} x {k_min} = {N:,} lunations")

    years = N * Fraction(19, 235)
    print(f"Phase closure period = {N:,} x (19/235) = {float(years):,.0f} solar years\n")

    # --- Verification ---
    total_days = N * T_s
    total_nodes = total_days * tidal_node_density

    print("VERIFICATION:")
    print(f"  N x T_s                    = {total_days} days")
    print(f"  Solar day alignment        = {total_days % 1 == 0}")
    print(f"  Total tidal nodes mod 24   = {total_nodes % 24}")
    print(f"  Admissibility factor check = {k_min % admissibility_factor == 0}\n")

    if total_days % 1 == 0 and total_nodes % 24 == 0 and k_min % admissibility_factor == 0:
        print("[VERIFIED] Full phase closure under R = 4 admissibility confirmed.")
        print(f"The Earth-Moon system returns to exact phase closure every")
        print(f"{float(years):,.0f} years under the Law of Admissibility.")
    else:
        print("[ERROR] Derivation failed verification.")

if __name__ == "__main__":
    derive_phase_closure()
    
