"""Desenvolva um programa que calcula a nota média de um aluno e informe se ele passou de ano, ficou de recuperação ou
reprovou"""

print('\033[1;31m-=-\033[m'*30)
print('NOTAS DO ALUNO')
print('\033[1;31m-=-\033[m'*30)

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
media = (n1 + n2)/2

if media >= 7:
    print('\033[1;32mPARABÉNS VOCÊ TEVE UMA NOTA MÉDIA {:.2f} E FOI APROVADO!!\033[m'.format(media))
elif 5 <= media < 7:
    print('\033[1;33mVOCÊ TEVE UMA MÉDIA DE {:.2f} E FICOU DE RECUPERAÇÃO!!!\nESTUDE PARA A PROVA'.format(media))
else:
    print('\033[1;31mVOCÊ TEVE UMA MÉDIA DE {:.2f} E FOI REPROVADO!!!\nESTUDE MAIS DA PROXIMA VEZ\033[m'.format(media))
print('\033[1;31m-=-\033[m'*30)
