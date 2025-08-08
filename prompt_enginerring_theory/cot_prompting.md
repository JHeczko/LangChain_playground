# Chain of Thoughts
## Zero shot
Czyli nie podajemy przykladu rozumowania, dajemy tylko prompta w przykladzie
```
Masz liczby 1+3+5+2, jaki jest wynik, przeanalizuj krok po kroku
```

## Few shot
Mozna podac przyklady rozumowania, a potem kolejny przykladowy problem jak ma byc rozwiazany:
```
Masz tutaj przyklady rozumowania do przykladowego problemu:
Pytanie: Jacek ma 5 jablek, zjadl 2, splesnialo 1, ile ma jablek
Rozumowanie: Skoro zjadl 2 jablka, ma juz fizycznie 3, jak splesnialo jedno to dalej ma dfizycznie 3 jablka, ale jedno splesniale
Odpowiedz: Jacek ma 3 jablka

Teraz masz pytanie i sproboj sam przeanalizowac i dac odpowiedz:
Pytanie: Skoro Ania ma 3 jablka i jedno zgubila to ile ma jablek
Odpowiedz:...
```
