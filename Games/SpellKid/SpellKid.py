
def spelling_challenge(word, art_correct, art_incorrect):
    while True:  # Use a while loop to keep asking until the correct input is given
        answer = input(f"Spell, {word.upper()}: ")
        user_input = answer.lower()  # Normalize the input to lowercase

        if user_input == word.lower():  # Check if the input matches the word
            print("\nYAY! That's Correct!")          
            print(art_correct)  # Print the ASCII art for the correct answer
            break  # Exit the loop if the input is correct
        else:
            print("\nSad sail says do it AGAIN.")
            print(art_incorrect)  # Prompt the user to try again

# ASCII art definitions here ...
cat_art_correct = r"""               
      /\_/\
 /\  / o o \
 //\\ \~(*)~/
 `  \/   ^ /
    | \|| ||
    \ '|| ||
     \)()-())
"""

art_incorrect = r"""    
                           .-=--.                
                         .' .--. '.              
                        :  : .-.'. :    _ _         
                        :  : : .': :   (o)o)     
                        :  '. '-' .'   ////      
                        _'.__'--=' '-.//i'       
                     .-'               /         
                     '---..____...---''    
"""

dog_art_correct = r"""               
    |\_/|                  
     | @ @   Woof! 
     |   <>              _  
     |  _/\------____ ((| |))
     |               `--' |   
 ____|_       ___|   |___.' 
/_/_____/____/_______|
"""
frog_art_correct = fr""" 
                            .-----.
                            /7  .  (
                           /   .-.  \
                          /   /   \  \
                         / `  )   (   )
                        / `   )   ).  \
                      .'  _.   \_/  . |
     .--.           .' _.' )`.        |
    (    `---...._.'   `---.'_)    ..  \
     \            `----....___    `. \  |
      `.           _ ----- _   `._  )/  |
        `.       /"  \   /"  \`.  `._   |
          `.    ((O)` ) ((O)` ) `.   `._\
            `-- '`---'   `---' )  `.    `-.
               /                  ` \      `-.
             .'                      `.       `.
            /                     `  ` `.       `-.
     .--.   \ ===._____.======. `    `   `. .___.--`     .''''.
    ' .` `-. `.                )`. `   ` ` \          .' . '  8)
   (8  .  ` `-.`.               ( .  ` `  .`\      .'  '    ' /
    \  `. `    `-.               ) ` .   ` ` \  .'   ' .  '  /
     \ ` `.  ` . \`.    .--.     |  ` ) `   .``/   '  // .  /
      `.  ``. .   \ \   .-- `.  (  ` /_   ` . / ' .  '/   .'
        `. ` \  `  \ \  '-.   `-'  .'  `-.  `   .  .'/  .'
          \ `.`.  ` \ \    ) /`._.`       `.  ` .  .'  /
    LGB    |  `.`. . \ \  (.'               `.   .'  .'
        __/  .. \ \ ` ) \                     \.' .. \__
 .-._.-'     '"  ) .-'   `.                   (  '"     `-._.--.
(_________.-====' / .' /\_)`--..__________..-- `====-. _________)
"""

big_truck_art_correct = fr"""
                       _____________________________________________________
                      |                                                     |
             _______  |                                                     |
            / _____ | |                       ACME MOO-VERS                 |
           / /(__) || |                                                     |
  ________/ / |OO| || |                                                     |
 |         |-------|| |                                                     |
(|         |     -.|| |_______________________                              |
 |  ____   \       ||_________||____________  |             ____      ____  |
/| / __ \   |______||     / __ \   / __ \   | |            / __ \    / __ \ |\
\|| /  \ |_______________| /  \ |_| /  \ |__| |___________| /  \ |__| /  \|_|/
   | () |                 | () |   | () |                  | () |    | () |
    \__/                   \__/     \__/                    \__/      \__/
 """

monster_truck_art_correct = fr"""
                                 (>|
                                 (>|======\\
                            ________||____ `\\
                        _-~~~~~~~~|~|~~~|~|  |\\
                       /          | |   | |  ||`\\
                     /_           | |   | |  ||  `\\
         ____-------(_|___________|_|___| |  ||    ||               _-~~~|
   _--~~~            |           =|       ||~~~~~~~~~~~~~~~~~~~~~~~~     |
  |]                 |            |       ||                             |
  |=   /~~~~~~~~~~\  |           /'       ||         /~~~~~~~~~~\        |
:~~~~/'  _ ----- _ `\~~~~~~~~~~~~~~~~~~~~~||~~~~~~~/'  _ ----- _ `\~~~~~~~~|
|   | _-~         ~-_|____________==______||______| _-~         ~-_| __--~
`~~~~/    _-----_    \___________________//______/-/    _-----_    \~~
    ;    / \ _ / \    .                           :    / \ _ / \    .
    |   | -((*))- |   |                           |   | -((*))- |   |
    |    \  / \  /    |                           |    \  / \  /    ,
     \    ~-----~    /                             \    ~-----~    /
      ~-_         _-~                           _---`-_         _-~
 --~~~|\~~ ----- ~\__--~~-\-^^^\___-~`~~---__--/       ~ ----- ~ -/_--~~\
"""



