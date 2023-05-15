# ROS Melodic Workspace

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) [![Coverage Status](http://img.shields.io/coveralls/badges/badgerbadgerbadger.svg?style=flat-square)](https://coveralls.io/r/badges/badgerbadgerbadger) [![MIT License](https://img.shields.io/github/license/iamrajee/slam_rosmelodic_ws.svg)](http://badges.mit-license.org) [![GitHub Issues](https://img.shields.io/github/issues/iamrajee/slam_rosmelodic_ws.svg)](https://github.com/iamrajee/slam_rosmelodic_ws/issues) [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/iamrajee/slam_rosmelodic_ws.svg)](https://github.com/iamrajee/slam_rosmelodic_ws/pulls) [![Gitter](https://badges.gitter.im/iamrajee-ROS/community.svg)](https://gitter.im/iamrajee-ROS/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) [![Join our Slack Workspace](https://img.shields.io/badge/Slack%20Workspace-roboticsclubiitpkd.slack.com-blue.svg?logo=slack&longCache=true&style=flat)](https://roboticsclubiitpkd.slack.com) 
<!---
[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-blue.svg)](https://www.firsttimersonly.com/)
[![Gem Version](http://img.shields.io/gem/v/badgerbadgerbadger.svg?style=flat-square)](https://rubygems.org/gems/badgerbadgerbadger)
--->
The below codebase is a ROS melodic workspace that contains a variety of packages for simultaneous localization and mapping (SLAM). Workspace is for testing various SLAM methods(Gmapping, Karto, Hector, Cartographer etc).The codebase is well-organized and easy to use. It includes a number of tutorials that provide instructions on how to use the SLAM packages. The codebase is a valuable resource for anyone who wants to learn about SLAM or who wants to use SLAM in their own projects.
<br/><br/>

## Table of content
- [Installation](https://github.com/iamrajee/slam_rosmelodic_ws#installation)
- [Package description](https://github.com/iamrajee/slam_rosmelodic_ws#package-description)
- [Helper scripts](https://github.com/iamrajee/slam_rosmelodic_ws#helper-scripts)
- [Team](https://github.com/iamrajee/slam_rosmelodic_ws#team)
- [Contributing](https://github.com/iamrajee/slam_rosmelodic_ws#contributing)
- [FAQ](https://github.com/iamrajee/slam_rosmelodic_ws#faq)
- [Support](https://github.com/iamrajee/slam_rosmelodic_ws#support)
- [License](https://github.com/iamrajee/slam_rosmelodic_ws#license)
- [Acknowledgments](https://github.com/iamrajee/slam_rosmelodic_ws#acknowledgments)
<!--- - [xyz](link) --->

---

## Installation

> All the `code` required to get started
- #### Prerequisite
    - You should have ROS melodic on your ubuntu 18.04.
    - All ROS dependency is satisfied.

- #### Clone

    ```
    git clone https://github.com/iamrajee/slam_rosmelodic_ws.git
    ```

- #### Setup
    ```
    cd slam_rosmelodic_ws/
    ./refresh.sh
    make
    ```
---


## Package description
* ## [test_slam](src/test_slam)
    
    ### Mapping
    > To do mapping run slam.launch file along with telop. Also, you can which slam_method to use among [Gmapping, Karto, Hector, Cartographer].
    ##### Run
    
    ```
    Terminal 1: roslaunch test_slam slam.launch slam_method:=gmapping          #here gmapping is default
    ```
    ```
    Terminal 2: roslaunch test_slam teleop.launch
    ```

    ### Navigation
    > After mapping you can run navigation by running navigation.launch file.
    ##### Run
    
    ```
    Terminal: roslaunch test_slam navigation.launch
    ```

Here are some details about the packages in the codebase:
gmapping: gmapping is a 2D SLAM package that uses a Rao-Blackwellized particle filter. It is a popular choice for SLAM applications that require low computational resources.
hector_slam: Hector_slam is a 2D SLAM package that uses a Hector laser scanner odometry and mapping algorithm. It is a good choice for SLAM applications that use a laser scanner.
slam_gmapping: slam_gmapping is a 2D SLAM package that combines the gmapping and Hector SLAM packages. It is a good choice for SLAM applications that require the best of both worlds.
cartographer: cartographer is a 3D SLAM package that uses a probabilistic graph SLAM algorithm. It is a good choice for SLAM applications that require high accuracy and robustness.
loam_livox: loam_livox is a 3D SLAM package that uses a LiDAR odometry and mapping algorithm. It is a good choice for SLAM applications that use a LiDAR sensor.

The codebase also includes a number of other packages that are used to support the SLAM packages, such as:
tf: A package that provides a transformation framework for ROS.
nav_msgs: A package that provides messages for navigation.
sensor_msgs: A package that provides messages for sensor data.
---
<br/><br/>
# Helper Scripts

* ## refresh.sh
    ```
    #!/bin/bash
    source /opt/ros/melodic/setup.bash
    source devel/setup.bash
    clear
    ```
    > It will source the workspace after buiding workspace or after creating new pkg. Run it as `./refresh.sh`

* ## makefile
    ```
    SHELL=/bin/bash
    all:
        make run
    run:
        catkin_make
        bash refresh.sh
    ```
    > It will build the workspace . Run it as `make`

* ## createpkg.sh
    ```
    #!/bin/bash
    cd src/
    catkin create $1
    cd ../
    make
    source refresh.sh
    ```
    > It will create new package . Run it as `./createpkg.sh newpkg_name`

* ## tftree.sh
    ```
    #!/bin/bash
    rosrun rqt_tf_tree rqt_tf_tree
    ```
    > It will  launch the gui to visvualise the tf tree. Run it as `./tftree.sh`

* ## printenv.sh
    ```
    #!/bin/bash
    printenv | grep -i ROS
    ```
    > It will print the ROS related environment variable . Run it as `./printenv.sh`

* ## rosdep.sh
    ```
    sudo rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y
    ```
    > It will install dependencies of all pkg in the workspace. Run it in the workspace as `./rosdep.sh`

* ## ssh_into_another_computer.sh
    ```
    #!/bin/bash
    ssh rajendra@rajendra
    ```
    > It will ssh into another system. Useful when using multiple ros masters. Run it as `./rajendra.sh`

---
<br/><br/>
## Team

> Or Contributors/supporters/mentors/guides who helped me out in these projects.
<!---
| <a href="https://github.com/MuskaanMaheshwari" target="_blank">**Muskaan Maheshwari**</a> | <a href="https://www.linkedin.com/in/sachin-rustagi-882b55145/" target="_blank">**Sachin Rustagi**</a> | <a href="https://www.linkedin.com/in/s-m-rafi-911442130/" target="_blank">**S M Rafi**</a> |
| :---: |:---:| :---:|
--->
| <a href="https://github.com/abhinand4as" target="_blank">**Abhinand A S**</a> | <a href="https://www.linkedin.com/in/sachin-rustagi-882b55145/" target="_blank">**Sachin Rustagi**</a> | <a href="https://www.linkedin.com/in/amin-swamiprasad-pkd-17732b152/" target="_blank">**Swami Prasad**</a> |
| :---: |:---:| :---:|
| ![](https://avatars1.githubusercontent.com/u/18076234?s=200&v=3) | ![](https://avatars0.githubusercontent.com/u/2555224?s=200&v=3) | ![](https://avatars0.githubusercontent.com/u/917816?s=200&v=3)  |


---

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/iamrajee/slam_rosmelodic_ws.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/iamrajee/slam_rosmelodic_ws/compare/" target="_blank">`https://github.com/iamrajee/slam_rosmelodic_ws/compare/`</a>.
---

## FAQ

- **I ran into some issue while running above package, what to do now?**
    - Simply contact me!

---

## Support
Reach out to me for any help!
|  |  |
| :---: | --- |
| ![](https://avatars0.githubusercontent.com/u/25712145?s=200&v=3) | Name : Rajendra Singh<br/> Email  : singh.raj1997@gmail.com<br/> Web    : https://iamrajee.github.io/<br/> LinkedIn    : https://www.linkedin.com/in/rajendra-singh-6b0b3a13a/<br/> Twitter: <a href="https://twitter.com/i_am_rajee" target="_blank">`@i_am_rajee`</a> |
|  |  |
 
---

## License

[![MIT License](https://img.shields.io/github/license/iamrajee/slam_rosmelodic_ws.svg)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright (c) 2019 [Rajendra Singh](https://iamrajee.github.io/).
---

## Acknowledgments

* Hat tip to anyone whose code was used and thanks to everyone who inspired and supported me in this project.

