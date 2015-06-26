#!/usr/bin/python

#executing this command:
#./config add floating-ip-pool user1-net-pool --network user1-net
#based on the user and data center nummber
import sys
import os
import getopt

def main(argv):
	try:                                
		opts, args = getopt.getopt(argv, "hu:d:", ["help", "user=","datacenter="])
	except getopt.GetoptError:                                
		sys.exit(2)
	for opt, arg in opts:       
		if opt in ("-h", "--help"):                         
			sys.exit()                                   
		elif opt in ("-u", "--user"): 
			username = arg
		elif opt in ("-d", "--datacenter"):
			data_num = arg
		#elif opt in ("-s", "--start_user")
		#	start_user = arg
	
	#subnet = "10.1." + str(data_num) +"."+str(((int(username))-int(start_user))*8)+"/29"
	
	command = "/root/code_specific/config" + " " + "--username " + username + " --password " + username + " --tenant "+ username + " --api-server 127.0.0.1 " + "add floating-ip-pool public-" + username + "-net-pool --network public-" + username + "-net" 
	#print command	
	os.system(command)
if __name__ == "__main__":
    main(sys.argv[1:])
