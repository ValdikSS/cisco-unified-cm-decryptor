# Cisco Unified Communication Manager passwords decryptor

This utility decrypts encrypted passwords found in Cisco Unified CM export files, like `appuser.csv`, `enduser.csv` and `ldapauth.csv`.  
It works only on "unencrypted" Cisco Unified CM installations, where hard-coded encryption key is used for exported files.

### How to use

Download binary builds for Windows and Linux from [Releases page](https://github.com/ValdikSS/cisco-unified-cm-decryptor/releases)

### The key

Hard-coded key has been found in `CCMEncryption.jar` and `CCMEncryptionTest` Cisco Unified CM files.
