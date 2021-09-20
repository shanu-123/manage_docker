# Docker Mamagement

import os
from rich.console import Console
import json

console = Console()


def menu():
	print(".................Menu....................")
	console.print("\t1.Status of containers",style="bold blue") 
	console.print("\t2.Download new Image",style="bold blue")
	console.print("\t3.Run container",style="bold blue")
	console.print("\t4.Delete Container",style="bold blue")
	console.print("\t5.Network details of container",style="bold blue")
	console.print("\t6.Modify Network details of contaniner",style="bold blue")
	console.print("\t7.Exit",style="bold blue")

def docker_status():
	print("...............Docker Status..............")
	cmd = os.popen("docker ps -a").read() # Details of containers
	console.print(cmd,style="bold green")

def download_new_img():
	print("...............Download Image................")
	image = input("Enter the image name to search :")
	cmd = f"docker pull {image}" # Pulling image from docker
	down_img = os.popen(cmd).read()
	console.print(down_img,style="bold green")

def run_container():
	print("...............Run Container...............")
	image = input("Enter the image name to search :")
	image_name = input("Enter the name you want to add as image name :")
	cmd = f"docker run --name {image_name} -it {image}" # Running image  
	os.system(cmd)
	

def delete_container():
	print("................Delete Container..................")
	container_name = input("Enter the image name to delete :")
	cmd = f"docker rm {container_name}" # Delete image
	dele_img = os.popen(cmd).read()
	console.print("Deleted successfully",style="bold red")
	

def network_details():
	print("...............Network Details................")
	net_detail = os.popen("docker network inspect bridge").read()
	net = json.loads(net_detail)[0]
	for i in net["Containers"].values():
		print(f'Image Name | {i["Name"]} | Mac Address | {i["MacAddress"]} | IPV4 Address | {i["IPv4Address"]}' ) # gets the details of the active containers
	#console.print(net_detail,style="bold green")

def modify_network():
	print("..............Modifying Network.............")
	mod = os.popen("docker network ls").read()
	print(mod)
	network_name = input("Enter the network name : ")
	container_image = input("Enter the container name to disconnect from network :")
	print("Disconnecting............")
	cmd =f"docker network disconnect {network_name} {container_image}" # Disconnects from a particular network
	dis = os.popen(cmd).read()
	console.print("Disconnected network",style="bold red")
	print("Connecting................")
	cmd1 = f"docker network connect {network_name} {container_image}" # Connects to a particular network
	con = os.popen(cmd1).read()
	console.print("Connected to network",style="bold red")
	
	

while True:
	menu()
	ch = int(input("Enter your choice"))
	if ch == 1:
		docker_status()
	elif ch == 2:
		download_new_img()
	elif ch == 3:
		run_container()
	elif ch == 4:
		delete_container()
	elif ch == 5:
		network_details()
	elif ch == 6:
		modify_network()
	elif ch == 7:
		break
	else:
		console.print("Wrong choice",style="bold red")
