import re
import struct
import os
import subprocess

def extract(plugin_path: str, game_path: str, game_version: str) -> None:
    pass

def build(plugin_path: str, game_path: str, game_version: str) -> None:
    if game_version == "japan":
        return
    current_directory = os.getcwd()
    mod_name = current_directory.split('\\')[-1]
    os.chdir(current_directory + "/../../build")
    args = ["MMX4_" + mod_name + ".xml", "-noisogen", "-lbahead", "LBA.H"]
    result = subprocess.run(['mkpsxiso.exe'] + args, capture_output=True, text=True)
    for line in result.stdout:
        print(line, end='')

    # Read lines from the file "LBA.H"
    with open("LBA.H", "r") as file:
        lines = file.readlines()

    # Create a binary stream and binary writer
    with open("MMX4_" + mod_name + "/SLUS_005.61", 'rb') as file:
        file_contents = file.read()
    ms = bytearray(file_contents)

    # Define the DiscFiles list
    DiscFiles = [
    "LBA_CAPCOM_ARC",
    "LBA_COL00_0X_ARC",
    "LBA_COL00_0Z_ARC",
    "LBA_COL00_1X_ARC",
    "LBA_COL00_1Z_ARC",
    "LBA_COL01_0X_ARC",
    "LBA_COL01_0Z_ARC",
    "LBA_COL01_1X_ARC",
    "LBA_COL01_1Z_ARC",
    "LBA_COL02_0X_ARC",
    "LBA_COL02_0Z_ARC",
    "LBA_COL02_1X_ARC",
    "LBA_COL02_1Z_ARC",
    "LBA_COL03_0X_ARC",
    "LBA_COL03_0Z_ARC",
    "LBA_COL03_1X_ARC",
    "LBA_COL03_1Z_ARC",
    "LBA_COL04_0X_ARC",
    "LBA_COL04_0Z_ARC",
    "LBA_COL04_1X_ARC",
    "LBA_COL04_1Z_ARC",
    "LBA_COL05_0X_ARC",
    "LBA_COL05_0Z_ARC",
    "LBA_COL05_1X_ARC",
    "LBA_COL05_1Z_ARC",
    "LBA_COL06_0X_ARC",
    "LBA_COL06_0Z_ARC",
    "LBA_COL06_1X_ARC",
    "LBA_COL06_1Z_ARC",
    "LBA_COL07_0X_ARC",
    "LBA_COL07_0Z_ARC",
    "LBA_COL07_1X_ARC",
    "LBA_COL07_1Z_ARC",
    "LBA_COL08_0X_ARC",
    "LBA_COL08_0Z_ARC",
    "LBA_COL08_1X_ARC",
    "LBA_COL08_1Z_ARC",
    "LBA_COL09_0X_ARC",
    "LBA_COL09_0Z_ARC",
    "LBA_COL0A_0X_ARC",
    "LBA_COL0A_0Z_ARC",
    "LBA_COL0B_0X_ARC",
    "LBA_COL0B_0Z_ARC",
    "LBA_COL0B_1X_ARC",
    "LBA_COL0B_1Z_ARC",
    "LBA_COL0C_0X_ARC",
    "LBA_COL0C_0Z_ARC",
    "LBA_COL0C_1X_ARC",
    "LBA_COL0C_1Z_ARC",
    "LBA_COL0D_0X_ARC",
    "LBA_COL0D_0Z_ARC",
    "LBA_COL0E_U0_ARC",
    "LBA_COL0E_U1_ARC",
    "LBA_COL0F_U0_ARC",
    "LBA_COL0F_U1_ARC",
    "LBA_COLD_1U1_ARC",
    "LBA_COLD_1U2_ARC",
    "LBA_COLD_1U3_ARC",
    "LBA_COLD_1U4_ARC",
    "LBA_COLD_1U5_ARC",
    "LBA_COLD_1U6_ARC",
    "LBA_COLD_1U7_ARC",
    "LBA_COLD_1U8_ARC",
    "LBA_FONT8X8_ARC",
    "LBA_LOAD_U_ARC",
    "LBA_MOJIPAT_ARC",
    "LBA_ONPARE1_ARC",
    "LBA_ONPARE2_ARC",
    "LBA_ONPARE3_ARC",
    "LBA_ONPARE4_ARC",
    "LBA_ONPARE5_ARC",
    "LBA_ONPARE6_ARC",
    "LBA_ONPARE7_ARC",
    "LBA_ONPARE8_ARC",
    "LBA_PL00SEP_ARC",
    "LBA_PL00_U_ARC",
    "LBA_PL01SEP_ARC",
    "LBA_PL01_U_ARC",
    "LBA_PL02_U_ARC",
    "LBA_PLDEMO_ARC",
    "LBA_PLDEMO00_ARC",
    "LBA_PLDEMO01_ARC",
    "LBA_PLDEMO02_ARC",
    "LBA_PLDEMO03_ARC",
    "LBA_ST00_00_ARC",
    "LBA_ST00_01_ARC",
    "LBA_ST01_00_ARC",
    "LBA_ST01_01_ARC",
    "LBA_ST02_00_ARC",
    "LBA_ST02_01_ARC",
    "LBA_ST03_00_ARC",
    "LBA_ST03_01_ARC",
    "LBA_ST04_00_ARC",
    "LBA_ST04_01_ARC",
    "LBA_ST05_00_ARC",
    "LBA_ST05_01_ARC",
    "LBA_ST06_00_ARC",
    "LBA_ST06_01_ARC",
    "LBA_ST07_00_ARC",
    "LBA_ST07_01_ARC",
    "LBA_ST08_00_ARC",
    "LBA_ST08_01_ARC",
    "LBA_ST09_00_ARC",
    "LBA_ST0A_00_ARC",
    "LBA_ST0B_00_ARC",
    "LBA_ST0B_01_ARC",
    "LBA_ST0B_0X_ARC",
    "LBA_ST0B_0Z_ARC",
    "LBA_ST0C_00_ARC",
    "LBA_ST0C_01_ARC",
    "LBA_ST0C_U1_ARC",
    "LBA_ST0D_0X_ARC",
    "LBA_ST0D_0Z_ARC",
    "LBA_ST0E_U0_ARC",
    "LBA_ST0E_U1_ARC",
    "LBA_ST0F_U1_ARC",
    "LBA_ST0F_UX_ARC",
    "LBA_ST0F_UZ_ARC",
    "LBA_ST0_1_1_ARC",
    "LBA_ST1_1_1_ARC",
    "LBA_ST2_1_1_ARC",
    "LBA_ST3_1_1_ARC",
    "LBA_ST4_1_1_ARC",
    "LBA_ST5_1_1_ARC",
    "LBA_ST6_1_1_ARC",
    "LBA_ST7_1_1_ARC",
    "LBA_ST8_1_1_ARC",
    "LBA_STA_0_1_ARC",
    "LBA_STB_1_1_ARC",
    "LBA_STC_1_1_ARC",
    "LBA_STD_1_1U_ARC",
    "LBA_STD_1_2U_ARC",
    "LBA_STD_1_3U_ARC",
    "LBA_STD_1_4U_ARC",
    "LBA_STD_1_5U_ARC",
    "LBA_STD_1_6U_ARC",
    "LBA_STD_1_7U_ARC",
    "LBA_STD_1_8U_ARC",
    "LBA_CAPCOM20_STR",
    "LBA_OP_U_STR",
    "LBA_X1_U_STR",
    "LBA_X2_U_STR",
    "LBA_X3_U_STR",
    "LBA_X4_U_STR",
    "LBA_Z1_U_STR",
    "LBA_Z2_U_STR",
    "LBA_Z3_U_STR",
    "LBA_Z4_U_STR",
    "LBA_Z5_U_STR",
    "LBA_BGM1_U_XA",
    "LBA_BGM2_XA",
    "LBA_BGM3_XA",
    "LBA_BGM4_XA",
    "LBA_BGM5_U_XA",
    "LBA_BOSINT_U_XA",
    "LBA_VOICE1_U_XA",
    "LBA_VOICE2_U_XA",
    "LBA_VOICE3_U_XA",
    "LBA_VOICE4_U_XA",
    "LBA_VOICE5_U_XA"]

    Const = {"FileDataAddress": 0x800F0E18}

    # Iterate through each line in the "LBA.H" file
    for line in lines:
        if not line.strip():
            continue

        words = re.sub(r' {2,}', ' ', line.strip()).split()

        if words[0] != "#define":
            continue

        for file in DiscFiles:
            if file != words[1]:
                continue

            i = DiscFiles.index(file) * 12
            i += (Const["FileDataAddress"] - 0x80010000 + 0x800)

            sector = int(words[2], 16) if '0x' in words[2] else int(words[2])

            # Seek to the appropriate position in the binary stream and write the sector
            struct.pack_into('I', ms, i, sector)
    
    # Save the result to a file
    with open("MMX4_" + mod_name + "/SLUS_005.61", "wb") as file:
        file.write(ms)
    
    os.chdir(current_directory)
    pass
