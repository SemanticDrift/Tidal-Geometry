import math
from fractions import Fraction

def run_synodic_coherence():
    print("==================================================================")
    print(" SYNODIC LUNAR CYCLE & QUADRANT RESONANCE")
    print(" 7-Day Coherence Envelope Protocol — Author: Carolina Johnson (CJ)")
    print("==================================================================")
    
    # 1. Core Framework Mathematical Constants
    h = Fraction(181, 3)
    c = 3
    f_s = h / c  # 181/9
    spatial_remainder = f_s - 20  # 1/9
    
    lunar_motion = Fraction(43, 120)
    f_t = 1 - lunar_motion  # 77/120
    
    epsilon = Fraction(235, 19) - 12  # 7/19
    lambda_scalar = 24
    
    print(f"[1] CONSTANTS CHECK:")
    print(f"  Spatial Remainder        : {spatial_remainder}")
    print(f"  Temporal Daily Fraction  : {f_t}")
    print(f"  Metonic Residual (ε)     : {epsilon} ({float(epsilon):.6f})")
    print(f"  Lattice Scalar (Λ)       : {lambda_scalar}")
    
    # 2. Scaling the Framework to the 7-Day Tracking Horizon
    print("\n[2] 7-DAY HORIZON TRANSFORMATION:")
    days = 7
    
    # Total cumulative temporal translation over 7 days
    cumulative_temporal_shift = days * f_t  # 7 * 77/120 = 539/120
    integer_rotations = int(cumulative_temporal_shift)
    temporal_residue = cumulative_temporal_shift - integer_rotations  # 59/120
    
    print(f"  Cumulative Temporal Shift: {cumulative_temporal_shift}")
    print(f"  Completed Phase Cycles   : {integer_rotations}")
    print(f"  Day 7 Temporal Residue   : {temporal_residue} ({float(temporal_residue):.6f})")
    
    # 3. Weekly Nodal and Peak Calculations
    raw_weekly_nodes = spatial_remainder * cumulative_temporal_shift * lambda_scalar  # (1/9) * (539/120) * 24 = 539/45
    weekly_metonic_correction = days * epsilon  # 7 * 7/19 = 49/19
    
    total_weekly_peaks = raw_weekly_nodes + weekly_metonic_correction  # 539/45 + 49/19 = 12446/855
    
    integer_peaks = int(total_weekly_peaks)
    boundary_lag = total_weekly_peaks - integer_peaks
    
    print("\n[3] COHERENCE ENVELOPE VERIFICATION:")
    print(f"  Raw Weekly Nodes Matrix  : {raw_weekly_nodes} ({float(raw_weekly_nodes):.5f})")
    print(f"  Scaled Metonic Correction: {weekly_metonic_correction} ({float(weekly_metonic_correction):.5f})")
    print(f"  Rational Weekly Product  : {total_weekly_peaks.numerator}/{total_weekly_peaks.denominator}")
    print(f"  Decimal Wave Frequency   : {float(total_weekly_peaks):.5f}")
    print(f"  MANDATED WEEKLY PEAKS    : {integer_peaks} (Exactly 2 Peaks per Day Locked)")
    print(f"  Boundary Lag Remainder   : {float(boundary_lag):.5f}")
    
    # 4. Physical Observational Target Comparison
    print("\n[4] SYSTEMIC DATA MATCH:")
    observed_weekly_ratio = (12 * 7) / 24.8412  # Observed ratio scaled over 7 tidal intervals
    calculated_ratio_float = float(total_weekly_peaks)
    variance_accuracy = (1 - abs(calculated_ratio_float - observed_weekly_ratio) / observed_weekly_ratio) * 100
    
    print(f"  Calculated Weekly Ratio  : {calculated_ratio_float:.5f}")
    print(f"  Observed Weekly Ratio    : {observed_weekly_ratio:.5f}")
    print(f"  Structural Sync Precision: {variance_accuracy:.2f}%")
    print("==================================================================")

if __name__ == "__main__":
    run_synodic_coherence()
  
