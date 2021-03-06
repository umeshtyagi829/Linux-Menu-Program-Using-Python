from subprocess import getstatusoutput as gso
import datetime
import os

def time():

  t  = str(datetime.datetime.now())    
  current_time = t.split(' ')[1][:5]
  print(current_time , end = '  ')

def minikube_setup():
  repo_name = '/etc/yum.repos.d/confi.repo'
  baseurl_path = 'baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64'

  status = gso('systemctl stop firewalld')
  status = gso('setenforce 0')

  #configuring yum repos
  status = gso(f'touch {repo_name}')

  status = gso(f'echo "[path1]" >> {repo_name}')
  status = gso(f'echo "baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/" >> {repo_name}')
  status = gso(f'echo "gpgcheck=0" >> {repo_name}')

  status = gso(f'echo "[path2]" >> {repo_name}')
  status = gso(f'echo "{baseurl_path}/AppStream" >> {repo_name}')
  status = gso(f'echo "gpgcheck=0" >> {repo_name}')

  status = gso(f'echo "[path3]" >> {repo_name}')
  status = gso(f'echo "{baseurl_path}/BaseOS" >> {repo_name}')
  status = gso(f'echo "gpgcheck=0" >> {repo_name}')

  time()
  print('yum repos configured!' if status[0]==0 else 'failed to configure yum repos!')
  if status[0]!=0 : exit()

#installing docker community edition
  status = gso('yum install docker-ce --nobest -y')

  time()
  print('docker-ce installed successfully' if status[0]==0 else 'failed to install docker-ce')
  if status[0]!=0 : exit()
  status = gso('yum install conntrack-tools -y')

  '''
  minikube installation

  minikube is local Kubernetes, focusing on making it easy to learn and
  develop for Kubernetes. All you need is Docker.
  minimum requirements -

  2 CPUs or more
  2 2GB of free memory
  20GB of free disk space
  Internet connection
  Docker

  '''

#x86 binary download
  status = gso('curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64')

  status = gso('sudo install minikube-linux-amd64 /usr/local/bin/minikube')

  time()
  print('minikube-linux-amd64 successfully installed' if status[0] == 0 else 'failed to install')
  if status[0]!=0 : exit()

  '''
the none driver allows advanced minikube users to skip VM creation, allowing minikube to be run on a user-supplied VM
  '''
  status = gso('minikube config set driver none')

  status = gso('minikube start --driver=none --kubernetes-version=v1.20.0 --memory=1800mb ')

  time()
  print('minikube started' if status[0]==0 else 'failed to start minikube')
  if status[0]!=0 : exit()

  '''
kubectl installation

The Kubernetes command line tool, kubectl, allows you to run commands against
Kubernetes clusters. You can use kubectl to deploy applications, inspect and
manage cluster resources, and view logs.

  '''

#downloading version v1.20.0
  status = gso('curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.20.0/bin/linux/amd64/kubectl')

#make the kubectl binary executable
  status = gso('chmod +x ./kubectl')

#move the binary in to your PATH
  status = gso('sudo mv ./kubectl /usr/local/bin/kubectl')

  time()
  print('kubectl installed successfully' if status[0]==0 else 'failed to install kubectl')

  print('enviornment ready' if status[0]==0 else 'failed to build the enviornment')




# K8s Main Menu
def k8s_menu():
	while True:
		os.system("clear")
		os.system("tput setaf 1")
		print("\t\t   ----------------------------------")
		print("\t\t   | Welcome to K8S Assistant !! |")
		print("\t\t   ----------------------------------")
		os.system("tput setaf 7")

		os.system("tput setaf 2")
		print("""
		  Press 1 : To Configure Kubernates Cluster
		  Press 2 : To Return to Previous Menu
		""")
		
		print()
		os.system("tput setaf 3")
		ch = input("\t\t  Enter your Choice : ")
		os.system("tput setaf 7")

		if int(ch) == 1:
			minikube_setup()

		elif int(ch) == 2:
			break

		else:
			print("Please Select Correct Choice")
			input()













