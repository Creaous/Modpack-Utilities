import os
import glob
import tomllib

curseforge_mods = []
modrinith_mods = []

for f in glob.iglob("*.url.txt"):
    print(f"Removing: {f}")
    os.remove(f)

for f in glob.iglob("*.toml"):
    with open(f, "rb") as f:
        data = tomllib.load(f)
        print(f"Processing: {f.name}")

        if data["download"]["mode"] != "metadata:curseforge":
            modrinith_mods.append(f.name)

            f = open(data["filename"] + ".url.txt","w+")
            f.write(data["download"]["url"])
            f.write("\n")
            f.write(data["download"]["hash"])
            f.close()
        else:
            curseforge_mods.append(f.name)
            print(f"Skipped: {f.name}")

print("\n\n\n")
print(f"Processed the following Modrinith mods: {modrinith_mods}")
print("\n")
print(f"Skipped the following CurseForge mods: {curseforge_mods}")
