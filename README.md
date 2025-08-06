# GoldSrc-ResGrab

⚒️ **ResGrab** is a tool for extracting necessary resources from a map using ResGen.

## 📋 Description

ResGrab is a Python tool that automates the process of extracting resources (models, textures, sounds) from GoldSrc `.bsp` files. It uses `resgen.exe` to generate `.res` files and then copies all resources to an organized directory.

## 🚀 Features

- ✅ **Automatic extraction** of resources from `.bsp` maps
- ✅ **Automatic generation** of `.res` files using `resgen.exe`
- ✅ **File organization** in structured directories
- ✅ **Robust error handling** with detailed feedback
- ✅ **AMX Mod X naming** for developers familiar with plugins
- ✅ **Object-oriented programming** for better maintenance
- ✅ **Type hints** for better code documentation

## 📦 Requirements

### Required Software:
- **Python 3.6+**
- **resgen.exe** (GoldSrc tool for generating .res files)
- **Git** (for cloning the repository)

### File Structure:
```
GoldSrc-ResGrab/
├── resgrab.py          # Main script
├── README.md           # This file
└── requirements.txt    # Dependencies (if any)
```

## 🛠️ Installation

### 1. Clone the repository:
```bash
git clone https://github.com/GoodbayKOD/GoldSrc-ResGrab.git
cd GoldSrc-ResGrab
```

### 2. Verify Python:
```bash
python --version
# Should show Python 3.6 or higher
```

### 3. Get resgen.exe: (https://gamebanana.com/tools/4777)
- Download `resgen.exe` from GoldSrc development tools
- Place it in an accessible location (e.g., `C:\tools\resgen.exe`)

## 📖 Usage Guide

### Step 1: Prepare the files
Make sure you have:
- The `.bsp` file of the map you want to extract
- `resgen.exe` in a known location
- An output directory to save the resources

### Step 2: Run the script
```bash
python resgrab.py
```

### Step 3: Follow the interactive instructions

The script will ask for the following information:

#### 3.1 Output directory
```
Output directory (Enter to use current directory): 
```
- **Press Enter** to use the current directory
- **Or type** a specific path (e.g., `C:\output\maps`)

#### 3.2 .bsp file path
```
Full path to the .bsp file (e.g. cstrike/maps/de_dust2.bsp): 
```
- **Example**: `C:\cstrike\maps\de_dust2.bsp`
- **Example**: `C:\resources\cstrike\maps\zs_decoy.bsp`

#### 3.3 resgen.exe path (if needed)
```
⚠️  de_dust2.res not found in C:\cstrike\maps
Please provide the path to resgen.exe
Path to resgen.exe: 
```
- **Example**: `C:\tools\resgen.exe`
- **Example**: `C:\cstrike\bin\resgen.exe`

### Step 4: Wait for extraction

The script will show progress:
```
🛠️  Running resgen...
📦 45 resources detected.
✅ Copied: models/player/terror/terror.mdl
✅ Copied: models/player/urban/urban.mdl
❌ NOT FOUND: models/missing_model.mdl
📁 Creating output directory: C:\output\maps\de_dust2
```

### Step 5: Review results

Files will be organized like this:
```
output_directory/
└── map_name/
    ├── models/
    │   ├── player/
    │   └── props/
    ├── materials/
    ├── sound/
    ├── missing.txt    # List of files not found
    └── ... (other resources)
```

## 📊 Example Output

```
=== Goldsrc ResGrab ===

Output directory (Enter to use current directory): 
Full path to the .bsp file (e.g. cstrike/maps/de_dust2.bsp): C:\cstrike\maps\de_dust2.bsp
⚠️  de_dust2.res not found in C:\cstrike\maps
Please provide the path to resgen.exe
Path to resgen.exe: C:\tools\resgen.exe
🛠️  Running resgen...
✅ .res file found.
📦 45 resources detected.
📁 Creating output directory: C:\Scripts\other\Mods\Tower Defense\de_dust2
✅ Copied: models/player/terror/terror.mdl
✅ Copied: models/player/urban/urban.mdl
✅ Copied: materials/models/player/terror/terror.vmt
⚠️  2 files not found. Saved in missing.txt

🎉 Process completed!
📊 Summary:
   • Total resources: 45
   • Successfully copied: 43
   • Missing files: 2
   • Output directory: C:\Scripts\other\Mods\Tower Defense\de_dust2
```

## ⚠️ Troubleshooting

### Error: "resgen.exe not found"
- Verify that the path to `resgen.exe` is correct
- Make sure the file exists and is executable

### Error: "The .bsp file does not exist"
- Verify that the path to the `.bsp` file is correct
- Make sure the file exists

### Error: "No resources found in the .res file"
- The `.res` file is empty or corrupted
- Try regenerating the `.res` file with `resgen.exe`

### Error: "Unexpected error: [WinError 193]"
- The `resgen.exe` file is not a valid executable
- Download a correct version of `resgen.exe`

## 🔧 Technical Features

### AMX Mod X Naming
The script uses naming conventions similar to AMX Mod X plugins:
- `sz` = String (text strings)
- `g_` = Global (global variables)
- `i` = Integer (integer numbers)
- `f` = Float (decimal numbers)

### Code Structure
- **ResourceExtractor class**: Handles all extraction logic
- **Modular methods**: Each function has a specific responsibility
- **Type hints**: Improves documentation and maintenance
- **Error handling**: Try/catch for critical operations

## 📝 License

This project is under the MIT license. See the LICENSE file for more details.

## 🤝 Contributing

Contributions are welcome. Please:

1. Fork the repository
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

If you have problems or questions:
- Open an issue on GitHub
- Check the "Troubleshooting" section
- Verify that you have all requirements installed

---
