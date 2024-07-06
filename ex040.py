print('\033[1;31m-=-\033[m'*30)
print('NOTAS DO ALUNO')
print('\033[1;31m-=-\033[m'*30)

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
media = (n1 + n2)/2

if media >= 7:
    print('\033[1;32mPARABÉNS VOCÊ TEVE UMA NOTA MÉDIA {:.1f} E FOI APROVADO!!\033[m'.format(media))
elif media >= 5 and media < 7:
    print('\033[1;33mVOCÊ TEVE UMA MÉDIA DE {:.1f} E FICOU DE RECUPERAÇÃO!!!\nESTUDE PARA A PROVA'.format(media))
else:
    print('\033[1;31mVOCÊ TEVE UMA MÉDIA DE {:.1f} E FOI REPROVADO!!!\nESTUDE MAIS DA PROXIMA VEZ\033[m'.format(media))

print('\033[1;31m-=-\033[m'*30)