# Reinforcement-Learning-Challenge

## How to setup project

> On your windows terminal 
>```
>python -m venv venv
>```
>```
>\venv\Scripts\activate 
>```
>```
>pip install -r requirements.txt
>```

## How to change game modes
> - play 
> - RandomlyAgent -> random
> - ValueIterationAgent -> value 
> - QLearningAgent -> q-l 
> 
> In the ``main.py`` file change the ``game_type`` parameter
>  ```python
> game = Game("RL-Challenge" , map_path, cell_size, game_type="q-l",  fps=120) 
> game.start() 
>```