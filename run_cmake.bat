call "%VS140COMNTOOLS%vsvars32.bat"
set cwd=%cd%
cmake -G "Visual Studio 14 2015 Win64" -B%cwd%/Projects -H%cwd%