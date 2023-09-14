#include <SDL2/SDL.h>
#include <SDL2_Image/SDL_image.h>
 
int main(int argc, char ** argv)
{
    char* angle_string = argv[1];
    int angle = atoi(angle_string);
    
    int quit = 0;
    SDL_Event event;
 
    SDL_Init(SDL_INIT_VIDEO);
 
    SDL_Window * window = SDL_CreateWindow("SDL2 Grayscale", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 640, 480, 0);
    SDL_Renderer * renderer = SDL_CreateRenderer(window, -1, 0);
    SDL_Surface * image = IMG_Load("sudoku.png");
    SDL_Texture * texture = SDL_CreateTexture(renderer,SDL_PIXELFORMAT_ARGB8888, SDL_TEXTUREACCESS_STATIC,image->w, image->h);
 
    SDL_Surface * originalImage = image;
    image = SDL_ConvertSurfaceFormat(image, SDL_PIXELFORMAT_ARGB8888, 0);
    SDL_FreeSurface(originalImage);
    	
    Uint32 * pixels = (Uint32 *)image->pixels;

    for (int y = 0; y < image->h; y++)
    {
      for (int x = 0; x < image->w; x++)
      {
        Uint32 pixel = pixels[y * image->w + x];
        Uint8 r = pixel >> 16 & 0xFF;
        Uint8 g = pixel >> 8 & 0xFF;
        Uint8 b = pixel & 0xFF;

        	
        Uint8 v = 0.212671f * r + 0.715160f * g + 0.072169f * b;    

        pixel = (0xFF << 24) | (v << 16) | (v << 8) | v;
        pixels[y * image->w + x] = pixel;
      }
    }

    


    while (!quit)
    {
        SDL_UpdateTexture(texture, NULL, image->pixels,image->w * sizeof(Uint32));
        SDL_WaitEvent(&event);
 
        switch (event.type)
        {
            case SDL_QUIT:
                quit = 1;
                break;
        }
 
        SDL_RenderCopyEx(renderer, texture, NULL, NULL, angle, NULL, SDL_FLIP_NONE );
        SDL_RenderPresent(renderer);
    }
 
    SDL_DestroyTexture(texture);
    SDL_FreeSurface(image);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    IMG_Quit();
    SDL_Quit();
 
    return 0;
}