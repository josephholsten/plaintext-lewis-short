#!/usr/bin/env sed -n -f
# Yes, the executable bit on this file is true!

# select only entries
1,/^A$/d
/^.$/d

# remove leading whitespace
s/^\s+\(.*\)$/\1/
s/^  \(.*\)$/\1/

# fortune-cookie-ize
i\
%
p
