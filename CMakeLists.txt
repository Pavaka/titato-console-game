cmake_minimum_required (VERSION 2.8.11)
project(TitatoConsoleGame)
SET(SOURCE
    "src/main.cpp"
)
add_subdirectory("external/titato-lib")
include_directories(
    "${PROJECT_SOURCE_DIR}/external/titato-lib/include"
)

add_executable(TitatoConsoleGame ${SOURCE} ${HEADERS})
target_link_libraries(TitatoConsoleGame TitatoGameCore)