# CountdownNumbers
Lost de numbers game van het programma countdown (hopelijk ooit) op


## Mogelijkheden
- kleinste gemeenschappelijke deler?
- gwn coole deling?
- https://www.dcode.fr/countdown-numbers-game#q1

## Oplossing die ik wil proberen
The general principle is to start with the list of N numbers, 
pick 2 and make all operations with these two numbers, 
if the result is the expected total, note the calculation as possible solution, 
else, store the result in the list and try again with the N-1 new numbers in the list, 
and so on.

Example: Numbers 2,6,10, then for each couple among (2,6),(2,10),(6,10), 
let's take (2,6), make the calculations 2+6=8, 2*6=12, 6-2=4 and 6/2=3 to get 4 new numbers (8,12,4,3) 
that will make 4 new couples with the remaining 10: (8,10), (12,10), (4,10) and (3,10). 
Start over with new couples recursively. 


### Stap 1
Zorg dat het programma het probleem kan oplossen

### Stap 2
Zorg dat het de stappen die werken op slaat

### Stap 3
Zorg dat de stappen die werkte getoont worden