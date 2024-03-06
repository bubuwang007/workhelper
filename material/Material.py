from abc import ABCMeta, abstractmethod

class Material(metaclass=ABCMeta):
    
    @property
    @abstractmethod
    def type(self): pass

    @property
    @abstractmethod
    def density(self): pass

    @property
    @abstractmethod
    def alpha(self): pass

    @property
    @abstractmethod
    def elastic_modulus(self): pass

    @property
    @abstractmethod
    def poissons_ratio(self): pass

    @property
    @abstractmethod
    def ultimate_tensile_strength(self): pass

    @property
    @abstractmethod
    def yield_strength(self): pass
    