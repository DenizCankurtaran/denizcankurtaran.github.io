Cross Plattform Building tool für C++

# CMakeLists.txt
```
cmake_minimum_required(VERSION 3.4)
project(getting-started)
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")
set(CMAKE_CXX_STANDARD 14)
set(SOURCE_FILES main.cpp )
add_executable(test ${SOURCE_FILES})
```

# Verwendung
## Build Project
 - mkdir build
 - cmake -G "Unix Makefiles" build
 - make -C build/ all
 - build/executable
 
## opt
 - make clean
