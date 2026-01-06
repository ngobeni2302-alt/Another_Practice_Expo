import unittest
import assessment


class TestAssessment(unittest.TestCase):

    # -------- extract_middle_three --------
    def test_middle_three(self):
        self.assertEqual(assessment.extract_middle_three("abcdefg"), "cde")
        self.assertEqual(assessment.extract_middle_three("Python"), "tho")
        self.assertEqual(assessment.extract_middle_three("hi"), "hi")

    # -------- swap_first_last_character --------
    def test_swap(self):
        self.assertEqual(assessment.swap_first_last_character("hello"), "oellh")
        self.assertEqual(assessment.swap_first_last_character("a"), "a")
        self.assertEqual(assessment.swap_first_last_character("ab"), "ba")

    # -------- describe_temperature --------
    def test_temperature(self):
        self.assertEqual(assessment.describe_temperature(-5), "Freezing")
        self.assertEqual(assessment.describe_temperature(10), "Cold")
        self.assertEqual(assessment.describe_temperature(20), "Warm")
        self.assertEqual(assessment.describe_temperature(30), "Hot")

    # -------- total_cost --------
    def test_total_cost(self):
        self.assertEqual(assessment.total_cost(9.99, 3), 29.97)
        self.assertEqual(assessment.total_cost(4.5, 2), 9.00)
        self.assertEqual(assessment.total_cost(0, 100), 0.00)

    # -------- remove_vowels --------
    def test_remove_vowels(self):
        self.assertEqual(assessment.remove_vowels("Hello World"), "Hll Wrld")
        self.assertEqual(assessment.remove_vowels("Python"), "Pythn")
        self.assertEqual(assessment.remove_vowels("AEIOUaeiou"), "")

    # -------- validate_id --------
    def test_validate_id(self):
        self.assertTrue(assessment.validate_id("9901014800082"))
        self.assertFalse(assessment.validate_id("abcd"))
        self.assertFalse(assessment.validate_id("123456789012"))

    # -------- bubble_sort --------
    def test_bubble_sort(self):
        self.assertEqual(assessment.bubble_sort([5,2,9,1,5]), [1,2,5,5,9])
        self.assertEqual(assessment.bubble_sort([]), [])
        self.assertEqual(assessment.bubble_sort([1]), [1])
        self.assertEqual(assessment.bubble_sort([3,3,2,1]), [1,2,3,3])

    # -------- insertion_sort --------
    def test_insertion_sort(self):
        self.assertEqual(assessment.insertion_sort([12,11,13,5,6]), [5,6,11,12,13])
        self.assertEqual(assessment.insertion_sort([]), [])
        self.assertEqual(assessment.insertion_sort([1]), [1])
        self.assertEqual(assessment.insertion_sort([2,1,2,3]), [1,2,2,3])


if __name__ == "__main__":
    unittest.main()
