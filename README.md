# VibeAI

## Environment setup

### 
ctrl - shift - v to open README in preview mode 

### Create virtual environment
Create a virtual environment with below or similar command 
```
python3.10 -m venv .venv
```

### Install requirements 
```
pip install -r requirements.txt
```

## Initial ideas

### Building our local library 
- We need a way to find new songs as we build out our local storage of metadata. For now I'm focusing on the search API call. 
-> https://developer.spotify.com/documentation/web-api/reference/search
 
- Not really how it works yet but it seems like you can use genres in the search filters. I think categories can be used as tag filters in the search query too. There are other filters like date. So I would like to work on getting all the genres and categories we can then working on a dynamic search process that will continually find new songs. Once we have those new songs we can fetch their metadata. 


# ☢☢☢

                      (      )
                      ~(^^^^)~
                       ) @@ \~_          |\
                      /     | \        \~ /
                     ( 0  0  ) \        | |       Hey
                      ---___/~  \       | |           Hiya
                       /'__/ |   ~-_____/ |                Doin?
        o          _   ~----~      ___---~
          O       //     |         |
                 ((~\  _|         -|                Oops! I mean MOOOOOOO
           o  O //-_ \/ |        ~  |
                ^   \_ /         ~  |
                       |          ~ |
                       |     /     ~ |
                       |     (       |
                        \     \      /\               
                       / -_____-\   \ ~~-*
                       |  /       \  \       .==.
                       / /         / /       |  |
                     /~  |      //~  |       |__|




     ________  ________  ________           ________  ________   ________     
    |\   ___ \|\   __  \|\   ___  \        |\   __  \|\   ___  \|\   ___ \    
    \ \  \_|\ \ \  \|\  \ \  \\ \  \       \ \  \|\  \ \  \\ \  \ \  \_|\ \   
     \ \  \ \\ \ \   __  \ \  \\ \  \       \ \   __  \ \  \\ \  \ \  \ \\ \  
      \ \  \_\\ \ \  \ \  \ \  \\ \  \       \ \  \ \  \ \  \\ \  \ \  \_\\ \ 
       \ \_______\ \__\ \__\ \__\\ \__\       \ \__\ \__\ \__\\ \__\ \_______\
        \|_______|\|__|\|__|\|__| \|__|        \|__|\|__|\|__| \|__|\|_______|
                                                                              
                                                                              
                                                                              
        ___  ___  ___  ___       ___  ________  ________   ________           
       |\  \|\  \|\  \|\  \     |\  \|\   __  \|\   ___  \|\   ____\          
       \ \  \ \  \\\  \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \  \___|_         
     __ \ \  \ \  \\\  \ \  \    \ \  \ \   __  \ \  \\ \  \ \_____  \        
    |\  \\_\  \ \  \\\  \ \  \____\ \  \ \  \ \  \ \  \\ \  \|____|\  \       
    \ \________\ \_______\ \_______\ \__\ \__\ \__\ \__\\ \__\____\_\  \      
     \|________|\|_______|\|_______|\|__|\|__|\|__|\|__| \|__|\_________\     
                                                             \|_________|     
                                                                              
                                                                              
     ________  ___                                                            
    |\   __  \|\  \                                                           
    \ \  \|\  \ \  \                                                          
     \ \   __  \ \  \                                                         
      \ \  \ \  \ \  \                                                        
       \ \__\ \__\ \__\                                                       
        \|__|\|__|\|__|                                                       
