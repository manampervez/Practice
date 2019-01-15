import subprocess


result = subprocess.run(["runas", "/noprofile", "/user:tpaadmin", "netsh", "interface", "set", "interface", "TPALAN", "DISABLED"])
print("FAILED..." if result.returncode else "SUCCESS!")
netifaces.interfaces()


