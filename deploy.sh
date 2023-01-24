ssh -tt ubuntu@18.135.103.40 << EOF
aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 644435390668.dkr.ecr.eu-west-2.amazonaws.com
docker pull 644435390668.dkr.ecr.eu-west-2.amazonaws.com/shamir-repo:1.1.$1
exit
EOF