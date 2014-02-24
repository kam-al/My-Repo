###########################################################################################################
reservation = conn.run_instances( ... )

# NOTE: this isn't ideal, and assumes you're reserving one instance. Use a for loop, ideally.
instance = reservation.instances[0]

# Check up on its status every so often
status = instance.update()
while status == 'pending':
    time.sleep(10)
    status = instance.update()

if status == 'running':
    instance.add_tag("Name","{{INSERT NAME}}")
else:
    print('Instance status: ' + status)
    return None

# Now that the status is running, it's not yet launched. The only way to tell if it's fully up is to try to SSH in.
if status == "running":
    retry = True
    while retry:
        try:
            # SSH into the box here. I personally use fabric
            retry = False
        except:
            time.sleep(10)

# If we've reached this point, the instance is up and running, and we can SSH and do as we will with it. Or, there never was an instance to begin with.


############################################################################################################

import boto.ec2
from boto.manage.cmdshell import sshclient_from_instance

# Connect to your region of choice
conn = boto.ec2.connect_to_region('us-west-2')

# Find the instance object related to my instanceId
instance = conn.get_all_instances(['i-12345678'])[0]

# Create an SSH client for our instance
#    key_path is the path to the SSH private key associated with instance
#    user_name is the user to login as on the instance (e.g. ubuntu, ec2-user, etc.)
ssh_client = sshclient_from_instance(instance,
                                     key_path='<path to SSH keyfile>',
                                     user_name='ec2-user')
# Run the command. Returns a tuple consisting of:
#    The integer status of the command
#    A string containing the output of the command
#    A string containing the stderr output of the command
status, stdin, stderr = ssh_client.run('ls -al')

############################################################################################################


##For future reference, this is how to start a stopped instance:

instance = conn.get_all_instances(instance_ids=['instance_id'])
print instance[0].instances[0].start()

############################################################################################################
	

#I have used the below to attach a volume to ec2 using boto. I am using ubuntu 12.04.

region_id=boto.ec2.get_region(region,aws_access_key_id=aws_access_key_id, 

aws_secret_access_key=aws_secret_access_key)
    conn = ec2.connection.EC2Connection(region=region_id,aws_access_key_id=aws_access_key_id, 
    
aws_secret_access_key=aws_secret_access_key)
    vol = conn.create_volume(gigs,placement)
    vol.attach(intsance_id, '/dev/sdh')
############################################################################################################

#!/usr/bin/env python
from boto_manage import BotoManageCommand

class ListServers(BotoManageCommand):
    """
List all currently registered servers.
"""
    def main(self):
        BotoManageCommand.main(self)
        from boto.manage.server import Server
        print '\tName\tDescription\tID\tDNS Name'
        for server in Server.all():
            print '\t%s\t%s\t%s\t%s' % (server.name, server.description,
                                        server.instance_id, server.hostname)

if __name__ == "__main__":
    command = ListServers()
    command.main()

###########################################################################################################

# This file contains the build configuration

#
# Mandatory elements
# (Elements with no default values)
#

# EC2 Region to work in.
EC2_REGION='eu-west-1'

# AWS Access key
AWS_ACCESS_KEY_ID='<My AWS Access KEY>'

# AWS Secret key
AWS_SECRET_ACCESS_KEY='<My AWS Secret KEY>'

# AWS Account ID (Necessary to upload an AMI to S3)
AWS_ACCOUNT_ID='My AWS Account ID'

# Location of the EC2 Certificate file (used to sign the S3 AMI bundle).
EC2_CERT_FILE='cert.pem'

# Location of the EC2 Private key file (used to sign the S3 AMI bundle).
EC2_PK_FILE='pk.pem'

# Bucket to upload S3 Image
S3_AMI_BUCKET = 'openanceamis'

#
# Optional elements
#

# Force use of a particular instance for the build.
# By default, the fab file will use the first running
# instance.
#EC2_BUILD_INSTANCE='i-64f57d2d'

# Architecture. By default, will use the architecture
# of the build instance. If there is no build instance
# available, will default to 'x86_64'
#ARCH='x86_64'

# If set to True, will use the first build snapshot
# as the base for the build volume in create_and_attach_volume
#USE_SNAPSHOT=False

########################################################################################################
    
