

leveldb_cli: leveldb_cli.cpp
	g++ leveldb_cli.cpp -o leveldb_cli -L ./lib -lleveldb -pthread

clean:
	find . -name '*.pyc' -o -name '*~' -o -name '*.o' | xargs rm
