print (1+1)
print ('a'+'b')
'''''print ('1'+1) '''''#--> TypeError: can only concatenate str (not "int") to str
 # no javascript é tipagem fraca como no caso acima ele converteria um tipo em outro
#no python, ele dá erro.
print (int('1'), type('1'))
print (int('1'), type(int('1')))
print (int('1') + 1) #conversao de tipos, tipos imutáveis e primitivos: str, int, float, bool
print (float('1') + 1) # = 2.0
print (type(float('1') + 1)) #ele executa dos primeiroas parenteses de dentro para fora, por isso que 
#só aparece <class 'float'>
print(bool('1')) #vazia = false , com algo = true

print('11' + 'b') 
print(str(11) + 'b') #coersao