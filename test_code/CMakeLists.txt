set(beast "${CMAKE_CURRENT_SOURCE_DIR}/../production_code/gnarly_beast.cpp")

add_custom_command(
  OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/tamed/beast.cpp ${CMAKE_CURRENT_SOURCE_DIR}/tamed/beast.h
  COMMAND  python3 ${CMAKE_CURRENT_SOURCE_DIR}/funsolator.py ${beast} ${CMAKE_CURRENT_SOURCE_DIR}/beast.template 
  DEPENDS ${beast} ${CMAKE_CURRENT_SOURCE_DIR}/beast.template
  VERBATIM
)


function(fun_test name)
  add_executable(${name} ${ARGN})
  target_include_directories(${name}
    PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

  add_test(NAME ${name}
    COMMAND  $<TARGET_FILE:${name}>
    )
endfunction(fun_test)


fun_test(tame_beast test_beast.cpp tamed/beast.cpp)
