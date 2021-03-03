#! /usr/bin/env python
import rospy
from sensor_msgs.msg import NavSatFix
#import data file here
 
rospy.init_node('/my_gps_node')
pub = rospy.Publisher('/my_gps_topic',NavSatFix, queue_size=1)
rate = rospy.Rate(2)
location = NavSatFix()
#location.longitude =  importing data from data coords file 
#location.latitude =       ^

while not rospy.is_shutdown(): 
 pub.publish(location)
 ros.loginfo("Longitude: %f \n Latitude: %f \n", location.longitude, location.latitude)
 rate.sleep()
