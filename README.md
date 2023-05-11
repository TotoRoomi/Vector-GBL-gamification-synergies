# VECTOR GAME
This is part of Toto Roomi and Harald Olins Bachelor thesis on gamification and it's borders. When is digital learning solely a game without the learning? When is it the perfect intersection between game and learning. Is all digital learning a game? Do all games have potential to be learning experiences?

In this project we demonstrate bad gamification wherein a learning experience is squandered by creating a game that neither follows game design rules nor behavioural science on learning. This is the fault of modern gamification, what __ calls "rhetorical gamification", that is, gamification for the hell of it.

The game is about simple Vector addition, subtraction and multiplication. You learn how to do these things visually.

![vecotor game diagram](Vektorspel_i_python.jpg)

## TO RUN 
write this in the terminal where gui.py is located. 
``` 
python3 gui.py
```

## To-Do
- new game after success 
- Score
- BUG: crash at loosing in score() had 27 points. 
Traceback (most recent call last):
  File "/Users/toto/Programming/VectorGame/main.py", line 138, in <module>
    main()
  File "/Users/toto/Programming/VectorGame/main.py", line 76, in main
    game.start()
  File "/Users/toto/Programming/VectorGame/Gameloop.py", line 341, in start
    self.score()
TypeError: 'int' object is not callable

## Spelfunktioner
scenario och utmaning 

### Regler för spelet
- En vektor på skärmen utgör målet. Ta dig från origo till spetsen av denna vektor givet andra vektorer i en "verktygslåda".
- Använd vektorerna i verktygslådan till att bygga målet 
- senaste vektorn börjar där förra slutade
- varje ny vektor kan läggas till i en lista som gör det enkelt att undo (radera senaste i listan)

### Extra gamification tillbehör som vi kan lägga till vid ett senare tillfälle
- poäng
- leaderboards
- störigt du-vann-ljud
- liv

- verktygslåda 
- undo/redo 


Första test exemplet;

Den vertikala vektorn är given och de "sneda" vektorerna finns i verktygslådan, skapa den horizontala vektorn med hjälp av vektorerna i verktygslådan.
|\
| \
|  \
|  /
| /
|/




conv_coordinates(0,1) = (123,500)