# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/kinetic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/kinetic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/prajval/arduino_ws/devel;/home/prajval/autoware.ai/install/ymc;/home/prajval/autoware.ai/install/xsens_driver;/home/prajval/autoware.ai/install/lattice_planner;/home/prajval/autoware.ai/install/waypoint_planner;/home/prajval/autoware.ai/install/waypoint_maker;/home/prajval/autoware.ai/install/way_planner;/home/prajval/autoware.ai/install/op_utilities;/home/prajval/autoware.ai/install/op_simulation_package;/home/prajval/autoware.ai/install/op_local_planner;/home/prajval/autoware.ai/install/op_global_planner;/home/prajval/autoware.ai/install/lidar_kf_contour_track;/home/prajval/autoware.ai/install/op_ros_helpers;/home/prajval/autoware.ai/install/lane_planner;/home/prajval/autoware.ai/install/ff_waypoint_follower;/home/prajval/autoware.ai/install/dp_planner;/home/prajval/autoware.ai/install/waypoint_follower;/home/prajval/autoware.ai/install/vlg22c_cam;/home/prajval/autoware.ai/install/vision_ssd_detect;/home/prajval/autoware.ai/install/vision_segment_enet_detect;/home/prajval/autoware.ai/install/vision_lane_detect;/home/prajval/autoware.ai/install/vision_darknet_detect;/home/prajval/autoware.ai/install/vision_beyond_track;/home/prajval/autoware.ai/install/vehicle_socket;/home/prajval/autoware.ai/install/vehicle_model;/home/prajval/autoware.ai/install/vehicle_gazebo_simulation_launcher;/home/prajval/autoware.ai/install/vehicle_gazebo_simulation_interface;/home/prajval/autoware.ai/install/vehicle_description;/home/prajval/autoware.ai/install/trafficlight_recognizer;/home/prajval/autoware.ai/install/op_simu;/home/prajval/autoware.ai/install/op_planner;/home/prajval/autoware.ai/install/op_utility;/home/prajval/autoware.ai/install/lidar_euclidean_cluster_detect;/home/prajval/autoware.ai/install/vector_map_server;/home/prajval/autoware.ai/install/road_occupancy_processor;/home/prajval/autoware.ai/install/costmap_generator;/home/prajval/autoware.ai/install/object_map;/home/prajval/autoware.ai/install/naive_motion_predict;/home/prajval/autoware.ai/install/map_file;/home/prajval/autoware.ai/install/libvectormap;/home/prajval/autoware.ai/install/imm_ukf_pda_track;/home/prajval/autoware.ai/install/decision_maker;/home/prajval/autoware.ai/install/vector_map;/home/prajval/autoware.ai/install/vector_map_msgs;/home/prajval/autoware.ai/install/vectacam;/home/prajval/autoware.ai/install/udon_socket;/home/prajval/autoware.ai/install/twist_generator;/home/prajval/autoware.ai/install/tablet_socket;/home/prajval/autoware.ai/install/runtime_manager;/home/prajval/autoware.ai/install/mqtt_socket;/home/prajval/autoware.ai/install/tablet_socket_msgs;/home/prajval/autoware.ai/install/state_machine_lib;/home/prajval/autoware.ai/install/sound_player;/home/prajval/autoware.ai/install/sick_lms5xx;/home/prajval/autoware.ai/install/sick_ldmrs_tools;/home/prajval/autoware.ai/install/sick_ldmrs_driver;/home/prajval/autoware.ai/install/sick_ldmrs_msgs;/home/prajval/autoware.ai/install/sick_ldmrs_description;/home/prajval/autoware.ai/install/points2image;/home/prajval/autoware.ai/install/rosinterface;/home/prajval/autoware.ai/install/rosbag_controller;/home/prajval/autoware.ai/install/roi_object_filter;/home/prajval/autoware.ai/install/range_vision_fusion;/home/prajval/autoware.ai/install/pos_db;/home/prajval/autoware.ai/install/points_preprocessor;/home/prajval/autoware.ai/install/points_downsampler;/home/prajval/autoware.ai/install/pixel_cloud_fusion;/home/prajval/autoware.ai/install/lidar_localizer;/home/prajval/autoware.ai/install/pcl_omp_registration;/home/prajval/autoware.ai/install/pc2_downsampler;/home/prajval/autoware.ai/install/oculus_socket;/home/prajval/autoware.ai/install/obj_db;/home/prajval/autoware.ai/install/nmea_navsat;/home/prajval/autoware.ai/install/ndt_tku;/home/prajval/autoware.ai/install/ndt_cpu;/home/prajval/autoware.ai/install/multi_lidar_calibrator;/home/prajval/autoware.ai/install/microstrain_driver;/home/prajval/autoware.ai/install/memsic_imu;/home/prajval/autoware.ai/install/marker_downsampler;/home/prajval/autoware.ai/install/map_tools;/home/prajval/autoware.ai/install/map_tf_generator;/home/prajval/autoware.ai/install/log_tools;/home/prajval/autoware.ai/install/lidar_shape_estimation;/home/prajval/autoware.ai/install/lidar_point_pillars;/home/prajval/autoware.ai/install/lidar_naive_l_shape_detect;/home/prajval/autoware.ai/install/lidar_fake_perception;/home/prajval/autoware.ai/install/lidar_apollo_cnn_seg_detect;/home/prajval/autoware.ai/install/lgsvl_simulator_bridge;/home/prajval/autoware.ai/install/kvaser;/home/prajval/autoware.ai/install/kitti_launch;/home/prajval/autoware.ai/install/kitti_player;/home/prajval/autoware.ai/install/kitti_box_publisher;/home/prajval/autoware.ai/install/javad_navsat_driver;/home/prajval/autoware.ai/install/integrated_viewer;/home/prajval/autoware.ai/install/image_processor;/home/prajval/autoware.ai/install/hokuyo;/home/prajval/autoware.ai/install/graph_tools;/home/prajval/autoware.ai/install/gnss_localizer;/home/prajval/autoware.ai/install/gnss;/home/prajval/autoware.ai/install/glviewer;/home/prajval/autoware.ai/install/gazebo_world_description;/home/prajval/autoware.ai/install/gazebo_imu_description;/home/prajval/autoware.ai/install/gazebo_camera_description;/home/prajval/autoware.ai/install/garmin;/home/prajval/autoware.ai/install/freespace_planner;/home/prajval/autoware.ai/install/fastvirtualscan;/home/prajval/autoware.ai/install/ekf_localizer;/home/prajval/autoware.ai/install/ds4_msgs;/home/prajval/autoware.ai/install/ds4_driver;/home/prajval/autoware.ai/install/detected_objects_visualizer;/home/prajval/autoware.ai/install/decision_maker_panel;/home/prajval/autoware.ai/install/data_preprocessor;/home/prajval/autoware.ai/install/custom_msgs;/home/prajval/autoware.ai/install/calibration_publisher;/home/prajval/autoware.ai/install/autoware_health_checker;/home/prajval/autoware.ai/install/autoware_system_msgs;/home/prajval/autoware.ai/install/autoware_rviz_plugins;/home/prajval/autoware.ai/install/autoware_quickstart_examples;/home/prajval/autoware.ai/install/autoware_pointgrey_drivers;/home/prajval/autoware.ai/install/autoware_driveworks_interface;/home/prajval/autoware.ai/install/autoware_connector;/home/prajval/autoware.ai/install/autoware_camera_lidar_calibrator;/home/prajval/autoware.ai/install/astar_search;/home/prajval/autoware.ai/install/as;/home/prajval/autoware.ai/install/amathutils_lib;/home/prajval/autoware.ai/install/autoware_msgs;/home/prajval/autoware.ai/install/autoware_map_msgs;/home/prajval/autoware.ai/install/autoware_launcher_rviz;/home/prajval/autoware.ai/install/autoware_launcher;/home/prajval/autoware.ai/install/autoware_external_msgs;/home/prajval/autoware.ai/install/autoware_driveworks_gmsl_interface;/home/prajval/autoware.ai/install/autoware_config_msgs;/home/prajval/autoware.ai/install/autoware_can_msgs;/home/prajval/autoware.ai/install/autoware_build_flags;/home/prajval/autoware.ai/install/autoware_bag_tools;/home/prajval/autoware.ai/install/adi_driver;/home/prajval/catkin_ws/devel;/home/prajval/AuE8930/git_ws/AuE893Spring20_PrajvalVaskar/github_ws/devel;/opt/ros/kinetic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/prajval/arduino_ws/devel/env.sh')

output_filename = '/home/prajval/arduino_ws/build/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)