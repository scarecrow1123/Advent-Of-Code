cmake_minimum_required(VERSION 3.18 FATAL_ERROR)
project(aoc20 VERSION 0.1.0 LANGUAGES CXX)
set(CMAKE_BUILD_TYPE Release)

add_executable(aoc20_day1 src/day01.cpp)

add_executable(aoc20_day2 src/day02.cpp)
target_compile_features(aoc20_day2 PUBLIC cxx_std_17)
