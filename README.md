# MultiAgentPacman
Pacman AI 😎

**Multi Agent Pacman** is another version of pacman agent that will find its path with the minimax, alpha beta pruning, and expectimax to collect its foods, and the ghost while blinking.

You can use the commands below to run the project 

# List of commands Pacman AI
```
// For classic pacman game (you play)
python pacman.py 
// Easy 
python pacman.py -p ReflexAgent -l testClassic
// Reflex Agent with one ghost / two ghost 
python pacman.py --frameTime 0 -p ReflexAgent -k 1
python pacman.py --frameTime 0 -p ReflexAgent -k 2
// Minimax
python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
// Alpha beta Agent on small map
python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
```

# Video overview
<img src='http://i.imgur.com/IEpdZWC.gif' title='pacman' width='' alt='Video Walkthrough' />

The above shows the pacman behavior on reflex agent with two ghost.

# LeftTurnAgent

```
$ python pacman.py --pacman LeftTurnAgent -n 30 -q
Average Score: 236.76666666666668
Scores:        245.0, 220.0, 433.0, 428.0, 214.0, 420.0, 233.0, 233.0, 172.0, -365.0, 189.0, 105.0, 175.0, 376.0, 241.0, 228.0, -28.0, 637.0, 94.0, 395.0, 327.0, 391.0, -329.0, 443.0, 445.0, 10.0, 448.0, -57.0, 393.0, 387.0
Win Rate:      0/30 (0.00)
Record:        Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss
```

# GreedyAgent

```
$ python pacman.py --pacman GreedyAgent -n 30 -q
Average Score: 216.0
Scores:        -208.0, 57.0, 1559.0, -70.0, 482.0, 150.0, -329.0, 1300.0, -249.0, -99.0, 1600.0, 407.0, -383.0, 304.0, 591.0, -54.0, -13.0, -105.0, 260.0, 60.0, -239.0, 594.0, 341.0, 177.0, -26.0, 553.0, -275.0, -318.0, -196.0, 609.0
Win Rate:      3/30 (0.10)
Record:        Loss, Loss, Win, Loss, Loss, Loss, Loss, Win, Loss, Loss, Win, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss, Loss
```

# ReflexAgent

```
$ python pacman.py --pacman ReflexAgent -n 30 -q
Average Score: 307.8666666666667
Scores:        1268.0, -3.0, -6.0, 1220.0, -323.0, -31.0, 1082.0, 31.0, 92.0, 1288.0, 89.0, 30.0, -181.0, -61.0, -248.0, 1144.0, 1071.0, -237.0, 727.0, -62.0, -137.0, 1194.0, -64.0, 1156.0, 1058.0, -269.0, -82.0, -48.0, -374.0, -88.0
Win Rate:      10/30 (0.33)
Record:        Win, Loss, Loss, Win, Loss, Loss, Win, Loss, Loss, Win, Loss, Loss, Loss, Loss, Loss, Win, Win, Loss, Win, Loss, Loss, Win, Loss, Win, Win, Loss, Loss, Loss, Loss, Loss
```

# Minimax Agent

```
$ python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4 -q -n 50
Average Score: 152.52
Scores:        516.0, 516.0, 514.0, -492.0, -494.0, 516.0, 514.0, 516.0, 514.0, 516.0, -492.0, 516.0, -492.0, 514.0, 516.0, -492.0, 516.0, 516.0, 516.0, 516.0, -492.0, -494.0, 516.0, 516.0, 516.0, -492.0, -492.0, 514.0, 516.0, -492.0, -492.0, 514.0, 516.0, -495.0, 516.0, -492.0, -492.0, -492.0, 516.0, -492.0, 516.0, 516.0, -495.0, 514.0, 516.0, -494.0, 514.0, 514.0, 516.0, 516.0
Win Rate:      32/50 (0.64)
Record:        Win, Win, Win, Loss, Loss, Win, Win, Win, Win, Win, Loss, Win, Loss, Win, Win, Loss, Win, Win, Win, Win, Loss, Loss, Win, Win, Win, Loss, Loss, Win, Win, Loss, Loss, Win, Win, Loss, Win, Loss, Loss, Loss, Win, Loss, Win, Win, Loss, Win, Win, Loss, Win, Win, Win, Win
```
