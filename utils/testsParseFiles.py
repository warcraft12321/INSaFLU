'''
Created on Oct 28, 2017

@author: mmp
'''
from django.test import TestCase
from constants.constantsTestsCase import ConstantsTestsCase
from .parseOutFiles import ParseOutFiles
from django.conf import settings 
import os

class Test(TestCase):

	### static
	parseOutFiles = ParseOutFiles()
	
	def setUp(self):
		self.baseDirectory = os.path.join(getattr(settings, "STATIC_ROOT", None), ConstantsTestsCase.MANAGING_TESTS)
		pass


	def tearDown(self):
		pass


	def test_parse_abricate_file(self):
		"""
		Test samtools fai index
		"""
		## create an index file from 
		
		txt_file = os.path.join(self.baseDirectory, 'abricate', ConstantsTestsCase.MANAGING_TEST_ABRICATE)
		self.assertTrue(os.path.exists(txt_file))
		vect_data = self.parseOutFiles.parse_abricate_file(txt_file)
		
		self.assertEqual('A', vect_data[0][ParseOutFiles.GENE])
		self.assertEqual(100.00, vect_data[0][ParseOutFiles.COVERAGE])
		self.assertEqual(99.69, vect_data[0][ParseOutFiles.IDENTITY])
		self.assertEqual('influenza_type', vect_data[0][ParseOutFiles.TYPE])
		self.assertEqual('XXXX', vect_data[0][ParseOutFiles.ACCESSION])
		
		self.assertEqual('Victoria', vect_data[3][ParseOutFiles.GENE])
		self.assertEqual(80.00, vect_data[3][ParseOutFiles.COVERAGE])
		self.assertEqual(78.65, vect_data[3][ParseOutFiles.IDENTITY])
		self.assertEqual('influenza_lineage', vect_data[3][ParseOutFiles.TYPE])
		self.assertEqual('M58428', vect_data[3][ParseOutFiles.ACCESSION])
