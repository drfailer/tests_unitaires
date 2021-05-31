#include <stdio.h>
#include "user_code.h"

int main(int argc, char ** argv) {
  if (somme(5, 6) == 11) {
    printf("test correcte pour 6 et 11\n");
  } else {
    printf("Echque du test: somme(6, 11)\n");
  }
  if (somme(-6, 6) == 0) {
    printf("test correcte pour -6 et 6\n");
  } else {
    printf("Echque du test: somme(-6, 6)\n");
  }
  return 0;
}
