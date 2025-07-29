# Prompt Template
W zasadzie jest to template poprostu naszego prompta

# Chain
Mozna wiele komponentow w jedno laczyc sekwencyjne. Mozna ogolnie laczyc rzeczy w calosc:
- agenty
- inne lancuchy
- jakies inne operacje

# Temperatura
Jest tym co mowi jak bardzo model bedzie kretywny
- `0`: nie bedzie kreatywny
- `40`: bedzie bardziej kreatywny

# Operator `|`
Ogolnie to jest przeciazany operator ktory mowi o tym, ze to jest chain. Ten kod:
```python
chain = mess_prompt_template | llm
```

To skrot od:
```python
chain = RunnableSequence([mess_prompt_template, llm])
```

# Ollama
Lokalne modele llm na naszej maszynie :D Trzeba pobrac klienta `ollama`, tkory sobie zarzadza tymi modelami i jest serwerem lokalnym, ktory udostepnia api do tych modeli