air_plane_art_correct = r"""
          ______
            _\ _~-\___
    =  = ==(____AA____D
                \_____\___________________,-~~~~~~~`-.._
                /     o O o o o o O O o o o o o o O o  |\_
                `~-.__        ___..----..                  )
                      `---~~\___________/------------`````
                      =  ===(_________D
"""

pray_art_correct = r"""
            .---.
           /-====)
           | / '(
          / /  _/
          | |-(    _
          / |  \  //|
         /  \   \/\/
        |    |\   /
        `-;./ ;-'
          |    \
          |     \
        _/       |
jgs .--/         /
    `''---`-----`
"""
bible_plane_art_correct = fr"""
   __________________________
  /\                         \
 /  \            ____         \
/ \/ \          /\   \         \
\ /\  \         \ \   \         \
 \  \  \     ____\_\   \______   \
  \   /\\   /\                \   \
   \ /\/ \  \ \_______    _____\   \
    \\/ / \  \/______/\   \____/    \
     \ / /\\         \ \   \         \
      \ /\/ \         \ \   \         \
       \\/ / \         \ \   \         \
  May   \ /   \         \ \   \         \
         \\  /\\         \ \   \         \
God Bless \ /\  \         \ \___\         \
           \\    \         \/___/          \
  you in    \  \/ \                         \
             \ /\  \_________________________\
 all  your    \  \ / ______________________  /
               \  / ______________________  /
Endeavors!!!    \/_________________________/
                                             LAW

"""

jesus_plane_art_correct = fr"""
                              |~~~~~|        _____       _____
         _____                  \~~~/ /~~~~\ /   __|     /   __|
        |  =  |\                 | | |  o  / \  /  _  _  \  /
        |  =  | \           |~|  | | | /~~~   \ \  || ||  \ \
        |  =  |  |          \ \_/  / | |___    \ \ ||_||   \ \
 _______|  =  |__|____       \____/  |_____||\__| ||___||\__| |
|          =          |\                    \____/      \____/
| =================== | \
|_______   =   _______|  |
 \      |  =  |\       \ |
  \_____|  =  | \_______\|
        |  =  |  |
        |  =  |  |
        |  =  |  |
        |  =  |  |
        |  =  |  |
        |  =  |  |
        |_____|  | 
        \      \ |      
         \______\|


"""


# Main game loop
while True:
    print("Hello, welcome to SpellKid!")
    input("Press Enter to start!")

    # Call the function for each word
    spelling_challenge("cat", cat_art_correct, art_incorrect)
    spelling_challenge("dog", dog_art_correct, art_incorrect)  # Reusing incorrect art for dog challenge
    spelling_challenge("frog", frog_art_correct, art_incorrect)
    spelling_challenge("big truck", big_truck_art_correct, art_incorrect)
    spelling_challenge("monster truck", monster_truck_art_correct, art_incorrect)
    spelling_challenge("air plane", air_plane_art_correct, art_incorrect)
    spelling_challenge("pray", pray_art_correct, art_incorrect)
    spelling_challenge("bible", bible_plane_art_correct, art_incorrect)
    spelling_challenge("jesus", jesus_plane_art_correct, art_incorrect)

    print("Congratulations, YOU WIN!!!!!!!")
    input("Press ENTER to receive your prize!")

    print(fr"""
                                                 *
 *                                                               *
          *
                          (             )
                  )      (*)           (*)      (
         *       (*)      |             |      (*)
                  |      |~|           |~|      |          *
                 |~|     | |           | |     |~|
                 | |     | |           | |     | |
                ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |.
           .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,.
         ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a,
        a@@@@@@@@@@@@@@@@@@@@@' . `@@@@@@@@@@@@@@@@@@@@@@@@a
        ;`@@@@@@@@@@@@@@@@@@'   .   `@@@@@@@@@@@@@@@@@@@@@';
        ;@@@`@@@@@@@@@@@@@'     .     `@@@@@@@@@@@@@@@@'@@@;
        ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@;
        ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@;
        ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;;
        ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;;
        ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@@;
    ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%,
 .%%%%%%;;;;;;;@@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%,
.%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%,
%%%%%%%%`;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;'%%%%%%%%
%%%%%%%%%%%%`;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;'%%%%%%%%%%%%
`%%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%'
  `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
      `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
             
                         
     
""")

    # Ask if the user wants to play again
    response = input("Play again? Yes or No: ").lower()

    # Check the user's input
    if response == "yes":
        # Restart the entire game
        continue
    else:
        # Exit the program
        print("Goodbye!")
        break
