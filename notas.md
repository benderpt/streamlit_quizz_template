# Quizz

## Elementos a controlar: 

1. Pergunta e respostas (Lista)
2. Seleção de resposta (Boolean)
3. Botão (Tuple=('Submeter', 'Avançar', 'Reiniciar'))  (Ação)
5. Resultado (score=0)
6. Barra de resultados (Função)


### Primeiro estado: 


1. Pergunta e respostas - index 0 de quiz_data.json
2. Seleção de resposta (highlight selection azul)
3. Botão ('Submeter') (Ação)
5. Resultado ()
6. Barra de resultados (total index quiz_data.json)


### segundo estado: 


1. Pergunta e respostas - index 0 de quiz_data.json
2. Seleção de resposta (if wrong highlight correct anwser green and highlight wrong anwser red, else highlight correct anwser green)
3. Botão ('Avançar') (Ação)
5. Resultado (if == correct score +=10)
6. Barra de resultados (0)

### terceiro estado: 


1. Pergunta e respostas - index 0 de quiz_data.json
2. Seleção de resposta (highlight correct anwser)
3. Botão ('Submeter') (Ação)
4. Resposta (if == correct 'resposta correta')
5. Resultado (if == correct score +=10)
6. Barra de resultados (total index quiz_data.json +1 )





