# Tidal Geometry and Phase Closure
### An Annex to the Earth-Moon Framework

**Author:** Carolina Johnson (CJ)  
**Date:** May 2026  
**License:** CC BY 4.0, Attribution required  
**DOI:** [10.5281/zenodo.20338064](https://doi.org/10.5281/zenodo.20338064)  
**ORCID:** [0009-0002-8819-3347](https://orcid.org/0009-0002-8819-3347)  

---

### What This Does

Demonstrates that the dual tidal peak observed in Earth's oceans is a direct geometric consequence of the Earth-Moon harmonic system, derivable from rational fractions alone. No gravitational constant, no continuous mass terms, and no transcendental approximations.

Using the harmonic distance coordinate $h = 181/3$, the lunar daily fraction $77/120$, the Metonic residual $e = 7/19$, and the lattice scalar 24 derived independently from the Law of Admissibility ($R = 4$), the calculation produces exactly two wave peaks per tidal day with a fractional remainder that correctly predicts the observed daily tidal lag.

The same rational framework yields a discrete phase closure period. Solving the solar day alignment and lattice alignment conditions simultaneously produces $N = 107,160,000$ lunations (approximately 8.66 million years). At this horizon, the Earth-Moon system returns to exact phase closure with zero residual drift relative to the structural lattice. This period matches the observed 8.5 to 9.0 million year stratigraphic resonance in deep-time marine sediment records.

---

### The Model

The tidal structure emerges from three rational coordinates within the Earth-Moon framework:
* **$h = 181/3$** — Harmonic distance coordinate
* **$e = 7/19$** — Metonic residual
* **$L = 24$** — Lattice scalar

The spatial frequency remainder $1/9$ interacts with the lunar daily fraction $77/120$ and the lattice scalar to produce the nodal distribution. Adding the Metonic correction yields the total daily wave peaks:

$$\frac{1778}{855} \approx 2.07953$$

* **Integer part:** 2 tidal peaks
* **Fractional remainder:** approx. 57-minute daily lag

#### Phase Closure:
From the solar day alignment condition, $N$ must be a multiple of 94,000 lunations (approx. 257.34 solar years). The lattice alignment condition requires an additional factor of $4 \times 3 \times 5 \times 19 = 1,140$.

$$N = 94,000 \times 1,140 = 107,160,000 \text{ lunations}$$
$$107,160,000 \text{ lunations} \times \left(\frac{19 \text{ years}}{235 \text{ lunations}}\right) = 8,664,000 \text{ solar years}$$

---

### Key Results

| Parameter | Calculated | Observed | Precision |
| :--- | :--- | :--- | :--- |
| **Tidal peaks per day (integer)** | 2 | 2 | Exact |
| **Peak ratio (fractional)** | $1778/855 \approx 2.0795$ | $\approx 2.0701$ | 99.5% |
| **Daily tidal lag** | $\approx 57 \text{ min}$ | $\approx 50 \text{ min}$ | 87.7% |
| **Moon distance (km)** | 384,250 | 384,400 | 99.96% |
| **Phase closure period** | 8,664,000 years | 8.5 to 9.0 Myr | > 99% |

---

### Dependencies

| Work | DOI |
| :--- | :--- |
| **Deriving Euler's Number from Lunar Cycles** | [10.5281/zenodo.18363931](https://doi.org/10.5281/zenodo.18363931) |
| **The Law of Admissibility** | [10.5281/zenodo.18223592](https://doi.org/10.5281/zenodo.18223592) |
| **Calculating Planetary Distance** | [10.5281/zenodo.19720428](https://doi.org/10.5281/zenodo.19720428) |

Full framework available at [SemanticDrift.net](https://semanticdrift.net) and [SemanticShift.net](https://semanticshift.net).

---

### Repository Contents

| File | Description |
| :--- | :--- |
| **README.md** | This file |
| **Tidal Geometry.pdf** | Full paper |
| **coherence_envelope.py** | Python script verifying phase closure |
| **index.html** | Interactive visualization |

---

### Live Engine

[https://semanticdrift.github.io/Tidal-Geometry/](https://semanticdrift.github.io/Tidal-Geometry/)

---

### Citation

```
Johnson, C. (2026). Tidal Geometry and Phase Closure: An Annex to the Earth-Moon Framework.
Series: Harmonic Systems. SemanticDrift. DOI: 10.5281/zenodo.20338064 License: CC BY 4.0
```
---

## License

© 2026 Carolina Johnson (CJ)
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)
Attribution required. https://creativecommons.org/licenses/by/4.0/
