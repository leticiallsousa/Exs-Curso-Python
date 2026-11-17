# \033[(style;text;back)m
# \033[0;00;00m
# style: 0 (None); 1 (Bold); 2 (Underline); 3 (Negative);
# text: 30 (Branco); 31 (Vermelho; 32 (Verde); 33 (Amarelo); 34 (Azul); 35 (Roxo); 36 (Ciano); 37 (Cinza);
# back: 40 (Branco); 41 (Vermelho; 42 (Verde); 43 (Amarelo); 44 (Azul); 45 (Roxo); 46 (Ciano); 47 (Cinza);
# Exemplo:
print('\033[1:30:41mOlá Mundo!\033[m')
