daxpy: daxpy.o
	g++ -static daxpy.o -o daxpy

daxpy.o: daxpy.cpp
	g++ -static -c daxpy.cpp -o daxpy.o

daxpy.s: daxpy.cpp
	g++ -static -S daxpy.cpp -o daxpy.s

clean:
	rm -f daxpy.o daxpy.s daxpy

