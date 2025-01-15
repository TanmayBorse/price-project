# 🏡 Pune House Price Prediction

This data science project walks through the step-by-step process of building a **real estate price prediction website**. I use **Pune House Prices Dataset** from Kaggle to predict property prices. The project is divided into three main components:

1. **Model Building**: Using **sklearn** and **linear regression**.
2. **Python Flask API**: Serving predictions via an HTTP server.
3. **Frontend**: Built with **HTML/CSS/JavaScript** to accept inputs like home area, bedrooms, etc., and retrieve the predicted price from the Flask API.

The project covers various **data science concepts** such as:
- Data loading and cleaning
- Outlier detection and removal
- Feature engineering
- Dimensionality reduction
- Hyperparameter tuning using GridSearchCV
- K-Fold cross-validation

## 💻 Technologies and Tools

- **Python**
- **Numpy** and **Pandas** for data cleaning
- **Matplotlib** for data visualization
- **Sklearn** for model building
- **Jupyter Notebook**, **VS Code**, and **PyCharm** as IDEs
- **Flask** for the backend server
- **HTML/CSS/JavaScript** for the frontend
- **NGINX** for web server setup
- **AWS EC2** for cloud deployment (Ubuntu)

---

## 📊 Data Science Process

1. **Data Preprocessing**: Handle missing values, outliers, and perform feature engineering.
2. **Model Building**: Train a linear regression model using `sklearn` and evaluate it using cross-validation.
3. **Model Evaluation**: Tune hyperparameters using `GridSearchCV` and check performance with metrics like RMSE and R².
4. **Flask API**: Serve the model as a REST API to make predictions.
5. **Frontend Development**: Build a user-friendly interface to input house features and get predictions.

---

## 🚀 Deployment on AWS EC2

### Step 1: Launch EC2 Instance
- Create an EC2 instance using the AWS Management Console.
- In the security group, add a rule to allow incoming HTTP traffic.

### Step 2: Connect to EC2 Instance
- Connect to the instance using SSH:
   ```bash
   ssh -i "C:\Users\ADMIN\.ssh\pune.pem" ubuntu@ec2-13-233-22-49.ap-south-1.compute.amazonaws.com

### step 3: nginx setup
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

### step 4: Copy all files fron local machine to EC2
- Then I copy all my code to EC2 instance by copying files using winscp. 
- Once I connect to EC2 instance from WinSCP I copy all code files into /home/ubuntu/ folder. The full path of your root folder is now: **/home/ubuntu/HousePrices**
### step 5: Create and Link configuration file.
- After copying code on EC2 server I can point nginx to load property website by default.
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
### step 6: Now install python packages and start flask server
```
python3 /home/ubuntu/HousePrices/server/server.py
```
- Running last command above will prompt that server is running on port 5000.
### step 7:
- Now just load cloud url in browser (for me it was http://ec2-13-233-22-49.ap-south-1.compute.amazonaws.com/) and this will be fully functional website running in production cloud environment


