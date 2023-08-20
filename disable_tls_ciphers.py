import _winreg as winreg

# Registry paths for SSL/TLS settings
protocols_path = r"SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols"
ciphers_path = r"SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Ciphers"

# List of protocols to disable
disabled_protocols = ["SSL 2.0", "SSL 3.0", "TLS 1.0", "TLS 1.1"]

# List of insecure cipher suites to disable
disabled_ciphers = ["3DES"]

def set_registry_value(path, name, value, value_type=winreg.REG_DWORD):
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, name, 0, value_type, value)

def disable_protocols():
    for protocol in disabled_protocols:
        set_registry_value(protocols_path + "\\" + protocol, "Enabled", 0)

def disable_ciphers():
    for cipher in disabled_ciphers:
        set_registry_value(ciphers_path + "\\" + cipher, "Enabled", 0)

if __name__ == "__main__":
    disable_protocols()
    disable_ciphers()
    print("Vulnerable protocols and cipher suites disabled.")
