import matplotlib.pyplot as plt
import numpy as np

# ===========================
# DATA
# ===========================
nilai_b = np.array([
    2.5, 2.021276596, 1.860815715, 1.843909274, 1.843734297, 1.843734278
])

iterasi = np.arange(1, len(nilai_b) + 1)

# Error - nilai terakhir tidak boleh 0 pada grafik log → diganti 1e-8
nilai_e = np.array([
    5.625, 1.150756578, 0.100502751, 0.001019134, 0.000000111, 1e-8
])

# ===========================
# PLOT
# ===========================
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot error (log scale)
ax1.plot(iterasi, nilai_e, 'b-o', label='|f(b)| atau Error')
ax1.set_xlabel('Iterasi')
ax1.set_ylabel('|f(b)| atau Error (skala log)', color='b')
ax1.set_yscale('log')
ax1.tick_params(axis='y', labelcolor='b')

# Garis batas toleransi
plt.hlines(1e-8, xmin=1, xmax=len(iterasi),
           colors='purple', linestyles='dashed',
           label='Toleransi: 10⁻⁸')

# Plot nilai b
ax2 = ax1.twinx()
ax2.plot(iterasi, nilai_b, 'g-o', label='Nilai b')
ax2.set_ylabel('Nilai b', color='g')
ax2.tick_params(axis='y', labelcolor='g')

# ===========================
# CARI ITERASI YANG MENCAPAI TOLERANSI
# ===========================
toleransi_tercapai_idx = np.where(nilai_e <= 1e-8)[0]

if len(toleransi_tercapai_idx) > 0:
    idx = toleransi_tercapai_idx[0]
    iterasi_tercapai = idx + 1
    nilai_e_tercapai = nilai_e[idx]

    # Titik merah toleransi tercapai
    ax1.plot(iterasi_tercapai, nilai_e_tercapai, 'ro', markersize=10,
             label=f'Toleransi tercapai: iterasi {iterasi_tercapai}')

    # Anotasi teks
    ax1.annotate(f'Toleransi tercapai\nIterasi {iterasi_tercapai}',
                 xy=(iterasi_tercapai, nilai_e_tercapai),
                 xytext=(iterasi_tercapai + 0.6, nilai_e_tercapai * 10),
                 arrowprops=dict(arrowstyle='->', color='red'),
                 fontsize=10, color='red')

# ===========================
# TAMBAHAN VISUAL
# ===========================
plt.title('GRAFIK METODE NEWTON RAPHSON:\n f(x) = x³ - 2x² + 3x - 5   |   Toleransi: 10⁻⁸')
fig.tight_layout()

# Gabungkan legenda
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
plt.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

plt.grid(True, which="both", ls="--")

plt.show()