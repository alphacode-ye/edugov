# Copyright (c) 2024, AlphaCode and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record depdendencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class TestUniversity(UnitTestCase):
	"""
	Unit tests for University.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestUniversity(IntegrationTestCase):
	"""
	Integration tests for University.
	Use this class for testing interactions between multiple components.
	"""

	pass
