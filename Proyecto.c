%option noyywrap

%{
#include <stdio.h>
%}

DIGITOS			[0-9]+
LETRAS          [a-zA-Z]+

%%

//  ESTRUCTURAS
int                 { printf("INT "); }
float               { printf("FLOAT "); }
short               { printf("SHORT "); }
long                { printf("LONG "); }
char                { printf("CHAR "); }
void                { printf("VOID "); }
if                  { printf("IF "); }
else                { printf("ELSE "); }
while               { printf("WHILE "); }
for                 { printf("FOR "); }
return              { printf("RETURN "); }
break               { printf("BREAK "); }
static              { printf("STATIC "); }
const               { printf("CONST "); }



// VARIABLES Y NUMEROS
{DIGITOS}           { printf("NUMERO(%s) ", yytext); }
{DIGITOS}.{DIGITOS} { printf("NUMEROFLOAT(%s) ", yytext); }

{LETRAS}            { printf("IDENTIFICADOR(%s) ", yytext); }

// OPERADORES
=                   { printf("ASIGNACION "); }
==                  { printf("IGUALDAD "); }
+                   { printf("SUMA "); }
-                   { printf("RESTA "); }
*                   { printf("MULTIPLICACION "); }
/                   { printf("DIVICION "); }


// OTROS
[;]                 { printf("FL \n"); }
[ \t\n]             // Ignorar espacios en blanco y saltos de línea
.                   { printf("Error: Caracter desconocido (%s) ", yytext); }

%%

int main() {
    yylex();
    printf("FIN\n"); // Agregar una marca al final de la salida
    return 0;
}