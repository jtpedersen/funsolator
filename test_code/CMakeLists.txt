set(beast "${CMAKE_CURRENT_SOURCE_DIR}/../production_code/gnarly_beast.cpp")

add_custom_command(
  OUTPUT tamed_beast.cpp
  COMMAND  python3 ${CMAKE_CURRENT_SOURCE_DIR}/funsolator.py ${beast} ${CMAKE_CURRENT_SOURCE_DIR}/tamer.template 
  MAIN_DEPENDCY ${CMAKE_CURRENT_SOURCE_DIR}/tamer.template
  DEPENDS ${beast}
  VERBATIM
)

function(fun_test name)
  add_executable(${name} ${ARGN})
  add_test(NAME ${name}
    COMMAND  $<TARGET_FILE:${name}>
    )
endfunction(fun_test)


fun_test(tame_beast test_beast.cpp tamed_beast.cpp)
