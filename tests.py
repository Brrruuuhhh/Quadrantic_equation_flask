import unittest
from equation import solve_quadratic
import requests


class TestQuadraticEquationSolver(unittest.TestCase):

    # Проверка доступности страницы /index
    def test_index_page_availability(self):
        response = requests.get('http://localhost:5000/')
        self.assertEqual(response.status_code, 200)

    # Проверка доступности страницы /solve
    def test_solve_page_availability(self):
        response = requests.post('http://localhost:5000/solve', data={'a': '1', 'b': '2', 'c': '3'})
        self.assertEqual(response.status_code, 200)

    # Проверка корней для уравнения с двумя действительными корнями
    def test_solve_quadratic_real_roots(self):
        self.assertEqual(solve_quadratic(1, -3, 2), (2.0, 1.0))

    # Проверка корней для уравнения с комплексными корнями
    def test_solve_quadratic_complex_roots(self):
        self.assertIsNone(solve_quadratic(1, 2, 5))

    # Проверка корней для уравнения с одним корнем
    def test_solve_quadratic_one_root(self):
        self.assertEqual(solve_quadratic(1, -2, 1), (1.0))

    # Проверка корней для уравнения без действительных корней
    def test_solve_quadratic_no_real_roots(self):
        self.assertIsNone(solve_quadratic(2, 4, 8))

    # Проверка корней для уравнения с нулевыми коэффициентами
    def test_solve_quadratic_zero_coefficients(self):
        self.assertIsNone(solve_quadratic(0, 0, 0))


if __name__ == '__main__':
    unittest.main()


