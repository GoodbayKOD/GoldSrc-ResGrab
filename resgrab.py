#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Goldsrc ResGrab by Goodbay - Extract resources from .bsp files
Extract all resources (models, textures, sounds) from a .bsp file
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple, Optional

class ResourceExtractor:
    """Class to extract resources from .bsp files"""
    
    def __init__(self):
        # Global variables (g_)
        self.g_szOutputDir: str = ""
        self.g_szBspPath: str = ""
        self.g_szMapName: str = ""
        self.g_szResourceList: List[str] = []
        self.g_szMissingFiles: List[str] = []
        
    def GetOutputDirectory(self) -> str:
        """Get output directory from user"""
        szOutputDir = input("Output directory (Enter to use current directory): ").strip()
        
        if not szOutputDir:
            szOutputDir = os.getcwd()
            
        return os.path.abspath(szOutputDir)
    
    def GetBspFilePath(self) -> Optional[str]:
        """Get .bsp file path from user"""
        szBspPath = input("Full path to the .bsp file (e.g. cstrike/maps/de_dust2.bsp): ").strip()
        
        if not os.path.isfile(szBspPath):
            print("❌ The .bsp file does not exist.")
            return None
            
        return os.path.abspath(szBspPath)
    
    def ExtractMapInfo(self, szBspPath: str) -> Tuple[str, str, str]:
        """Extract information from the .bsp file"""
        szMapDir, szMapFilename = os.path.split(szBspPath)
        szMapName = os.path.splitext(szMapFilename)[0]
        szResPath = os.path.join(szMapDir, f"{szMapName}.res")
        
        return szMapDir, szMapName, szResPath
    
    def GetResgenPath(self) -> Optional[str]:
        """Get resgen.exe path from user"""
        print("Please provide the path to resgen.exe")
        szResgenPath = input("Path to resgen.exe: ").strip()
        
        if not os.path.isfile(szResgenPath):
            print("❌ resgen.exe not found at the specified path.")
            return None
            
        return os.path.abspath(szResgenPath)
    
    def GenerateResFile(self, szMapDir: str, szBspPath: str, szResPath: str) -> bool:
        """Generate .res file using resgen.exe"""
        print(f"⚠️  {os.path.basename(szResPath)} not found in {szMapDir}")
        
        szResgenPath = self.GetResgenPath()
        if not szResgenPath:
            return False
            
        print("🛠️  Running resgen...")
        try:
            # Use the full path to resgen.exe and the .bsp file
            subprocess.run([szResgenPath, szBspPath], cwd=szMapDir, check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running resgen.exe: {e}")
            return False
        except FileNotFoundError:
            print("❌ resgen.exe not found or not executable")
            return False
            
        if not os.path.isfile(szResPath):
            print("❌ .res file not generated. Something went wrong.")
            return False
            
        return True
    
    def ReadResourceFile(self, szResPath: str) -> List[str]:
        """Read and process .res file"""
        try:
            with open(szResPath, 'r', encoding='utf-8', errors='ignore') as fResFile:
                szResourceLines = fResFile.readlines()
        except FileNotFoundError:
            print(f"❌ Could not read {szResPath}")
            return []
        
        # Process resources
        szResourceList = []
        for szLine in szResourceLines:
            szLine = szLine.strip()
            if not szLine or szLine.startswith("//"):
                continue
            szResourceList.append(szLine.replace("\\", "/"))  # Normalize separators
            
        return szResourceList
    
    def CopyResources(self, szResourceList: List[str], szBspPath: str, szOutputDir: str) -> List[str]:
        """Copy resources to output directory"""
        szMissingFiles = []
        szMapOutputDir = os.path.join(szOutputDir, self.g_szMapName)
        
        print(f"📁 Creating output directory: {szMapOutputDir}")
        
        for szResourcePath in szResourceList:
            # Build source path
            szSourcePath = os.path.join(os.path.dirname(szBspPath), "..", szResourcePath)
            szSourcePath = os.path.abspath(szSourcePath)
            
            # Build destination path
            szDestPath = os.path.join(szMapOutputDir, szResourcePath)
            szDestDir = os.path.dirname(szDestPath)
            
            # Create destination directory if it doesn't exist
            if not os.path.exists(szDestDir):
                os.makedirs(szDestDir, exist_ok=True)
            
            if os.path.isfile(szSourcePath):
                try:
                    shutil.copy2(szSourcePath, szDestPath)
                    print(f"✅ Copied: {szResourcePath}")
                except (shutil.Error, OSError) as e:
                    print(f"❌ Error copying {szResourcePath}: {e}")
                    szMissingFiles.append(szResourcePath)
            else:
                print(f"❌ NOT FOUND: {szResourcePath}")
                szMissingFiles.append(szResourcePath)
                
        return szMissingFiles
    
    def SaveMissingFiles(self, szMissingFiles: List[str], szOutputDir: str):
        """Save list of missing files"""
        if not szMissingFiles:
            return
            
        szMapOutputDir = os.path.join(szOutputDir, self.g_szMapName)
        szMissingFilePath = os.path.join(szMapOutputDir, "missing.txt")
        
        try:
            with open(szMissingFilePath, 'w', encoding='utf-8') as fMissingFile:
                for szMissingItem in szMissingFiles:
                    fMissingFile.write(szMissingItem + "\n")
            print(f"⚠️  {len(szMissingFiles)} files not found. Saved in missing.txt")
        except IOError as e:
            print(f"❌ Error saving missing files: {e}")
    
    def ShowSummary(self, szOutputDir: str):
        """Show summary of the process"""
        szMapOutputDir = os.path.join(szOutputDir, self.g_szMapName)
        iCopiedCount = len(self.g_szResourceList) - len(self.g_szMissingFiles)
        
        print(f"\n🎉 Process completed!")
        print(f"📊 Summary:")
        print(f"   • Total resources: {len(self.g_szResourceList)}")
        print(f"   • Successfully copied: {iCopiedCount}")
        print(f"   • Missing files: {len(self.g_szMissingFiles)}")
        print(f"   • Output directory: {szMapOutputDir}")
    
    def Run(self):
        """Run the resource extractor"""
        print("=== Goldsrc ResGrab ===\n")
        
        # 1.Get output directory
        self.g_szOutputDir = self.GetOutputDirectory()
        
        # 2.Get .bsp file path
        szBspPath = self.GetBspFilePath()
        if not szBspPath:
            return
            
        self.g_szBspPath = szBspPath
        
        # 3.Extract map information
        szMapDir, self.g_szMapName, szResPath = self.ExtractMapInfo(szBspPath)
        
        # 4.Check/generate .res file
        if not os.path.isfile(szResPath):
            if not self.GenerateResFile(szMapDir, szBspPath, szResPath):
                return
        else:
            print("✅ .res file found.")
        
        # 5.Read resources
        self.g_szResourceList = self.ReadResourceFile(szResPath)
        
        if not self.g_szResourceList:
            print("⚠️  No resources found in the .res file.")
            return
            
        print(f"📦 {len(self.g_szResourceList)} resources detected.")
        
        # 6.Copy resources
        self.g_szMissingFiles = self.CopyResources(self.g_szResourceList, szBspPath, self.g_szOutputDir)
        
        # 7.Save missing files
        self.SaveMissingFiles(self.g_szMissingFiles, self.g_szOutputDir)
        
        # 8.Show summary
        self.ShowSummary(self.g_szOutputDir)

def main():
    """Main function"""
    try:
        g_ResourceExtractor = ResourceExtractor()
        g_ResourceExtractor.Run()
    except KeyboardInterrupt:
        print("\n\n⚠️  Process interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
