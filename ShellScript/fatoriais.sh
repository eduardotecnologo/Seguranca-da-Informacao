

#!/bin/bash

f() {
	for a in $(seq $*);
	do echo "f($a) = $(seq -s* $a|bc)";
done;
}
f 1 1 10
