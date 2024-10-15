# Parameters

Agents (`-p` flag):
- MinimaxAgent
- AlphaBetaAgent

Evaluation function (`-a evalFn=...`):
- `dumb`: lab requirement (pellet dist + ghost dist)
- `dumb2`: `dumb` + game score
- `dumbAstar`: `dumb2` using A* search


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

# Minimax with alpha-beta pruning

We want to compare the performance with and without pruning.
```
$ time python pacman.py -p AlphaBetaAgent -l originalClassic -a evalFn=dumb2,depth=2 -q
Pacman died! Score: 1317
Average Score: 1317.0
Scores:        1317.0
Win Rate:      0/1 (0.00)
Record:        Loss
python pacman.py -p AlphaBetaAgent -l originalClassic -a evalFn=dumb2,depth=2  8.63s user 0.07s system 99% cpu 8.718 total
```

# BFS vs A* performance

Using 5 runs on the original layout with 4 ghosts.

With BFS it took 2 minutes.
```
time python pacman.py -p MinimaxAgent -l originalClassic -a evalFn=dumb2,depth=2 -q -n 5
Pacman emerges victorious! Score: 2660
Pacman emerges victorious! Score: 3063
Pacman emerges victorious! Score: 2661
Pacman emerges victorious! Score: 2839
Pacman emerges victorious! Score: 2673
Average Score: 2779.2
Scores:        2660.0, 3063.0, 2661.0, 2839.0, 2673.0
Win Rate:      5/5 (1.00)
Record:        Win, Win, Win, Win, Win
python pacman.py -p MinimaxAgent -l originalClassic -a evalFn=dumb2,depth=2 -  118.30s user 0.54s system 99% cpu 1:59.34 total
```

With A* it's 2:16, a bit slower.
```
$ time python pacman.py -p MinimaxAgent -l originalClassic -a evalFn=dumbAstar,depth=2 -q -n 5
Pacman emerges victorious! Score: 2875
Pacman emerges victorious! Score: 2870
Pacman emerges victorious! Score: 2879
Pacman died! Score: 164
Pacman died! Score: 1159
Average Score: 1989.4
Scores:        2875.0, 2870.0, 2879.0, 164.0, 1159.0
Win Rate:      3/5 (0.60)
Record:        Win, Win, Win, Loss, Loss
python pacman.py -p MinimaxAgent -l originalClassic -a  -q -n 5  135.62s user 0.37s system 99% cpu 2:16.32 total
```

Now let's try with only 1 ghost.

BFS: 24 seconds.
```
$ time python pacman.py -p MinimaxAgent -l originalClassic -a evalFn=dumb2,depth=2 -q -n 5 -k 1    
Pacman emerges victorious! Score: 2882
Pacman emerges victorious! Score: 2692
Pacman emerges victorious! Score: 2680
Pacman emerges victorious! Score: 2452
Pacman emerges victorious! Score: 2484
Average Score: 2638.0
Scores:        2882.0, 2692.0, 2680.0, 2452.0, 2484.0
Win Rate:      5/5 (1.00)
Record:        Win, Win, Win, Win, Win
python pacman.py -p MinimaxAgent -l originalClassic -a evalFn=dumb2,depth=2 -  23.89s user 0.16s system 99% cpu 24.118 total
```

A*: 24 seconds.
```
$ time python pacman.py -p MinimaxAgent -l originalClassic -a evalFn=dumbAstar,depth=2 -q -n 5 -k 1
Pacman emerges victorious! Score: 2435
Pacman emerges victorious! Score: 2489
Pacman emerges victorious! Score: 2457
Pacman emerges victorious! Score: 2478
Pacman emerges victorious! Score: 2480
Average Score: 2467.8
Scores:        2435.0, 2489.0, 2457.0, 2478.0, 2480.0
Win Rate:      5/5 (1.00)
Record:        Win, Win, Win, Win, Win
python pacman.py -p MinimaxAgent -l originalClassic -a  -q -n 5 -k 1  23.71s user 0.16s system 99% cpu 23.931 total
```
