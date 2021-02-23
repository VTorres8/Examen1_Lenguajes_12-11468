#include <stdio.h>
#include <time.h>


//X = 4
//Y = 6
//Z = 8

//Alfa: 3
//Beta: 7

//Pregunta 5.a: Subrutina recursiva que calcula los valores F para los valores de "alfa" y "beta".
//(Implementacion directa de la formula resultante a codigo)
int funcion_recursiva(int n){
	if(n>=0 && n<21){
		return n;
	}
	else if(n>= 21){
		return funcion_recursiva(n-7) + funcion_recursiva(n-14) + funcion_recursiva(n-21);
	}
}

//Pregunta 5.b: Pokevolucion a subrutina recursiva de cola que calcula F para "alfa" y "beta"
int funcion_recursiva_cola(int a1, int a2, int a3, int i, int n){
	if(i == n){
		return (a1 + a2 + a3);
	} return funcion_recursiva_cola(a1+a2+a3, a1, a2, i+7, n);

}

int llamada_funcion_rcola(int n){
	if(n<21){
		return n;
	}
	else{
		int i = 21 + (n % 7);
		return funcion_recursiva_cola(i - 7, i-14, i-21, i ,n);
	}
}

//Pregunta 5.c: Pokevolucion de la 5.b a una version iterativa
int funcion_iterativa(int n){
	if(n< 21){return n;}

	int i = 21 + (n % 7);
	int temporal, a1 = i - 7, a2 = i - 14, a3 = i- 21;
	while(i <= n ){
		temporal = a1 + a2 + a3;		
		a3 = a2;
		a2 = a1;
		a1 = temporal;
		i = i+7;
	}
	return a1;
}

//Main en el que se imprimen los resultados
void main(){

	int n[5] = {50, 100, 150, 200, 250};

	int i = 0;
	while (i < 5) {
		printf("\n\nProbamos las funciones para n = %i\n\n", n[i]);
		clock_t inicio, fin, total;

		inicio = clock();
		printf("5.a) Subrutina Recursiva: %i\n", funcion_recursiva(n[i]));
		fin = clock();
		total = fin - inicio;
		printf("La funcion recursiva toma: %f segundos.\n\n",((double) total / CLOCKS_PER_SEC));

		inicio = clock();
		printf("5.b) Pokevolucion Recursiva de Cola: %i\n", llamada_funcion_rcola(n[i]));
		fin = clock();
		total = fin - inicio;
		printf("La evolucion recursiva de cola toma: %f segundos.\n\n", ((double) total / CLOCKS_PER_SEC));

		inicio = clock();
		printf("5.c) Pokevolucion Iterativa: %i\n", funcion_iterativa(n[i]));
		fin = clock();
		total = fin - inicio;
		printf("La evolucion iterativa toma: %f segundos.\n\n", ((double) total / CLOCKS_PER_SEC));

		i = i+1;
	}

}