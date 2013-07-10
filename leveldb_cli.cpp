

#include <string>
using namespace std;
#include <leveldb/db.h>

int main(int argc, const char** argv) {

	leveldb::DB* db;
	leveldb::Options options;
	options.create_if_missing = true;
	leveldb::Status status = leveldb::DB::Open(options, "./testdb", &db);

	char line [1024];
	while ( fgets(line, sizeof(line), stdin) ) {
		line[ strlen(line)-1 ] = 0;
		string key = line;
		fprintf(stderr, "Searching key[%s]\n", key.c_str());
	}

	return 0;
}
