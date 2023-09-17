import csv
import os

user_fields = [
    'User ID', 'Name', 'Class', 'Stream', 'Email', 'Password', 'Role'
]
user_database = 'user.csv'
mark_fields = [
    "ID", "User ID", "Name", "Class", "Stream", "Exam", "Mark 1", "Mark 2",
    "Mark 3", "Mark 4", "Mark 5", "Total", "Average"
]
mark_database = 'mark.csv'


def add_user(l):
    if os.path.isfile(user_database):
        flag = 0
        with open(user_database, "r", newline="") as f:
            obj = csv.reader(f)
            for row in obj:
                if row[0] == l[0]:
                    flag = 1
        if flag == 0:
            with open(user_database, "a", newline="") as f:
                obj = csv.writer(f)
                obj.writerow(l)
            return 1
        else:
            return 0
    else:
        with open(user_database, "w", newline="") as f:
            obj = csv.writer(f)
            obj.writerow(user_fields)
            obj.writerow(l)
        return 1


def checkUser(u, p):
    flag = 0
    with open(user_database, "r", newline="") as f:
        obj = csv.reader(f)
        for row in obj:
            if row[0] == u and row[5] == p:
                l = row
                flag = 1
                break
    if flag == 0:
        return 0
    else:
        return l


def searchStud(c, s):
    flag = 0
    with open(user_database, "r", newline="") as f:
        obj = csv.reader(f)
        l = []
        for row in obj:
            if row[2] == c and row[3] == s and row[6] == "Student":
                l.append([row[0], row[1]])
                flag = 1
    if flag == 0:
        return 0
    else:
        return l


def getTeacher(c, s):
    flag = 0
    with open(user_database, "r", newline="") as f:
        obj = csv.reader(f)
        for row in obj:
            if row[2] == c and row[3] == s and row[6] == "Teacher":
                l = [row[1], row[4]]
                flag = 1
    if flag == 0:
        return 0
    else:
        return l


def addMark(l):
    if os.path.isfile(mark_database):
        id1 = 0
        with open(mark_database, "r", newline="") as f:
            obj = csv.reader(f)
            for row in obj:
                id1 = row[0]
        with open(mark_database, "a", newline="") as f:
            l.insert(0, int(id1) + 1)
            obj = csv.writer(f)
            obj.writerow(l)
    else:
        with open(mark_database, "w", newline="") as f:
            l.insert(0, 1)
            obj = csv.writer(f)
            obj.writerow(mark_fields)
            obj.writerow(l)


def searchMark(id, exm):
    flag = 0
    with open(mark_database, "r", newline="") as f:
        obj = csv.reader(f)
        for row in obj:
            if row[1] == id and row[5] == exm:
                l = row
                flag = 1
                break
    if flag == 0:
        return 0
    else:
        return l


def searchUser(id):
    flag = 0
    with open(user_database, "r", newline="") as f:
        obj = csv.reader(f)
        for row in obj:
            if row[0] == id:
                l = row
                flag = 1
                break
    if flag == 0:
        return 0
    else:
        return l


def updateUser(l):
    lst = []
    with open(user_database, "r", newline="") as f:
        obj = csv.reader(f)
        for row in obj:
            if row[0] == l[0]:
                lst.append(l)
            else:
                lst.append(row)
    with open(user_database, "w", newline="") as f:
        obj = csv.writer(f)
        obj.writerows(lst)


def deleteUser(uid):
    flag = 0
    lst = []
    with open(user_database, "r", newline="") as f:
        obj = csv.reader(f)
        for row in obj:
            if row[0] != uid:
                lst.append(row)
            else:
                flag = 1
    if flag == 1:
        with open(user_database, "w", newline="") as f:
            obj = csv.writer(f)
            obj.writerows(lst)


def updateMark(mid, l):
    lst = []
    with open(mark_database, "r", newline="") as f:
        obj = csv.reader(f)
        for row in obj:
            if row[0] == mid:
                l.insert(0, mid)
                lst.append(l)
            else:
                lst.append(row)
    with open(mark_database, "w", newline="") as f:
        obj = csv.writer(f)
        obj.writerows(lst)


"""
def view_stud():
    with open(user_database, "r", newline="") as f:
        obj = csv.reader(f)
        l = []
        for row in obj:
            l.append(row)
        print(l)
"""
