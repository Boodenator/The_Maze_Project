#ifndef MAZE_H
#define MAZE_H

#include <SDL2/SDL.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

// Screen dimensions
#define SCREEN_WIDTH 800
#define SCREEN_HEIGHT 600

// Function prototypes
void init();
void close();
void render_walls(SDL_Renderer *renderer, double cameraX);

#endif
