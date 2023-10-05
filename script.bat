@echo off
rem Compilar el programa Flex
flex Analizador
echo "FLEX creo lex.yy.c"
pause

gcc.exe lex.yy.c -o Analizador.exe
echo "Se compilo el ANALIZADOR"
pause

Analizador.exe Ejemplo.c
echo "Fin del analisis"
pause