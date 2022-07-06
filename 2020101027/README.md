Assumptions : 
The barbarian can move in all directions and the distance to nearest now walll building is considered in terms of euclidian distance
Two barbarians are not on the same tile.
The king is represented by K
the barbarians with B
The townhall with T, huts with H, walls with W, cannon C.

I have used codepos, colorpos, buildingclass, personclass variables to store all the details regarding the state of the game and to make accurate movements of barbarians as well as attack by the cannon. I have assigned a specific code and color to each person and wall and depending on the code the background and stuff changes. If health drops to zero of any object it permanently disappears. The heal spell and ragespells work on attributes by increasing them. There it the time factor in while loop which can be changed by the rage spell. 
Introduced balloonclass to work with balloons and when a balloon howers over something, the symbol changes to a number for distinction. The archer queen works similar to king with the except of area of effect and archer works similar to cannon. There is a limit on number of troops we can pick and levels have been implemented. The wizrd tower checks for balloons, if not there attacks the troops when checking the same place for both.