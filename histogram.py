import matplotlib.pyplot as plt
import numpy as np

def plot_histograms(matrix: np.ndarray, bins: int = 20) -> None:
    rows, columns = matrix.shape

    fig, axes = plt.subplots(rows, 1, figsize=(8, 2 * rows), squeeze=False)
    for i in range(rows):
        axes[i, 0].hist(matrix[i], bins=bins, color="steelblue", edgecolor="black")
        axes[i, 0].set_title(f"Строка {i}")
        axes[i, 0].set_ylabel("Частота")
    plt.tight_layout()
    plt.show()

    fig, axes = plt.subplots(columns, 1, figsize=(8, 2 * columns), squeeze=False)
    for j in range(columns):
        axes[j, 0].hist(matrix[:, j], bins=bins, color="salmon", edgecolor="black")
        axes[j, 0].set_title(f"Столбец {j}")
        axes[j, 0].set_ylabel("Частота")
    plt.tight_layout()
    plt.show()