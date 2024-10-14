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

Takes about 2 minutes:
```
$ python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4 -q -n 50
Average Score: 293.78
Scores:        -495.0, 516.0, 516.0, 516.0, 516.0, 516.0, 516.0, 516.0, 516.0, 516.0, 516.0, 516.0, -494.0, 516.0, 516.0, -492.0, 516.0, 516.0, 516.0, 516.0, 516.0, -492.0, 514.0, -494.0, 516.0, 516.0, 516.0, 516.0, 516.0, 516.0, -492.0, -494.0, 514.0, 516.0, 516.0, 516.0, -492.0, 516.0, 514.0, 516.0, 516.0, 516.0, 516.0, 516.0, 514.0, 516.0, -495.0, 516.0, -492.0, -495.0
Win Rate:      39/50 (0.78)
Record:        Loss, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Loss, Win, Win, Loss, Win, Win, Win, Win, Win, Loss, Win, Loss, Win, Win, Win, Win, Win, Win, Loss, Loss, Win, Win, Win, Win, Loss, Win, Win, Win, Win, Win, Win, Win, Win, Win, Loss, Win, Loss, Loss
```

Picking an evaluation function:
```
$ python pacman.py -p MinimaxAgent -a evalFn=dumbEvalFunc
```

# Minimax with improved scoring (`Dumb2EvalFunc`)

```
$ python pacman.py -p MinimaxAgent -a evalFn=dumb2,depth=2 -q -n 30
Average Score: 1617.3333333333333
Scores:        222.0, 1540.0, 1730.0, 1738.0, 1934.0, 1737.0, 1735.0, 1335.0, 1545.0, 1742.0, 1540.0, 1721.0, 1937.0, 1337.0, 1716.0, 1536.0, 1724.0, 1531.0, 1741.0, 1542.0, 1539.0, 1339.0, 1739.0, 1521.0, 1924.0, 1537.0, 1931.0, 1537.0, 1945.0, 1925.0
Win Rate:      29/30 (0.97)
Record:        Loss, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win
```

# BFS vs A* performance

It's noticeably slower on the trickyClassic layout,
probably because of BFS.
A single run takes almost 40s.
```
$ time python pacman.py -p MinimaxAgent -l trickyClassic -a evalFn=dumb2,depth=2 -q 
Pacman emerges victorious! Score: 1472
Average Score: 1472.0
Scores:        1472.0
Win Rate:      1/1 (1.00)
Record:        Win
python pacman.py -p MinimaxAgent -l trickyClassic -a evalFn=dumb2,depth=2 -q  38.11s user 0.19s system 99% cpu 38.403 total
```
