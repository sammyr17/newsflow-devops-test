import unittest

from article_parser import parse_article


class TestArticleParser(unittest.TestCase):
    def test_parse_article_splits_title_and_body(self):
        raw = """Breaking News
This is the body line 1.
Line 2."""
        result = parse_article(raw)

        self.assertEqual(result["title"], "Breaking News")
        self.assertIn("This is the body line 1.", result["body"])
        self.assertIn("Line 2.", result["body"])

    def test_empty_article_raises_value_error(self):
        with self.assertRaises(ValueError):
            parse_article(" \n   ")


if __name__ == "__main__":
    unittest.main()
