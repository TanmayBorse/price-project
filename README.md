# Pune House Price Prediction

This data science project series walks through step by step process of how to build a real estate price prediction website. We will first build a model using sklearn and linear regression using Pune House prices dataset from kaggle.com. Second step would be to write a python flask server that uses the saved model to serve http requests. Third component is the website built in html, css and javascript that allows user to enter home square ft area, bedrooms etc and it will call python flask server to retrieve the predicted price. During model building we will cover almost all data science concepts such as data load and cleaning, outlier detection and removal, feature engineering, dimensionality reduction, gridsearchcv for hyperparameter tunning, k fold cross validation etc. Technology and tools wise this project covers,

1. Python.
2. Numpy and Pandas for data cleaning.
3. Matplotlib for data visualization.
4. Sklearn for model building.
5. Jupyter notebook, visual studio code and pycharm as IDE.
6. Python flask for http server.
7. HTML/CSS/Javascript for UI.
8. Testing site on NGINX (on windows).
9. Deployment of Project on AWS cloud EC2 (ubuntu).

# Deploy this app to cloud (AWS EC2)

1. Create EC2 instance using amazon console, also in security group add a rule to allow HTTP incoming traffic
2. Now connect to your instance using a command like this,
```
ssh -i "C:\Users\ADMIN\.ssh\pune.pem" ubuntu@ec2-13-233-22-49.ap-south-1.compute.amazonaws.com
```
3. nginx setup
   1. Install nginx on EC2 instance using these commands,
   ```
   sudo apt-get update
   sudo apt-get install nginx
   ```
   2. Above will install nginx as well as run it. Check status of nginx using
   ```
   sudo service nginx status
   ```
   3. Now when you load cloud url (ec2-13-233-22-49.ap-south-1.compute.amazonaws.com) in browser you will see a message saying "welcome to nginx" This means your nginx is setup and running.

4. Then I copy all my code to EC2 instance by copying files using winscp.
5. Once I connect to EC2 instance from WinSCP I copy all code files into /home/ubuntu/ folder. The full path of your root folder is now: **/home/ubuntu/HousePrices**
6.  After copying code on EC2 server now I can point nginx to load property website by default.
    1. Create this file /etc/nginx/sites-available/php.conf. The file content looks like this,
    ```
    server {
	    listen 80;
            server_name php;
            root /home/ubuntu/HousePrices/client;
            index app.html;
            location /api/ {
                 rewrite ^/api(.*) $1 break;
                 proxy_pass http://127.0.0.1:5000;
            }
    }
    ```
    2. Create symlink for this file in /etc/nginx/sites-enabled by running this command,
    ```
    sudo ln -v -s /etc/nginx/sites-available/php.conf
    ```
    3. Remove symlink for default file in /etc/nginx/sites-enabled directory,
    ```
    sudo unlink default
    ```
    4. Restart nginx,
    ```
    sudo service nginx restart
    ```
7. Now install python packages and start flask server
```
python3 /home/ubuntu/HousePrices/server/server.py
```
Running last command above will prompt that server is running on port 5000.
8. Now just load cloud url in browser (for me it was http://ec2-13-233-22-49.ap-south-1.compute.amazonaws.com/) and this will be fully functional website running in production cloud environment


