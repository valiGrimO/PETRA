This layer is produced with the `Distance Map` plugin.
It should be configured as follow:
+ raycast mode: Normals, *default value*
+ normalization value: 0.1
+ positive color: pure Red
+ negative color: pure Green
+ out of range color: pure Blue, *but we don't care in reality*

**Note:**
**I succeed to change the default parameter, so we don't need to load this interface, we just have to select the 2 meshes (in the right order), and then hit `Generate Distance Map`!!!**

Then:
1. select the light mesh (worked with MeshLab)
2. `shift`+ click on the documented mesh
3. hit `Generate Distance Map`
4. apply the `r3_deviation_map` material

And under `Shading` tab, we have to:
5. set the right `vertex color` group
6. define the extreme values of the map range.
