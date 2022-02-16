#!/bin/python3
import sys, os, time
clear = lambda: os.system('clear')
global id_list, cintainer_list, temp_name, temp_port, image_name, d_port
images_list = [ 'adejonge/helloworld:latest', 'abh1nav/dockerui:latest', 'nginx:latest', 'jenkins']

uesd_names = []
uesd_potrs = []
#--------------------------------
def name_port():
    for i in os.system.__str__("sudo docker container ls -a --format '{{.Names}}'"):
        uesd_names.append(i)
    for i in  os.system.__str__("sudo docker container ls --format '{{.Ports}}' | cut -c 9-12"):
        uesd_potrs.append(i)
#--------------------------------
def container_name():
    clear()
    temp_name = input("Give a name to the container")
    if temp_name in uesd_names:
        temp_name = input("Give a name to the container number {}.\nThe already uesd names are:\n{}\n".format(uesd_names, temp_name))
    else:
        container_port(temp_name)
#---------------------
def container_port(temp_name):
    temp_port = input("Set a port to the container.\n")
    if temp_port in uesd_potrs:
        temp_port = input("Set a name to the container {}.\nThe already uesd names are:\n{}}\n".format(temp_name, uesd_potrs))
#--------------------------------
def images_select():
    cun = 1
    for i in images_list:
        print(str(cun) + " " + i)
        cun  = cun + 1
    f = int(input()) - 1
    y = images_list[f]
    return y
#--------------------------------
#exit fun
def finish():
    clear()
    print("Good bey!")
    time.sleep(1)
    clear()
    exit
#---------------------  
def run():
    os.system(''' 
    sudo docker run -d -p {}:{} --name {} {}
    '''.format(temp_port, d_port, temp_name, image_name))
#---------------------
def continue_fun():
    temp = input('\nPress any key to continue\n')
#--------------
def pu_image(image_name):
    os.system('''
        echo "{}"
        sleep 2
        if [ "$(sudo docker inspect {})" == "[]" ] ; then
            clear
            echo -e "The imgae $image_name is pulling\n"
            sudo docker pull {}
            clear
            mage_main
        else
            clear
            echo "The imgae {0} is exsit"
            sleep 2
            clear
            image_main
        fi
        '''.format(*image_name))
def container_main():
    clear()
    name_port()
    temp = input('Menu:\n1. Run a container \n2. Stop runing containers\n3. See runing containers\n4. Delete a containers.\n9. Back to mein meun\n\n0. Mein menu or Exit.\n')
    clear()
    if temp == "1":
        print(images_list)
        image_name = input('Select docker inage to run\n')
        container_name()
        print(temp_port + temp_name)
    elif temp == "2":
        run()
    elif temp == "3":
        os.system('sudo docker containr stop {}'.format())
    elif temp == "4":
        os.system('sudo docker ps')
    elif temp == "9":
        main()
    elif temp == "0":
        finish()
    else:
        print("1-5 or 0 only!")
        time.sleep(2)
        container_main()
#image_main
def image_main():
    clear()
    temp = input('Image Menu:\n1. Pull a docker image.\n2. To see your images.\n3. Update image\n4. Remove image.\n9. Back to mein meun\n0. Exit.\n')
    clear()
    if temp == "1":
        print('Which docker image do you want to pull?\nSelect by number\n')
        image_name = images_select()
        pu_image(image_name)
        image_main()
    elif temp == "2":
        os.system('sudo docker images -a')
        continue_fun()
        image_main()
    elif temp == "3":
        print('Which docker image do you update to pull?\nSelect by number\n')
        image_name = images_select()
        pu_image(image_name)
        image_main()
    elif temp == "4":
        print('Which docker image do you want to remove?')
        image_name = images_select()
        os.system('sudo docker rmi -f {}'.format(image_name))
        image_main()
    elif temp == "9":
        main()
    elif temp == "0":
        finish()
    else:
        print("1-2 or 0 only!")
        time.sleep(2)
        image_main()
#main menu
def main():
    clear()
    temp = input('Mein menu:\n1. Images menu. \n2. Containers menu.\n0. Exit.\n')  
    clear()
    if temp == "1":
        image_main()
    elif temp == "2":
        container_main()
    elif temp == "0":
        finish()
    else:
        print("1-5 or 0 only!")
        time.sleep(2)
        main() 
main()