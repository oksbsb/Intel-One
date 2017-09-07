from unittest import TestCase
import search.companies as companies
import sys
from contextlib import contextmanager
from io import StringIO


class TestCompanies(TestCase):
    # tests if search is returning back the correct link for two terms.
    def test_edgarSearch_singleTerm_shortFlag(self):
        query = "google -e"
        with TestCompanies.captured_output(self) as (out, err):
            companies.Companies.edgarSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.sec.gov/cgi-bin/browse-edgar?company=google&owner=exclude&action=getcompany')

    # tests if search is returning back the correct link for two terms.
    def test_edgarSearch_doubleTerm_shortFlag(self):
        query = "goldman sachs -e"
        with TestCompanies.captured_output(self) as (out, err):
            companies.Companies.edgarSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.sec.gov/cgi-bin/browse-edgar?company=goldman+sachs&owner=exclude&action=getcompany')

    # tests if search is returning back the correct link for two terms.
    def test_edgarSearch_singleTerm_longFlag(self):
        query = "google --edgar"
        with TestCompanies.captured_output(self) as (out, err):
            companies.Companies.edgarSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.sec.gov/cgi-bin/browse-edgar?company=google&owner=exclude&action=getcompany')

    # tests if search is returning back the correct link for two terms.
    def test_edgarSearch_doubleTerm_longFlag(self):
        query = "goldman sachs --edgar"
        with TestCompanies.captured_output(self) as (out, err):
            companies.Companies.edgarSearch(query)
        # This can go inside or outside the `with` block
        link = out.getvalue().strip()
        self.assertEqual(link, 'https://www.sec.gov/cgi-bin/browse-edgar?company=goldman+sachs&owner=exclude&action=getcompany')

    # tests output in screen.
    @contextmanager
    def captured_output(self):
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err