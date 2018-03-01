/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
#include <iostream>
#include <ctime>

using namespace std;

int main (){
  unsigned time0, time1;

  
  //Se prueba con siete matrices distintas en tamaño de forma incremental
  for (int n=3; n<=10; n++){
      time0=clock();
      int matx[n][n];
      int suma=0;
      //Se crea la matriz identidad.
      for (int i=0; i<n; i++){
	    for (int j=0; j<n; j++){
	          matx[i][j]=1;
	        }
	    }
      //Se suman las posiciones de la matriz triangular superior.
      for (int i=0; i<n; i++){
	    for (int j=0; j<n; j++){
	            suma+=matx[i][j];
	            j++;
	        }
	    }  
	  //Se imprimen resultados, tanto del programa como de su rendimiento.
      cout<<"Suma elementos matriz triangular superior: "<<suma<<endl;
      time1=clock();
      double t_exe=(double (time1-time0)/CLOCKS_PER_SEC);
      cout<<"Tiempo de ejecución: "<<t_exe<<endl;
      for (int i=0; i<n; i++){
	    for (int j=0; j<n; j++){
	        matx[i][j]=0;
	        }
	    }
    }
}