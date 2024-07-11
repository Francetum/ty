from add import isaletter
from add import addition
import unittest
from unittest.mock import patch
from io import StringIO

class TestIsAletter(unittest.TestCase):
    """_summary_
        @patch('builtins.input', side_effect=['a']) : Pour simuler les entrées utilisateur dans les tests.
        Cela permet de tester des fonctions qui nécessitent une saisie utilisateur sans avoir besoin d'une 
        interaction réelle avec l'utilisateur pendant les tests.

        @patch('sys.stdout', new_callable=StringIO) : Pour capturer et vérifier les sorties imprimées par 
        la fonction pendant les tests. Cela permet de tester si les messages imprimés (par exemple, les 
        messages de validation ou d'erreur) sont corrects.
    
    """
    @patch('builtins.input', side_effect=['a'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_isaletter_valid(self, mock_stdout, mock_input):
        isaletter('')
        self.assertIn("La lettre a est valide.", mock_stdout.getvalue().strip())
        
    def test_addition(self):
        self.assertEqual(addition(4, 3), 7)

  

if __name__ == '__main__':
    unittest.main()