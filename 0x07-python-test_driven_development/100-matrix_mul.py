#!/usr/bin/python3
"""Defines a matrix multiplication function"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices

    Args:
        m_a (list of lists of ints/floats): The first matrix
        m_b (list of lists of ints/floats): The second matrix

    Returns:
        A new matrix representing the ruslt of the multiplication of m_a by m_b

    Raises:
        TypeError: If either m_a or m_b is not a list
        TypeError: If either m_a or m_b is not a list of lists of ints/floats
        TypeError: If either m_a or m_b has different-sized rows
        ValueError: If either m_a or m_b is empty
        ValueError: If m_a and m_b cannot be multiplied
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(isinstance(ele, (int, float))
               for ele in [n for row in m_a for n in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(ele, (int, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_b_inverted = []
    for i in range(len(m_b[0])):
        m_b_row = []
        for j in range(len(m_b)):
            m_b_row.append(m_b[j][i])
        m_b_inverted.append(m_b_row)

    mul_matrix = []
    for row in m_a:
        mul_row = []
        for col in m_b_inverted:
            mul = 0
            for i in range(len(m_b_inverted[0])):
                mul += row[i] * col[i]
            mul_row.append(mul)
        mul_matrix.append(mul_row)

    return mul_matrix
