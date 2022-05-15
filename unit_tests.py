import unittest
from website_fetcher import WebsiteFetcher
# from document_parser import parse_text
from document_parser import clean_text
from document_parser import DocumentParser


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

    # this will be a variety of tests on the clean_text() function
    def test_clean_text_empty(self):
        my_text = ""
        result = clean_text(my_text)
        self.assertEqual(result, [], "If given an empty string, clean text should return an empty list.")

    def test_clean_text_no_invalid(self):
        my_text = "this is a test to see what this returns"
        result = clean_text(my_text)
        expected_result = ['this', 'is', 'a', 'test', 'to', 'see', 'what', 'this', 'returns']
        self.assertEqual(result, expected_result, "If there are no lowercase characters, we expect this to return a "
                                                  "list of the words")

    def test_clean_text_w_uppercase(self):
        my_text = "THIS IS A TEST TO SEE WHAT THIS RETURNS"
        result = clean_text(my_text)
        expected_result = ['this', 'is', 'a', 'test', 'to', 'see', 'what', 'this', 'returns']
        self.assertEqual(result, expected_result, "we expect this to return a list of the words, all lowercase")

    def test_clean_text_w_punctuation(self):
        my_text = "this is.a.test!"
        result = clean_text(my_text)
        expected_result = ['this', 'is', 'a', 'test']
        self.assertEqual(result, expected_result, "we expect this to return the response removing punctuation")

    def test_clean_text_w_punctuation_2(self):
        my_text = "this is.a..().?test!"
        result = clean_text(my_text)
        expected_result = ['this', 'is', 'a', 'test']
        self.assertEqual(result, expected_result, "we expect this to return the response removing punctuation")

    def test_clean_text_w_variety(self):
        my_text = "this!is()a test? Or Not testing maybe?"
        result = clean_text(my_text)
        expected_result = ['this', 'is', 'a', 'test', 'or', 'not', 'testing', 'maybe']
        self.assertEqual(result, expected_result, "we expect this to strip out a variety of punctuation and "
                                                  "uppercase, etc")

    # this will run a variety of tests on the parse_string() function
    def test_parse_empty_string(self):
        my_text = ""
        parser = DocumentParser()
        result = parser.parse_text(my_text)
        self.assertEqual(result, {}, "if it is an empty string, we expect an empty dictionary as the return")

    def test_parse_string(self):
        my_text = "THIS IS A TEST TO SEE WHAT RETURNS"
        parser = DocumentParser()
        result = parser.parse_text(my_text)
        expected_result = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'to': 1, 'see': 1, 'what': 1, 'this': 1, 'returns': 1}
        self.assertEqual(result, expected_result)

    def test_parse_string_duplicates(self):
        my_text = 'test test test test test this'
        parser = DocumentParser()
        result = parser.parse_text(my_text)
        expected_result = {'test': 5, 'this': 1}
        self.assertEqual(result, expected_result, 'we expect this to return the count of test')

    def test_parse_string_duplicates_punctuation(self):
        my_text = 'test!test?test    test   this   wow    works?   (testing)  '
        parser = DocumentParser()
        result = parser.parse_text(my_text)
        expected_result = {'test': 4, 'this': 1, 'wow': 1, 'testing': 1, 'works': 1}
        self.assertEqual(result, expected_result)


    def test_parse_caps(self):
        my_text = 'test Test test Test TEST test!'
        parser = DocumentParser()
        result = parser.parse_text(my_text)
        expected_result = {'test': 6}
        self.assertEqual(result, expected_result)

    def test_text_parse_plural(self):
        my_text = 'My dog went to the park.  He saw many dogs there!  He was happy to see the dogs.'
        parser = DocumentParser()
        result = parser.parse_text(my_text)
        expected_result = {'my': 1, 'dog': 1, 'went': 1, 'to': 2, 'the': 2, 'park': 1, 'he': 2, 'saw': 1, 'many': 1,
                           'dogs': 2, 'there': 1, 'was': 1, 'happy': 1, 'see': 1}
        self.assertEqual(result, expected_result, 'check for tense')


if __name__ == '__main__':
    unittest.main()
