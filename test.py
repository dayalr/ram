# python script for creating granular plot 
# requires files/dump.*
# creates tmp*.vtk
d = dump("dump_t.*")
v = vtk(d)
v.manyGran()

print "all done ... type CTRL-D to exit Pizza.py"
