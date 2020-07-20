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

## Launch

## Worlds
