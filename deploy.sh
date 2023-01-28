ssh -tt ubuntu@18.134.229.9 << EOF
aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 644435390668.dkr.ecr.eu-west-2.amazonaws.com
docker pull 644435390668.dkr.ecr.eu-west-2.amazonaws.com/shamir-repo:1.1.$1
# replace image of app service to the new image
exit
EOF