#include <stdio.h>

int isValid(char board[81], int row, int col, char ch){
  for(int i=0; i<9; i++){
    if(board[9 * i + col] == ch)
      return 0;
    if(board[9 * row + i] == ch)
      return 0;
    if(board[9 * (3*(row/3)+i/3) + (3*(col/3)+i%3)] == ch)
      return 0;
  }
  return 1;
}

int solve(char board[81]) {
  for(int i=0; i< 9; i++){
    for(int j=0; j< 9; j++){
      if(board[9 * i + j] == '.'){
        for(char ch='1'; ch<='9'; ch++){
          if(isValid(board, i, j, ch)){
            board[9 * i + j] = ch;
            if(solve(board))
              return 1;
            board[9 * i + j] = '.';
          }
        }
        return 0;
      }
    }
  }
  return 1;
}

void returnBoard(char board[81]){
  int i = 0;
  while (i < 81)
  {
    if (i!=0){
      if (i % 27 == 0)
        printf("\n\n");
      else if (i % 9 == 0)
        printf("\n");
      else if (i % 3 == 0)
        printf(" ");
    }
    printf("%c", board[i]);
    i++;
  }
}

int main(int argc, char **argv){
  FILE *f = fopen(argv[1], "r");
  char board[81];
  int i = 0;
  char c = ' ';
  while(c != EOF){
    c = fgetc(f);
    if (c == '.' || (c >= '0' && c <= '9')){
      board[i] = c;
      i++;
    }
  }
  fclose(f);

  solve(board);
  returnBoard(board);
  return 0;
}
