# Preguntar al usuario por la VLAN nativa y las VLANs configuradas en cada switch
print("Por favor, ingrese la información de VLAN para el switch1:")
native_vlan_switch1 = int(input("VLAN nativa del switch1: "))
vlans_switch1 = list(map(int, input("VLANs configuradas en el switch1 (separadas por comas, ej: 10,20,30): ").split(',')))

print("Por favor, ingrese la información de VLAN para el switch2:")
native_vlan_switch2 = int(input("VLAN nativa del switch2: "))
vlans_switch2 = list(map(int, input("VLANs configuradas en el switch2 (separadas por comas, ej: 40,50,60): ").split(',')))

# Definir las VLANs nativas y configuradas esperadas para los switches
expected_native_vlan_switch1 = 99
expected_vlans_switch1 = [10, 20, 30]
expected_native_vlan_switch2 = 200
expected_vlans_switch2 = [40, 50, 60]

# Comparar las VLANs ingresadas con las esperadas para el switch1
if native_vlan_switch1 == expected_native_vlan_switch1:
    print("Switch1: La VLAN nativa ingresada cumple con el requerimiento.")
else:
    print("Switch1: La VLAN nativa ingresada NO cumple con el requerimiento.")

if set(vlans_switch1) == set(expected_vlans_switch1):
    print("Switch1: Las VLANs configuradas cumplen con el requerimiento.")
else:
    print("Switch1: Las VLANs configuradas NO cumplen con el requerimiento.")

# Comparar las VLANs ingresadas con las esperadas para el switch2
if native_vlan_switch2 == expected_native_vlan_switch2:
    print("Switch2: La VLAN nativa ingresada cumple con el requerimiento.")
else:
    print("Switch2: La VLAN nativa ingresada NO cumple con el requerimiento.")

if set(vlans_switch2) == set(expected_vlans_switch2):
    print("Switch2: Las VLANs configuradas cumplen con el requerimiento.")
else:
    print("Switch2: Las VLANs configuradas NO cumplen con el requerimiento.")
