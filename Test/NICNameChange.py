import subprocess
subprocess.run(['netsh', 'interface', 'show', 'interface'])
change_name = input("Enter the Interface name:")
new_name = 'newname="{}"'.format(change_name)  # new_name = f'newname="{change_name}"'
subprocess.run(['netsh', 'interface', 'set', 'interface', 'name="Wi-Fi"', new_name])
subprocess.run(['netsh', 'interface', 'show', 'interface'])