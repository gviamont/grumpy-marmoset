# Copyright 2021 The Knights of Ni

find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

add_executable(grumpy-marmoset-test grumpy-marmoset-test.cpp ${PROJECT_SOURCE_DIR}/src/array_board.cpp)

target_include_directories(grumpy-marmoset-test PUBLIC ${PROJECT_SOURCE_DIR}/include ${PROJECT_SOURCE_DIR}/test)
target_link_libraries(grumpy-marmoset-test ${GTEST_LIBRARIES} pthread)
