'''
Desafio
Agora, vamos Adicionar uma funcionalidade à classe UsuarioTelefone para que possa ser verificado o saldo disponível em seu plano. Para essa solução, você pode criar uma classe PlanoTelefone, o seu método de inicialização e encapsular os atributos, 'nome' e 'saldo' dentro da classe. Adicione também um método 'verificar_saldo' para verificar o saldo do plano e uma  'mensagem_personalizada' para gerar uma mensagem personalizada.

Condições da verificação do saldo:
- Caso o saldo seja menor do que 10, retorne: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
- Caso o saldo seja maior ou igual a 50, retorne: "Parabéns! Continue aproveitando seu plano sem preocupações."
- Caso contrário, retorne: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

Entrada
Como entrada, será solicitado o nome, plano (Essencial, Prata, Premium) e saldo atual do cliente.

Saída
Mensagem personalizada de acordo o saldo do cliente.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
João     
Essencial      
9

Seu saldo está baixo. Recarregue e use os serviços do seu plano.

Debora
Prata
11
 	Seu saldo está razoável. Aproveite o uso moderado do seu plano.
     
Catarina
Premium
50

Parabéns! Continue aproveitando seu plano sem preocupações.


'''
class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo
        
    def verificar_saldo(self):
        if self.__saldo < 10:
            return self.__saldo, "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.__saldo >= 50:
            return self.__saldo, "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return self.__saldo, "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
        
    def mensagem_personalizada(self):
        return self.verificar_saldo()[1]

class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano
    
    def verificar_saldo(self):
        return self.plano.verificar_saldo()

nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)
