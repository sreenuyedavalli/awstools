#!/bin/bash
#Author Sreenu Yedavalli
set -e 
set -x 

HOSTS=$(aws ec2 describe-instances --query 'Reservations[*].Instances[*].[Placement.AvailabilityZone, State.Name, InstanceId]' --output text | grep us-east-1 | awk '{print $3}')

echo ${HOSTS[*]}

function stop_hosts() {
	aws ec2 stop-instances --instance-ids ${HOSTS[*]}
	}

function start_hosts() {
	aws ec2 start-instances --instance-ids ${HOSTS[*]}
	}

if  [ $1 == "start" ] 
then
	start_hosts
	echo Starting Hosts
elif [ $1 == "stop" ]
then
	stop_hosts
	echo Stopping Hosts
else
	echo ERROR: Not running
fi

