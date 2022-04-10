# battleship_game
A 2 player non-interactive battleship CLI game runner


Problem Statement :

The task is to develop a non-interactive battleship CLI game runner which should do the following:
1. Handle initial board configuration validation for 2 players.
2. Process a sequence of moves (shots) from each player.
3. Provide the game result, i.e. print who is the winner (if there is any) or report the simulation error in a user-
    friendly format with a clear statement why the simulation can not continue, e.g. ships are placed incorrectly
    or a player is trying to take a shot outside the game grid.


Configuration : 

1. There are two default configuration files P1config.py and P2config.py files 
    to configure the Battleship boards for each player. If nothing is specified then these two
    default configurations will be used to run the game.
2. Add your desired board configuration by replacing P1config.py and P2config.py files content.
    Replace the Board matrix with your desired matrix.
3. In each matrix 0 means water or empty area in the board and "S" means there is a part of the ship.
4. Ship Placement :
    a. Each player has their own board.
    b. Board should have rectangular dimensions.
    c. Ships can be oriented only horizontally or vertically.
    d. All ship units must be located inside the board.
    e. There must be at least a single unit of distance between any pair of ships, i.e. each player's ships can not overlap or
    be connected.


Start using the application :

1. Application is written on python3 and runs on the command line tool like Linux, MacOs etc.
2. To start the application we have to use the main file i.e Game.py
3. We need to pass the additional system arguments required to configure, initialize and start the game.
4. Run the Game.py by executing python3 Game.py <sys_arguments>
5. Example command :
    python3 src/Game.py p1 p2 p1 F0 B2 C2 E3 F3 G3 H3 A4 A5 D5 E5 A6 H6 I6 J6 C7 D7 D9 F9 H9
6. Arguments description :
    p1 and p2 : 1st and 2nd argument says the two player's names to identify them
    p1 : 3rd argument identifies the first playeer to start the game
    F0 B2 C2 E3... : The remaining arguments provides the sequence of moves/targets for each player
7. Output : 
    Example output : 

        <----------------------------->
        Validating P1 configuration: OK
        p2 has overlapping ships at D5 position
        p2 has overlapping ships at C6 position
        Simulation aborted
        <----------------------------->

        <----------------------------->
        Validating P1 configuration: OK
        Validating P2 configuration: OK
        Starting the game
        p1 shoots first
        F0 - Battleship destroyed
        B2 - Cruiser hit
        C2 - Cruiser destroyed
        E3 - Submarine hit
        F3 - Submarine hit
        G3 - Submarine hit
        H3 - Submarine destroyed
        A4 - Destroyer hit
        A5 - Destroyer hit
        D5 - Cruiser hit
        E5 - Cruiser destroyed
        p1 won!
        <----------------------------->


Furter enhancemets :

1. Modify the logic for printing the message when a ship is completely destroyed.
2. Add unit test cases
3. Add more validations
4. Make more decoupled components to be flexible for more players and more types of ships.
4. Optimize code
