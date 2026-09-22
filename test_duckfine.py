import unittest

from duckfine import DuckFine


class TestDuckFine(unittest.TestCase):
    def setUp(self):
        self.duck_fine = DuckFine("member-1")

    def test_stores_member_id(self):
        self.assertEqual(self.duck_fine.member_id, "member-1")

    def test_starts_with_no_amount_owed(self):
        self.assertEqual(self.duck_fine.total_owed, 0.0)

    def test_forgives_first_two_days(self):
        self.assertEqual(self.duck_fine.charge(2), 0.0)

    def test_charges_daily_fee_after_grace_period(self):
        self.assertEqual(self.duck_fine.charge(3), 0.5)

    def test_deluxe_charge_is_doubled(self):
        self.assertEqual(self.duck_fine.charge(3, deluxe=True), 1.0)

    def test_single_charge_is_capped(self):
        self.assertEqual(self.duck_fine.charge(20), 5.0)

    def test_accumulates_multiple_charges(self):
        self.duck_fine.charge(3)
        self.duck_fine.charge(4)

        self.assertEqual(self.duck_fine.total_owed, 1.5)

    def test_rejects_negative_days_late(self):
        with self.assertRaises(ValueError):
            self.duck_fine.charge(-1)


if __name__ == "__main__":
    unittest.main()