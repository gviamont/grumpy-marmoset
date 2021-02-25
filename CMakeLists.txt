# Copyright 2021 The Knights of Ni

cmake_minimum_required(VERSION 3.11)
project(grumpy-marmoset)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

add_subdirectory(src)
add_subdirectory(test)
