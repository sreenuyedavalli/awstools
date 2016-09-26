import boto.ec2
import sys
import os
# NOTE: if you don't put the key at conn then it will search for
# your profile file, if not /etc/boto.cfg if not your varible 'BOTO_CONFIG=/file/path'

# Following is the prod key: [ Read only ec2 access via the 'Stats' AIM user. ]
# after appending output to your ssh config, can access boxes via "ssh metrics-10.prd"
# Usage ex.. python ec2_sshconfig_generator.py frankthefish > /users/frankthefish/.ssh/config

my_access_key = os.environ.get('AWS_ACCESS_KEY_ID')
my_access_secret_key = os.environ.get ('AWS_SECRET_ACCESS_KEY')

#conn=boto.ec2.connect_to_region('us-east-1')
conn=boto.ec2.connect_to_region('us-east-1',aws_access_key_id=my_access_key , aws_secret_access_key=my_access_secret_key)

reservations = conn.get_all_instances()
for res in reservations:
    for inst in res.instances:
	if inst.private_ip_address != None:
            print "%s \t %s" % ("Host", inst.tags['Name'])
            print "%s  %s" % ("HostName", inst.private_ip_address)
            print "%s" % ("StrictHostKeyChecking no")
            print "%s  %s" % ("Port", "22")
            print "%s %s" % ("User", str(sys.argv[1]))
            print "%s %s%s" % ("IdentityFile", "~/.ssh/", "id_rsa" )
	    print "%s\n" % ("ForwardAgent yes")
            #print "%s" % (inst.tags['Name'])
	else:
	    print "#oops"
