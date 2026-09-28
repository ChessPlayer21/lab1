"""Заготовки задач на NumPy."""

import numpy as np
from grader_contracts.numpy_tasks import (
    BinarizeInput, ChessInput, EllipseInput, MatrixInput, MatrixStatistics,
    MatrixVectorBatchInput, OneHotInput, RandomMatrixInput, RectangleInput,
    TimeSeriesInput, TimeSeriesStatistics,
)


def sum_prod(data: MatrixVectorBatchInput) -> np.ndarray:
    matrices, vectors = data.matrices, data.vectors
    n = matrices.shape[-1]  
    answer = np.zeros((n, 1))
    for i in range(len(matrices)):
        answer += matrices[i] @ vectors[i]
    return answer


def binarize(data: BinarizeInput) -> np.ndarray:
    matrix, threshold = data.matrix, data.threshold
    new_matrix = matrix.copy()
    for i in range(len(matrix)):
        for k in range(len(matrix[0])):
            if matrix[i, k] > threshold:
                new_matrix[i, k] = 1
            else:
                new_matrix[i, k] = 0
    return new_matrix


def unique_rows(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    array_unique_simbols = []
    for i in range(len(matrix)):
        count_simbols = {}
        unique_simbols = []
        for k in range(len(matrix[0])):
            if matrix[i, k] in count_simbols:
                count_simbols[matrix[i, k]] += 1
            else:
                count_simbols[matrix[i, k]] = 1
        for key, value in count_simbols.items():
            if value == 1:
                unique_simbols.append(key)   
        array_unique_simbols.append(unique_simbols)
    return array_unique_simbols


def unique_columns(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    array_unique_simbols = []
    for i in range(len(matrix[0])):       
        count_simbols = {}
        unique_simbols = []
        for k in range(len(matrix)):
            if matrix[k, i] in count_simbols:   
                count_simbols[matrix[k, i]] += 1 
            else:
                count_simbols[matrix[k, i]] = 1  
        for key, value in count_simbols.items():
            if value == 1:
                unique_simbols.append(key)
        array_unique_simbols.append(unique_simbols)
    return array_unique_simbols


def matrix_statistics(data: RandomMatrixInput) -> MatrixStatistics:
    rows, columns, mean, std, seed = data.rows, data.columns, data.mean, data.std, data.seed
    raise NotImplementedError  # TODO


def chess(data: ChessInput) -> np.ndarray:
    rows, columns, first, second = data.rows, data.columns, data.first, data.second
    matrix = np.zeros((rows, columns))
    for i in range(rows):
        for k in range(columns):
            if (i % 2 == 0 and k % 2 == 0) or (i % 2 != 0 and k % 2 != 0):
                matrix[i, k] = first
            else:
                matrix[i, k] = second
    return matrix   


def draw_rectangle(data: RectangleInput) -> np.ndarray:
    width, height = data.width, data.height
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    rgb_image = np.zeros((image_height, image_width, 3), dtype=np.uint8)
    rgb_image[:] = background_color
    rgb_image[(image_height - height) // 2:(image_height - height) // 2 + height, (image_width - width) // 2:(image_width - width) // 2 + width] = shape_color
    return rgb_image


def draw_ellipse(data: EllipseInput) -> np.ndarray:
    semi_axis_x, semi_axis_y = data.semi_axis_x, data.semi_axis_y
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    center_x = image_width / 2
    center_y = image_height / 2 
    rgb_image = np.zeros((image_height, image_width, 3), dtype=np.uint8)
    rgb_image[:] = background_color
    Y, X = np.indices((image_height, image_width))
    figure = (X - center_x)**2 / semi_axis_x**2 + (Y - center_y)**2 / semi_axis_y**2
    mask = figure <= 1
    rgb_image[mask] = shape_color
    return rgb_image



def analyze_time_series(data: TimeSeriesInput) -> TimeSeriesStatistics:
    values, window = data.values, data.window
    values = np.asarray(values, dtype=float)
    average = values.mean()
    dispersion = values.var()
    deviation = values.std()
    local_max = []
    local_min = []
    for i in range(0, len(values) - 2):
        if values[i] < values[i + 1] and values[i + 1] > values[i + 2]:
            local_max.append(i + 1)
        if values[i] > values[i + 1] and values[i + 1] < values[i + 2]:
            local_min.append(i + 1)
    kernel = np.ones(window) / window
    moving = np.convolve(values, kernel, mode="valid")
    return TimeSeriesStatistics(
    average=average,
    dispersion=dispersion,
    deviation=deviation,
    local_max=local_max,
    local_min=local_min,
    moving_average=moving,
)


def one_hot(data: OneHotInput) -> np.ndarray:
    labels, class_count = data.labels, data.class_count
    if class_count is None:
        class_count = labels.max() + 1
    matrix = np.zeros((len(labels), class_count))
    for i in range(len(labels)):
        matrix[i, labels[i]] = 1
    return matrix