#centos image which sleeps by default for 5 sec or sleeps according to the given number in the docker run command
# 1-base img
FROM centos

# 2-steps to setup environment

# 3-container starting command

#appand
ENTRYPOINT ["sleep"]

#overwrite
CMD ["5"]
