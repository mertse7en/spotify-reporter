# Spotify Weekly Report

# Prerequisites 

- SQLİTE --> https://www.servermania.com/kb/articles/install-sqlite/
- DOCKER -->
- MAIL 




## Docker

docker build --tag spotify-reporter:latest .

```
docker create --name spotify-daily-history spotify-reporter:latest --option daily_history_push 
docker create --name spotify-weekly-report spotify-reporter:latest --option weekly_report 
```


docker build --tag spotify-reporter:latest  .
    
```
docker run -e REPORT_NAME='daily_history_push' spotify-reporter

docker run -e REPORT_NAME='weekly_report' spotify-reporter


```