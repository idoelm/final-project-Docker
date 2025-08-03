from flask import Flask
import os
import json
import logging
import printColors

app = Flask(__name__)

def loadUsers():
    try:
        with open("config.json", "r", encoding='utf-8') as file:
            list_name = json.load(file)
            set_list_name = set(list_name)
            return set_list_name
    except FileNotFoundError:
        logging.critical("Error: Config file missing.")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

@app.route("/")
def home():
    logging.info("The user has accessed the path /")
    return printColors.printBlack("Welcome to my system, Please login.")

@app.route("/login")
def login():
    logging.info("The user has accessed the path /login")
    return printColors.printBlack("Please enter your name in the address bar like this: 127.0.0.1/login/yourName")

@app.route("/login/<my_name>")
def userName(my_name):
    if searchName(my_name):
        logging.info("Name " + my_name + " exists in list, access granted")
        return printColors.printGreen("Access Granted.")
    else:    
        logging.warning("Name " + my_name + " does not exists in list, access denied")
        return printColors.printRed("Access Denied.")

@app.route("/addName/<new_name>")
def addName(new_name):
    if searchName(new_name):
        return printColors.printBlack("The username exists in the system.")
    else:
        try:
            with open("config.json", "r", encoding='utf-8') as file:
                list_name = json.load(file)
                list_name.append(new_name)
                with open("config.json", "w", encoding='utf-8') as file:
                    json.dump(list_name, file, indent=4, ensure_ascii=False)
                    logging.info(list_name)
                return printColors.printGreen("Name " + new_name + " Added successfuly")
        except FileNotFoundError:
            logging.critical("Error: Config file missing.")


def searchName(name):
    users = loadUsers()
    if name in users:
        return True
    return False
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)