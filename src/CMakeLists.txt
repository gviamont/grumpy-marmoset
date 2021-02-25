# Copyright 2021 The Knights of Ni

add_executable(grumpy-marmoset grumpy-marmoset.cpp array_board.cpp)

target_include_directories(grumpy-marmoset PUBLIC ${PROJECT_SOURCE_DIR}/include)
