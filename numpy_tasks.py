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
    raise NotImplementedError  # TODO


def draw_rectangle(data: RectangleInput) -> np.ndarray:
    width, height = data.width, data.height
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    raise NotImplementedError  # TODO


def draw_ellipse(data: EllipseInput) -> np.ndarray:
    semi_axis_x, semi_axis_y = data.semi_axis_x, data.semi_axis_y
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    raise NotImplementedError  # TODO


def analyze_time_series(data: TimeSeriesInput) -> TimeSeriesStatistics:
    values, window = data.values, data.window
    raise NotImplementedError  # TODO


def one_hot(data: OneHotInput) -> np.ndarray:
    labels, class_count = data.labels, data.class_count
    raise NotImplementedError  # TODO
