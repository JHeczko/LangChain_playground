# Reasoning and Acting
1. Reasoning: model analizuje co trzeba zrobic, jakie akcje podjac
2. Acting: podejmuje akcje, na podstawie narzedzi ktorych moze uzywac.

Przyklad przebiegu ReAct prompt moze byc nastepuajcy:
```
Ile to jest pierwiastek kwadratowy z (144 + 81)?

Myśl i działaj krok po kroku.
```

A odpowiedz LLM jest nastepujaca:
```
Thought: Najpierw muszę obliczyć sumę 144 i 81.  
Action: Oblicz 144 + 81  
Observation: Wynik to 225  
Thought: Teraz muszę znaleźć pierwiastek kwadratowy z 225  
Action: Oblicz pierwiastek kwadratowy z 225  
Observation: Wynik to 15  
Answer: 15
```

Po kilku iteracjach mozna dojsc do odpowiedzi.

Ale to nie jest amgai ze model sam sobie zebke skrobie. Model sam nie wykonuje Search(...) czy Calculator(...). To zewnętrzny kod/program, który:
- „czyta” co model napisał jako `Action:`
- wykonuje dane działanie (np. wyszukiwanie, kalkulację, API call)
- wstawia wynik jako `Observation`: i ponownie przekazuje wszystko modelowi do kontynuacji.

Prawda jest taka, ze przed calym naszym promptem trzeba jeszcze model przygotowac:
```
Jesteś inteligentnym agentem, który potrafi myśleć i wykonywać działania przy pomocy dostępnych narzędzi.

Dostępne narzędzia:
- Search(query): wyszukuje informacje w Internecie.
- Calculator(expression): oblicza wyrażenia matematyczne.

Format odpowiedzi:
Thought: [opis toku rozumowania]
Action: [nazwa narzędzia i parametr]
Observation: [wynik działania narzędzia]
... (powtórz w razie potrzeby)
Answer: [ostateczna odpowiedź]
```