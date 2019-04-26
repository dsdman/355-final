#/bin/sh

./csce-dfa-project-test -d src -t test-suite
rm src/comments.bak
cat src/comments.txt
