#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main() {

  /**
   * 0 -> Rock
   * 1 -> Paper
   * 2 -> Scissors
   *
   */

  srand(time(0));
  char p, c;
  int p_score = 0, c_score = 0;
  int round = 0, com = rand() % 3;
  char quit[5];
  switch (com) {
  case 0:
    c = 'r';
    break;
  case 1:
    c = 'p';
    break;
  case 2:
    c = 's';
    break;
  }
  do {
    printf("\nChoose r for Rock, p for Paper, s for Scissors: \n");
    scanf(" %c", &p);
    /**
     * Note the space before %c. There is a newline character while scanning
     * integer(a) which is picked up by %c so you need to get rid of it using a
     * space.
     */
    if ((p == 'r' && c == 'r') || (p == 'p' && c == 'p') ||
        (p == 's' && c == 's')) {
      printf("It is even!");
    }
    if ((p == 'r' && c == 's') || (p == 'p' && c == 'r') ||
        (p == 's' && c == 'p')) {
      printf("You won!");
      p_score++;
    }
    if ((p == 's' && c == 'r') || (p == 'r' && c == 'p') ||
        (p == 'p' && c == 's')) {
      c_score++;
      printf("Machine won!");
    }

    printf("Computer chose: %c\n", c);
    printf("\nWanna quit? (q for quit/n for continue): \n");
    scanf("%s", &quit);
    round++;
  } while (strcmp(quit, "q") != 0 || strcmp(quit, "n") == 0);
  printf("\n----------------------------------------\n");
  printf("Round: %d\nYou: %d\nComp: %d\n", round, p_score, c_score);
  if (p_score > c_score)
    printf("You won the competition, Bro!\n");
  else if (p_score > c_score)
    printf("Computer won the competition, brah!\n");
  else
    printf("Equality!\n");

  return 0;
}
