#!/usr/bin/python3

from basemodel import BaseModel
from user import User

user1 = BaseModel()



# dict_rep = user1.to_dict()
# print(dict_rep)

str_rep = user1.__str__()
print(str_rep)
