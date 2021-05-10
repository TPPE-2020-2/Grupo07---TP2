import unittest
from fragments import Fragments
from fragmentsExtrairMetodo import FragmentsRefactor
from fragmentsPolimorfismo import FragmentsPolimorfismo
from fragmentsPolimorfismo import FragmentsArray

class FragmentTest(unittest.TestCase):
  # fragments class test
  def test_shouldCreateFragmentsArray(self):
    fragment = Fragments('Invalid Fragment', False, 'else')
    self.assertEqual(len(fragment.arrayFragments), 0, 'Array fragments length should be equal 0')
    fragment = Fragments('Valid Fragment', True, 'else')
    self.assertEqual(len(fragment.arrayFragments), 1, 'Array fragments length should be equal 1')
  # fragments refactored using extract method class test
  def test_shouldCreateFragmentsArrayRefactor(self):
    fragment = FragmentsRefactor('Invalid Fragment', False, 'else')
    self.assertEqual(len(fragment.arrayFragments), 0, 'Array fragments length should be equal 0')
    fragment = FragmentsRefactor('Valid Fragment', True, 'else')
    self.assertEqual(len(fragment.arrayFragments), 1, 'Array fragments length should be equal 1')
  def test_shouldCreateFragmentsArrayPolimorfism(self):
    fragment = FragmentsPolimorfismo('Invalid Fragment', False, 'else')
    fragmentArray = FragmentsArray()
    fragmentArray.addFragment(fragment)
    self.assertEqual(len(fragmentArray.arrayFragments), 0, 'Array fragments length should be equal 0')
    fragment = FragmentsPolimorfismo('Valid Fragment', True, 'else')
    fragmentArray = FragmentsArray()
    fragmentArray.addFragment(fragment)
    self.assertEqual(len(fragmentArray.arrayFragments), 1, 'Array fragments length should be equal 1')

if __name__ == '__main__':
  unittest.main()