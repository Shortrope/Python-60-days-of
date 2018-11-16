#!/usr/bin/python3

import os
import unittest


def analyze_text(filename):
    lines = 0
    chars =0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
    return (lines, chars)



class TextAnalysisTests(unittest.TestCase):
    """Tests for the ``analyze_text()`` function."""

    def setUp(self):
        """Fixture: creates a file for the text methods to use."""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war.\n'
                    'testing whether that nation,\n'
                    'or any namtion so conceived and so dedicated,\n'
                    'can long endure.')

    def tearDown(self):
        """Fixture: deletes the files used by the test methods."""
        try:
            os.remove(self.filename)
        except:
            pass


    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check the line count is correct"""
        self.assertEqual(analyze_text(self.filename)[0], 4)

    def test_char_count(self):
        """Check the character count is correct"""
        self.assertEqual(analyze_text(self.filename)[1], 132)

    def test_no_such_file(self):
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        """Check function does not delete the input file"""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

if __name__ == '__main__':
    unittest.main()