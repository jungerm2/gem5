all: daxpy.o single-sided.o double-sided.o
	g++ -static daxpy.o -o daxpy
	g++ -static single-sided.o -o single-sided
	g++ -static double-sided.o -o double-sided 


daxpy: daxpy.o
	g++ -static daxpy.o -o daxpy

single-sided: single-sided.o
	g++ -static single-sided.o -o single-sided

double-sided: double-sided.o
	g++ -static double-sided.o -o double-sided




daxpy.o: daxpy.cpp
	g++ -static -c daxpy.cpp -o daxpy.o

single-sided.o: single-sided.cpp
	g++ -static -c single-sided.cpp -o single-sided.o

double-sided.o: double-sided.cpp
	g++ -static -c double-sided.cpp -o double-sided.o




daxpy.s: daxpy.cpp
	g++ -static -S daxpy.cpp -o daxpy.s

single-sided.s: single-sided.cpp
	g++ -static -S single-sided.cpp -o single-sided.s

double-sided.s: double-sided.cpp
	g++ -static -S double-sided.cpp -o double-sided.s



clean:
	rm -f daxpy.o daxpy.s daxpy single-sided.o single-sided.s single-sided double-sided.o double-sided.s double-sided

