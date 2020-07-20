# RUN
    
### Mapping
> To do mapping run slam.launch file along with telop. Also, you can which slam_method to use among [Gmapping, Karto, Hector, Cartographer].

```
Terminal 1: roslaunch test_slam slam.launch slam_method:=gmapping          #here gmapping is default
```
```
Terminal 2: roslaunch test_slam teleop.launch
```

### Navigation
> After mapping you can run navigation by running navigation.launch file.

```
Terminal: roslaunch test_slam navigation.launch
```

# Package Description

#### Launch
> Contains various launch files. It have four sub-folder inside.

#### Worlds
> Contain .world file, one which is used gazebo.

#### config
> Contains various configuration file like 

#### maps
> Contains saved map files

#### meshes
> Contains mesh files which are used in robot

#### param
> Contains param files like base_local_planner_params.yaml.

#### rviz
> Contains saved rviz configuration.

#### urdf
> Contains robot model urdfs. Here burger.
