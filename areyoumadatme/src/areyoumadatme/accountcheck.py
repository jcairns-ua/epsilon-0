"""
checking/ addding accounts
accounts.txt:
name,username,email,password
"""

def getaccounts():
    """
    opens accounts.txt, creates dictionary of all acounts
    returns: none

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
        0 : if account add failed
    """
    try:
        #add account if username not already exists
        accounts[username] = [name, email, password]


    except KeyError:
        #if in dictionary already
        pass

def checkaccount(username, password):
    """
    logs user in if username exists and password matches
    returns: 
        if valid : "true"
        if username doesnt exist : username
        if password invalid : "false"
    """
    pass

