acl_number = int(input("Número de ACL: "))
if 1 <= acl_number <= 99:
    print("ACL Estándar")
elif 100 <= acl_number <= 199:
    print("ACL Extendida")
else:
    print("Número no corresponde a una ACL")
