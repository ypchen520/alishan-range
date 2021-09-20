# Install TF on MAC M1 Chip

## [stack overflow](https://stackoverflow.com/questions/65383338/zsh-illegal-hardware-instruction-python-when-installing-tensorflow-on-macbook#)

* [download and install tensorflow](https://github.com/apple/tensorflow_macos/releases/tag/v0.1alpha1)
  * Mac-optimized TensorFlow and TensorFlow Addons
* zip: tensorflow_macos
  * arm64
  * x86_64
  * install_venv.sh
  * In this folder run
    * **destination venv should be created**
    * ```arch -arm64 bash install_venv.sh --python=[PATH_TO_THE_PYTHON_THAT_WAS_USED_TO_CREATE_THE_VENV] [PATH_TO_VENV]```
* Python3 is shipped with 2 architectures in M1
  * file $(which python3)
    * /usr/bin/python3: Mach-O universal binary with 2 architectures: [x86_64:Mach-O 64-bit executable x86_64] [arm64e:Mach-O 64-bit executable arm64e]
    * /usr/bin/python3 (for architecture x86_64): Mach-O 64-bit executable x86_64
    * /usr/bin/python3 (for architecture arm64e): Mach-O 64-bit executable arm64e
    