From Clear Code YT:

https://www.youtube.com/watch?v=AY9MnQ4x3zk

# Movies vs. game, concept

- Movie = a lot of images shown in fast succession (frames) with added sound
- movies often run at 24 frames per second FPS (24 images per second)
- the human eye/brain assume the motion is fluent/fluid if it's shown images at fast enough rate
- 90min move: 5400seconds * 24 frames per second = 129,600 pictures with sound (on average)
- 3 ways to make movie: record irl with camera, draw images/animation, use digital computer generated animation
- all three images = a lot of images in rapid sucession
- video games also = a lot of images/frames in rapid succession

- in move, images are fixed. images do not change
- in video game, images are dynamically generated while game is running
- game's images change on the fly depending on what the game needs a the current moment
- example dynamic game situations: position of enemies, player movement, health bars/resources changing values simultaneously
- video game frames are updated automatically

- Video game takes player/user input to update what frame is being drawn
- in game, before the image is drawn, check player input
- movie generally does not take user input (pausing, fastforwarding, rewinding are inputs, but do not change the order of images displayed in movie)


## Video games at the conceptual level

- checking player input [called **the event loop**]
- event loop can also include timers 
- taking all of the necessary inputs to draw the current image
- use player input info to place elements on screen [player placement, enemy placement, point indicator, resources(health, stamina, etc.)]

- 1. player input/event loop => 2. placing elements on screen => 3. creates one frame
- after creating 1 frame, start cycle over again for the next frame, multiple times per second (30-60 times per second FPS depending on game programming and/or hardware limitations)

- frame creating cycle applies to 2d and 3d games
- 2d games = place 2d images on screen
- 3d games = place 3d models on screen
- draw lots of images in 2d and 3d

## Pygame overview

- pygame provides Python with key functionality to make games
- pygame can also be used to make movies, diplay graphs/data

- Pygame helps you draw images
- With just Python, drawing things on screen is difficult. Usually you just see console displaying text, image display and animation display = not easy
- Pygame helps you **create an app window** and **helps you display images**
- Pygame can play sounds
- Pygame checks for player input, mouse, keyboard, gamepad button presses 
- normal input() function in Python stops all of your code = useless for games
- Pygame gamedev tools: collision detection, creating text, timers [Pygame makes them easier, but they can be done without]
- Pygame not for advanced game development, use designated game engines like unity, unreal, godot, etc. that have more features
- Pygame not used often for commercial games

- Pygame used to learn coding/systems via problem solving that can be transferrable when learning other coding development = become better programmer
- learning a game engine only gives you skills to work with that specific engine, cannot develop without relying on game engine's toolset


## while pygame is running

- when code reaches its end, the game/app window will close automatically, this is intended
- in Python code is continuously running and does not reach an endpoint, the app window will continue to stay open until you close it
- can prevent closing with "while True" loop

	while True:
	
- must break while loop from the inside
- no conditions are set for "while True" to ever be False
- while True loop will run indefinitely = app window will always stay open

## Most common pygame event types (from pygame documentation)
- QUIT
- ACTIVEEVENT
- KEYUP
- KEYDOWN
- MOUSEMOTION
- MOUSEBUTTONUP
- MOUSEBUTTONDOWN
- JOYAXISMOTION
- JOYBALLMOTION
- JOYHATMOTION
- JOYBUTTONUP
- JOYBUTTONDOWN
- VIDEORESIZE
- VIDEOEXPOSE
- USEREVENT

## framerate

- movies = framerates are constant
- video games = framerate can vary depending on hardware, framerate and animation speed can become unstable/make game unplayable
- older hardware/weaker hardware = less performance/fps
- better hardware = better performance
- depending on game optimization (or lack thereof), more framerate can become a bad thing, if game engine, animations, game logic, etc. are not designed to be able to run at 1000fps. ex. game might run much faster (let's say 100x as fast as normal) speed if framerate is uncapped and 200 fps
- game must run consistently (to a reasonable level) on any platform: consistent 30fps or 60fps
- constant framerate is ideal, not too fast, not too slow => constant 60 fps
- 60fps ceiling (framecap) = easy
- 60fps floor (minimum framerate) = difficult to do => requires powerful hardware, game logic needs to be designed around high fps
- **one way of maintaining framerate: design game so there isn't too much on screen at one time (not too many things to render)**
- 

If a character moves 10pixels every frame
- normal: 1fps => 10pixels per second * 1fps => 10 pixels per second
- not normal: 100fps => 10px per second * 100fps => 1000px per second

