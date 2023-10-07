

import unittest
import os
from financial_report_generator import generate_html_report

class TestFinancialReportGenerator(unittest.TestCase):

    def test_generate_html_report(self):
        html_report_filename = 'financial-report.html'

        generate_html_report([], html_report_filename)
        self.assertTrue(os.path.exists(html_report_filename))

if __name__ == '__main__':
    unittest.main()