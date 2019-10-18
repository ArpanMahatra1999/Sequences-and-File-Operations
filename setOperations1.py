s = {1,2,3,'a','b'}
sub = {1,'a','b'}

print(1 in s)
print(5 not in s)
print(sub.issubset(s))
print(s.issuperset(s))
print(s.difference(sub))
print(s.symmetric_difference(sub))

sub2 = {'c'}

print(s.union(sub2))
print(s.intersection(sub))