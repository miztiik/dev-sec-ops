#!/bin/bash
set -e
set -x

# Checking arguments passed
if [[ $# -eq 0 ]] ; || [ -z "$1" ]
  then
    printf "No arguments supplied or empty string arguments"
    printf "Assuming default role as blueUserRole"
    $1="Blue"
fi


account_id=$(aws sts get-caller-identity --query Account --output text)
#ROLE ARN PATTERN->  arn:aws:iam::${account_id}:role/unicornTeamProjectBlueRole"
role_arn_to_assume="arn:aws:iam::${account_id}:role/unicornTeamProjectBlueRole"



s3_role=$(aws sts assume-role \
                    --role-arn "${role_arn_to_assume}" \
                    --role-session-name "S3UploadRoles" --profile blue)

export AWS_ACCESS_KEY_ID=$(echo $s3_role | jq -r .Credentials.AccessKeyId)
export AWS_SECRET_ACCESS_KEY=$(echo $s3_role | jq -r .Credentials.SecretAccessKey)
export AWS_SESSION_TOKEN=$(echo $s3_role | jq -r .Credentials.SessionToken)

printf "Checking Role Identity\n"

if ! aws sts get-caller-identity | grep -q 'S3AccessRole'; then
  echo "No Assumed Role found"
  exit
fi

printf "Assumed Role Successfully.\nProceeding to upload local files"

aws s3 cp awslogo.jpeg s3://sddemos3
aws s3api put-object-tagging --bucket sddemos3 --key "awslogo.jpeg" --tagging 'TagSet=[{Key=org,Value=awstagged}]'

aws s3 cp netflixlogo.jpeg s3://sddemos3
aws s3api put-object-tagging --bucket sddemos3 --key "netflixlogo.jpeg" --tagging 'TagSet=[{Key=org,Value=netflixtagged}]'



# {"S3PutObjectTagging": { "TagSet": [{"Key":"keyOne", "Value":"ValueOne"}] }}