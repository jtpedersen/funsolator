#include <tamed/beast.h>

#include <stdlib.h>

int main(int argc, char *argv[]) {
  CustomType bar;

  bar.injected_result = 3;

  if (interesting_fun(bar) == 4) {
    return EXIT_SUCCESS;
  } else {
    return EXIT_FAILURE;
  }
}
