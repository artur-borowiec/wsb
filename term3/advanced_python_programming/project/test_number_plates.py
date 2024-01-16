from unittest import TestCase
import number_plates


class Test(TestCase):
    def test_is_polish_plate(self):
        assert number_plates.is_polish_plate('DPL 67JX'), "Should be correct"
        assert number_plates.is_polish_plate('DPL 67JXY'), "Should be correct"
        assert number_plates.is_polish_plate('DPL 67JXYF') is False, "Should be incorrect"
        assert number_plates.is_polish_plate('D9 67JX56') is False, "Should be incorrect"
        assert number_plates.is_polish_plate('D 67JX') is False, "Should be incorrect"
