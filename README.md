# 1 Dimensional Cellular Automata
For more details about cellular automata: [Wolfram Alpha](https://mathworld.wolfram.com/CellularAutomaton.html), [Wikipedia](https://en.wikipedia.org/wiki/Cellular_automaton), [Explanation with code (natureofcode)](https://natureofcode.com/book/chapter-7-cellular-automata/).
\
This is a simple 1Dimensional cellular automata visualized using matplotlib.pyplot.

## How to use
  -Install matplotlib (To install matplotlib use `pip install matplotlib` on your command line)
  -Run this file and enter the rule [see what is rule](https://plato.stanford.edu/entries/cellular-automata/supplement.html)
  -wait for the output
  
### Here are a few results:
1. *Rule 60*
\
   ![image](https://user-images.githubusercontent.com/29653551/123817910-2c429100-d916-11eb-81b1-0566a1360397.png)
2. *Rule 90*
\
  ![image](https://user-images.githubusercontent.com/29653551/123818222-6e6bd280-d916-11eb-91af-c18be80ae9d7.png) 
  
3. *Rule 73*
\
  ![image](https://user-images.githubusercontent.com/29653551/123818750-dd492b80-d916-11eb-9703-58b7836792d3.png)

Note that the initial generation is taken to just have 1 live cell at the center.

### How to play my code:
  - you can change the initial state by manually changing the variable `current` declared in the python file. By default it is set to 499 `zeros` and only one `1` at the center.
  - my code only thinks about the nearest neighbour (i.e. left and right), maybe you can care about cells which are the neighbour of the nearest neighbours. In that case there will be 2<sup>32</sup> rules possible, which is equivalent to 4294967296 rules and you can just choose any. Think about how many cool patterns (and other things) you can generate from it.
\
Here is an example of state 887847937
\
![image](https://user-images.githubusercontent.com/29653551/123845115-6cfbd380-d931-11eb-8d48-e012f8b66806.png)
