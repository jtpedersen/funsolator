#include <cassert>

#define TESTCASE(X) int testcase()

#define ASSERT(A, B)                                                           \
  do {                                                                         \
    assert(A == B);                                                            \
  } while (0)

#define RUN_TESTS                                                              \

