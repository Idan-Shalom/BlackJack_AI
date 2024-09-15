# BlackJack_AI
This is a repo for the final project in AI course at the Hebrew university of Jerusalem. The project tries to solve blackJack using AI and compare different agents behaviors. 

The project uses Unity engine and c#, both must be faimiliar to the user in order to try the project.
Unity version we used - 2021.3.31f1

# Unity set up and guidance
The unity project is inside "Unity-Blackjack-Game-Tutorial-master-2" folder.
## Main Scene
The main scene is called "game". It already has all the assets needed. We consructed 2 game "modes":
1. Regular BlackJack game:
     The game is compatible with up to 3 players to choose (from different behaviours and algprithms such as RL player, ExpcetiMax Player, Mimic the dealer Player, Never bust           Player and more) not including the dealer. The scene has 3 Player GameObjects - "bottom", "right", "left" with player script on each one. It also has GameManager gameobject        with GameManager script.  You can change the scripts on the players to the one you want to play with and add it to the list in the gameManager script on the gameManager using      the inspector.
2. Sruvival mode:
   Same as before, but the only change is you need to deactivate the gameManager script on the GameManager gameobject and activate the survivalManager script on the same gameobject.
   The survival mode simulates a game with 1000 dollars to each player and continues until everyone busts. Using this mode, we were able to compare how different agents last in a      game comparing to others.

* Additional info - Time between each game can be controlled by a parameter in the GameManager script. 

* Make sure in the RLPLayer script to give the qTable a path to the "qTable2.json" provided in the repo. This is the qTable result from the RL player training.

  
# Plotting
## "plotting" folder
To create the figures shown in the article and video, run plots.py.
To create the animations of the results shown in the video, run 

# Scripts
You can view the AI as well as all other scripts for the game. 
* RL training is in "TrainingScript" folder. 
* RL Player script - "Unity-Blackjack-Game-Tutorial-master-2/Assets/Scripts/RL_Player_Q_learning.cs"
* ExpectiMax players - "Unity-Blackjack-Game-Tutorial-master-2/Assets/Scripts/ExpectiMaxUnified.cs"
* All rest of the players AND game classes are also in "Unity-Blackjack-Game-Tutorial-master-2/Assets/Scripts"





