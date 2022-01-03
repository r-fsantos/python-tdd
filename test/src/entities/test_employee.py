"""
Employee Test Class
"""

import unittest

from src.entities.employee import Employee


class TestEmployeeComputePayment(unittest.TestCase):
	def setUp(self) -> None:
		self.NAME: str = "Renato F"
		self.EMPLOYEE_ID: int = 42
		self.EXPECTED_PAYOUT_NO_COMISSION_NO_HOURS_WORKED: float = 1000.0
		self.EXPECTED_PAYOUT_TEN_HOURS_WORKED: float = 2000.0
		self.EXPECTED_PAYOUT_WITH_COMISSION: float = 3000.0
		self.EXPECTED_PAYOUT_WITHOUT_COMISSION: float = 2000.0

		self.sut: Employee = Employee(name=self.NAME, employee_id=self.EMPLOYEE_ID)


	def test_it_should_return_a_float_type(self) -> None:
		self.assertIsInstance(float, self.sut.compute_payout())

	def test_if_computes_correctly_for_no_comission_no_hours_worked(self) -> None:
		self.assertAlmostEqual(
			first=self.EXPECTED_PAYOUT_NO_COMISSION_NO_HOURS_WORKED,
			second=self.sut.compute_payout()
		)
	
	def test_if_computes_correctly_for_ten_hours_worked(self) -> None:
		self.sut.hours_worked = 10

		self.assertEqual(
			first=self.EXPECTED_PAYOUT_TEN_HOURS_WORKED,
			second=self.sut.compute_payout()
		)

	def test_if_computes_correctly_with_comission(self) -> None:
		"""This test assumes: 10 contracts and hours worked"""
		self.sut.contracts_landed = 10
		self.sut.hours_worked = 10

		self.assertAlmostEqual(
			first=self.EXPECTED_PAYOUT_WITH_COMISSION,
			second=self.sut.compute_payout()
		)

	def test_if_computes_correctly_without_comission(self) -> None:
		"""This test assumes: 10 contracts and hours worked"""
		self.sut.contracts_landed = 10
		self.sut.hours_worked = 10
		self.sut.has_comission = False

		self.assertAlmostEqual(
			first=self.EXPECTED_PAYOUT_WITHOUT_COMISSION,
			second=self.sut.compute_payout()
		)


if __name__ == "__main__":
	unittest.main()
