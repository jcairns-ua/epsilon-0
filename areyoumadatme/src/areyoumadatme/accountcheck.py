"""
checking/ addding accounts
accounts.txt:
name,username,email,password
"""

def getaccounts():
    """
    opens accounts.txt, creates dictionary of all acounts
    returns: accounts

    accounts dict of form "username" : [name, email, password]
    """
    acctfile = open("accounts.txt", "r")
    accounts = {}
    for lines in acctfile:
        account = lines.split(",")
        username = account.pop(1)
        accounts[username] = account

    acctfile.close()

    return accounts




def addaccount(accounts, name, email, username, password):
    """
    adds account to dictionary + text file
    cannot contain ','
    username cannot be 'true'
    returns:
        1 : if added account successfully
        0 : if account already exists
       -1 : if invalid name/username/password
    """
    
    #add account if username not already exists
    if ( ("," in name) or ("," in email) or ("," in password) or ("," in username) ):
        return -1
        
    elif (("true"==username) or ("true"==password)):
        return -1
    
    elif ( username in accounts ):
        return 0
    
    else :
        accounts[username] = [name, email, password]
        return 1


def checkaccount(accounts, username, password):
    """
    logs user in if username exists and password matches
    returns: 
        if valid : "true"
        if username doesnt exist : username
        if password invalid : password
    """
    try:
        testpass = accounts[username]
        if (testpass == password):
            return "true"
        else:
            return password
        
    except KeyError:
        return username

