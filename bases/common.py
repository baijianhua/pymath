from numpy import mat
from numpy.core._multiarray_umath import array


def get_column_from_matrix(m: mat, c: int) -> array:
    """
    取矩阵的某一列
    :param m:
    :param c:
    :return:
    """
    return array([m[0, c], m[1, c]])
