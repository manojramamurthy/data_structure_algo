import unittest


from roman import decimal_to_roman, roman_to_decimal


class TestDecimalToRoman(unittest.TestCase):
	def test_decimal_to_roman_11(self):
		self.assertEqual(decimal_to_roman(11), "XI", msg="decimal_to_roman(11) should return \"XI\"")
	
	def test_decimal_to_roman_60(self):
		self.assertEqual(decimal_to_roman(60), "LX", msg="decimal_to_roman(60) should return \"LX\"")
	
	def test_decimal_to_roman_78(self):
		self.assertEqual(decimal_to_roman(78), "LXXVIII", msg="decimal_to_roman(78) should return \"LXXVIII\"")
	
	def test_decimal_to_roman_4(self):
		self.assertEqual(decimal_to_roman(4), "IV", msg="decimal_to_roman(4) should return \"IV\"")
	
	def test_decimal_to_roman_99(self):
		self.assertEqual(decimal_to_roman(99), "XCIX", msg="decimal_to_roman(99) should return \"XCIX\"")




class TestRomanToDecimal(unittest.TestCase):
	def test_roman_to_decimal_11(self):
		self.assertEqual(roman_to_decimal("XXIV"), 24, msg="roman_to_decimal(\"XXIV\") should return 24")
	
	def test_roman_to_decimal_60(self):
		self.assertEqual(roman_to_decimal("CIX"), 109, msg="roman_to_decimal(\"CIX\") should return 109")
	
	def test_roman_to_decimal_78(self):
		self.assertEqual(roman_to_decimal("CDXCVII"), 497, msg="roman_to_decimal(\"CDXCVII\") should return 497")
	
	def test_roman_to_decimal_4(self):
		self.assertEqual(roman_to_decimal("XIX"), 19, msg="roman_to_decimal(\"XIX\") should return 19")
	
	def test_roman_to_decimal_99(self):
		self.assertEqual(roman_to_decimal("MCCCXCVII"), 1397, msg="roman_to_decimal(\"MCCCXCVII\") should return 1397")
