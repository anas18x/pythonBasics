amount = 2
print(amount)
print(type(amount))
print(id(amount))


# strings are immutable
name = "anas"
print(id(name))
name = "as"
print(id(name))


print(name.capitalize())
reversedName = name[::-1]
print(reversedName)

print(name[1:2])


# ------------------------------

# tuples are immutable
role = ("admin", "user", "superAdmin")
(role_1, role_2, role_3)= role
print(role_1)
print(role_2)
print(role_3)
print(role)


admin_access , user_access = "readWrite" , "read"

#----------------------------------------------------------

#lists(mutable)
roles = ["user","admin"]
print(roles[0])
roles[0] = "user1"
print(roles)

roles.append("superadmin")
print(roles)

roles.remove("user1")
print(roles)

roles.insert(0,"xyz")
print(roles)

#opeartor overloading
print(roles + ["abc"])


data = bytearray(b"hello")
print(data)
