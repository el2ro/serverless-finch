# serverless-finch test

This is just a quick zipLambda test fork related to [**issues/99**](https://github.com/fernando-mc/serverless-finch/issues/99)

## ZIP Test pre-requisites

```
cd test/zip_test
npm install
```

**Update** profile: to match yours environment specified in `serverless.yml`.

**Add data** to client/dist

## Usage

**First** run `sls client deploy`, to create archive.zip and upload it to s3 bucket
**Second** run `sls deploy`, to deploy lambda function to be run from invoke
**3rd** run `sls invoke -f hello`, to unpack files from s3 bucket back to s3 bucket

## Configure

Configure zipLambda on / off from the `serverless.yml`

```
custom:
  client:
    bucketName: flinch-s3-test-bucket # (see Configuration Parameters below)
    zipLambda: true # or true if uploading archive.zip
```
