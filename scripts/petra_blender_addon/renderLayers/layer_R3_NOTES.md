To produce this layer of information:
1. select the light mesh (worked with MeshLab)
2. `shift`+ click on the documented mesh
3. hit `Generate Distance Map`
4. apply the `r3_deviation_map` material

And under `Shading` tab, we have to:
5. set the right `vertex color` group
6. define the extreme values of the map range.

Future developments:
+ at the moment, the "middle value" between the extrem is 0. It could be usefull if we can change this value, for some reason.
+ It could be great also to in include "out of range" values (set in blue) in the covering layer.
