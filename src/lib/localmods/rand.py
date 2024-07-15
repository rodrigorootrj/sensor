import random
class Randomic:
    def __init__(self):
        self.main_12 = Randomic.main_12()
        self.main_1845 = Randomic.main_1845()
        return None

    def main_02():
        '''
        ...
        '''
        value = random.randrange(0, 3)                
        return value    
    
    def main_12():
        '''
        a=1, b=3-1, randomico entre 1 e 2.
        '''
        value = random.randrange(1, 3)                
        return value
    def main_110():
        '''
        ...
        '''
        value = random.randrange(1, 11)                
        return value

    def main_1845():
        '''
        ...
        '''
        value = random.randrange(18, 46)                
        return value    
    def temperatura(self,):
        '''
        handle, para criar valor especifico com.
        '''
        #inteiro = random.randrange(1, 3)
        inteiro = self.main_1845
        decimal = random.randrange(0,100)
        value = '{}.{}'.format(inteiro,decimal)
        marshmellow_127 = float(value)
        marshmellow_127_2 = "{:.2f}".format(marshmellow_127)
        return marshmellow_127_2
    def humidade(self,):
        '''
        handle, para criar valor especifico com.
        '''
        #inteiro = random.randrange(1, 3)
        inteiro = self.main_1845
        decimal = random.randrange(0,100)
        value = '{}.{}'.format(inteiro,decimal)
        marshmellow_127 = float(value)
        marshmellow_127_2 = "{:.2f}".format(marshmellow_127)
        return marshmellow_127_2