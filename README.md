# TimerCalculator_PIC
Program to calculate the counter time in PIC's and give the preloading (in hexadecimal). The file "basic_code.py' contains the logic structure of the program, but without the interface. The file 'main_interface' contains the final version of the code, and the file 'TmrCalcPIC.exe' is the final project, in an executable archive generated by the pyinstaller library.

To generate the .exe program:
pyinstaller --onefile --noconsole arquivo.py (using the library PyInstaller - pip install pyinstaller)
