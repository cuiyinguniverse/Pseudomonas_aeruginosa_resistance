#!/bin/bash

#Using clustalw2 for double sequence alignment

######################process management##################################
start_time=`date +%s`              #Defining the start time of script execution.
[ -e /tmp/fd1 ] || mkfifo /tmp/fd1 #Creating a named pipe.
exec 3<>/tmp/fd1                   #Creating a file descriptor that associates the pipeline file in a readable (<) writable (>) way, and file descriptor 3 has all the features of a named pipeline file.
rm -rf /tmp/fd1                    #The associated file descriptor has all the features of the pipeline file, so the pipeline file can be deleted at this time, and we can leave the file descriptor to use.
for ((i=1;i<=15;i++))
do
        echo >&3                   #"&3" stands for reference file descriptor 3, and this command stands for putting a "token" into the pipe.
done
#######################process management##################################
#######################program##################################
clustalw2=/edisk2/houj21/program/CUDA-clustalW/clustalw-2.1-linux-x86_64-libcppstatic/clustalw2 

for name in gyrA gyrB nfxB mexR
do
    for i in `cat /edisk2/yangh22/yxq_works/protein/complete_genome_level/${name}_mutation.csv` 
    do
        read -u3                               #Representing reading a token from the pipeline.
        {
                    echo 'success_  '/edisk2/yangh22/protein/ncbi_dataset/data/$i/${name}.fasta 
                    $clustalw2 -INFILE=/edisk2/yangh22/protein/ncbi_dataset/data/$i/${name}.fasta -ALIGN -QUIET        #input the fasta format file used for the double sequence alignment
                    echo >&3                   #Representing this time the command is executed to the end, put the token back in the pipeline.
        }&
    done
done
######################Script execution##################################
wait
stop_time=`date +%s`            #Defining the end time of the script run.
echo "TIME:`expr $stop_time - $start_time`"
exec 3<&-                       #Closing the read of the file descriptor.
exec 3>&-                       #closing the write of the file descriptor.
