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
> Contains various launch files related to slam, navigation, gazebo, slam_methods.

#### Worlds
> Contain .world file, one which is used gazebo.

#### maps
> This is where map files are saved.

#### meshes
> Contains mesh files which are used in robot

#### param
> Contains param files like base_local_planner_params.yaml

#### config
> Contains other configuration file like karto_mapper_params.yaml

#### rviz
> Contains saved rviz configuration.

#### urdf
> Contains robot model urdfs. Here burger.
