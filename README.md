# notebook-genelab-client
GenePattern notebook client to connect to the NASA GeneLab system


#
# To start a genepattern-notebook docker container
#

docker run  -p 8888:8888 -v /Users/liefeld/GenePattern/gp_dev/GeneLab:/home/jovyan/work  -t genepattern/genepattern-notebook

# a bit of container setup
docker exec --user root -it <CONTAINER_ID>  chmod -R 777 /home/jovyan/.jupyter
docker exec --user root -it <CONTAINER_ID>  chmod -R 777 /home/jovyan/.local


# IN THE NOTEBOOK INSTALL THE OZZIE GS CLIENT
!pip install python-genomespaceclient

#
# to work on the extension
#
cd /Users/liefeld/GenePattern/gp_dev/GeneLab/myExtension
cd myExtension

# uninstall and reinstall the extension if necessary
# make sure to use --user and --symlink so that it uses the files here and does not copy and cache them
#
# do this inside the docker container or in a terminal launched from the jupyter
#
jupyter nbextension uninstall GSGeneLab
jupyter nbextension install GSGeneLab --py --user --symlink
jupyter nbextension enable GSGeneLab --user --py 
jupyter serverextension enable GSGeneLab --user



