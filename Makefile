$(CC) = gcc
final:
	$(CC) catlearn/simple_derivative.c -o final -lgsl -lm

run:
	./final

Clean:
	rm *.o final
