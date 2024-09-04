#include "maze.h"

// Global variables
SDL_Window *gWindow = NULL;
SDL_Renderer *gRenderer = NULL;

void init() {
    SDL_Init(SDL_INIT_VIDEO);
    gWindow = SDL_CreateWindow("Raycasting", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
    gRenderer = SDL_CreateRenderer(gWindow, -1, SDL_RENDERER_ACCELERATED);
}

void close() {
    SDL_DestroyRenderer(gRenderer);
    SDL_DestroyWindow(gWindow);
    SDL_Quit();
}

int main() {
    init();

    int quit = 0;
    SDL_Event e;

    double cameraX = 0.0;

    while (!quit) {
        while (SDL_PollEvent(&e) != 0) {
            if (e.type == SDL_QUIT) {
                quit = 1;
            }
        }

        SDL_SetRenderDrawColor(gRenderer, 0, 0, 0, 255);
        SDL_RenderClear(gRenderer);

        render_walls(gRenderer, cameraX);

        SDL_RenderPresent(gRenderer);
    }

    close();

    return 0;
}
