#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import date

class Nota_fiscal(object):

    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes=''):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        self.__detalhes = detalhes
        self.__itens = itens

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes

    @property
    def itens(self):
        return self.__itens


# In[10]:


from datetime import date

class Criador_de_nota_fiscal(object):

    def __init__(self):

        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__detalhes = None
        self.__itens = None

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def com_detalhes(self, detalhes):
        self.__detalhes = detalhes
        return self

    def constroi(self):

        if self.__razao_social is None:
            raise Exception('Razao social deve ser preenchida')

        if self.__cnpj is None:
            raise Exception('CNPJ deve ser preenchido')

        if self.__itens is None:
            raise Exception('Os itens devem ser preenchidos')

        if self.__data_de_emissao is None:
            self.__data_de_emissao = date.today()

        if self.__detalhes is None:
            self.__detalhes = ''
        else:
            if len(self.__detalhes) < 5:
                raise Exception('Detalhes da nota fiscal nao pode ter mais que 5 chars')

        # retorna o tipo espec
        
        return Nota_fiscal(
            razao_social=self.__razao_social,
            cnpj=self.__cnpj,
            itens=self.__itens,
            data_de_emissao=self.__data_de_emissao,
            detalhes=self.__detalhes
        )


# In[12]:


from datetime import date

class Item(object):

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor


itens = [Item('ITEM A', 100), Item('ITEM B', 200)]


nf1 = (Criador_de_nota_fiscal()
                                  .com_razao_social('FHSA Limitada')
                                  .com_cnpj('01928391827321')
                                  .com_itens(itens)
                                  .com_detalhes("d")
                                  .constroi())


# In[5]:


nf1


# In[6]:


for x in nf1.itens:
    print(x.descricao, x.valor)


# In[7]:


type(nf1)


# In[9]:


nf1.cnpj


# In[1]:


# Isto para Python 2.7
import abc


class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def method_to_implement(self, input):
        return

class Foo(Shape):
    pass

foo = Foo()


# In[15]:


import abc


class Shape(metaclass=abc.ABCMeta):

    def __init__(self, )
    
    @abc.abstractmethod
    def area(self):
        return

    @abc.abstractmethod
    def lados(self):
        return self
    
    
class Triangulo(Shape):
    def __init__(self, l1, l2, l3):
        self.__lados = 
#     def area(self, l1, l2, l3):
#         return l1*l2*l3


foo = Foo()
foo.area(3,2,4)


# In[11]:


foo.method_to_implement(5)


# In[ ]:




