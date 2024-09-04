#include "maze.h"

void render_walls(SDL_Renderer *renderer, double cameraX) {
    int map[8][8] = {
        {1, 1, 1, 1, 1, 1, 1, 1},
        {1, 0, 0, 0, 0, 0, 0, 1},
        {1, 0, 0, 1, 0, 0, 0, 1},
        {1, 0, 0, 1, 0, 0, 0, 1},
        {1, 0, 0, 0, 0, 0, 0, 1},
        {1, 0, 0, 0, 0, 0, 0, 1},
        {1, 0, 0, 0, 0, 0, 0, 1},
        {1, 1, 1, 1, 1, 1, 1, 1}
    };

    // Simple Raycasting to render walls
    for (int x = 0; x < SCREEN_WIDTH; x++) {
        // Example of casting a simple vertical line to represent walls
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        SDL_RenderDrawLine(renderer, x, 200, x, 400);
    }
}
