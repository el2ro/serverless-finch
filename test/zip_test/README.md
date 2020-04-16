## Zip path upload

time sls client deploy
real 0m51,253s
user 0m5,960s
sys 0m0,475s

time sls deploy
real 0m30,972s
user 0m8,323s
sys 0m0,735s

time sls invoke --function hello
real 0m57,806s
user 0m1,204s
sys 0m0,053s

## Original upload

time sls client deploy
real 5m17,486s
user 0m9,336s
sys 0m0,778s

### File amount

cd client/dist
du -sh
174M

Compressed archive.zip size was ~53M
File amount roughly 503 files

