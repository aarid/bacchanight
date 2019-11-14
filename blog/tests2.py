import unittest


# Create your tests here.
#Test sur la TABLE DU JEU


def say_hello():
    """
    Cette fonction dit bonjour !
    """
    print('Hello')

def is_even(nbr):
    """
    Cette fonction teste si un nombre est pair.
    """
    return nbr % 2 == 0
class TaleJeuTest(unittest.TestCase):

    # TODO Écrire les tests...
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(1))
        self.assertEqual(is_even(0), True)

    def test_speudo(self):
        """
        Affichage du speudo.
        """
        speudo = vvv 

        
    def test_passWord(self):
            """
            Affichage du mot de passe.
            """
if __name__ == '__main__':
    unittest.main()          