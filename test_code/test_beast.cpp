#include <tamed/beast.h>

int testcase() {

  foo bar;

  bar.loaded_from_weird_system = 3;
  return interesting_fun(bar) != 4;
}

int main(int argc, char *argv[]) { return testcase(); }
