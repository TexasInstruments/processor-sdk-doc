.. _mmc-sd-card-compatibility-label:

#################################
SD Card Compatibility Data Points
#################################

Some SD cards may not boot as expected on TI EVMs. This varies by SD card manufacturer, model, capacity, speed, and other factors. A variety have been tested and are documented in the table below:

.. note::

   Tested on SDK v11.01.05. "MISMATCH" result means board boots but shows mismatching speed modes in U-Boot and Kernel.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. csv-table::
      :header: SoC,Board,Brand,Capacity (GB),Model,Bus Interface,Speed Class,UHS Speed Class,App Performance,Video Speed Class,Color,Pass/Fail,Speed Mode (U-Boot / Kernel),Notes

      AM62X,SK-AM62B-P1,SanDisk,4,,I,C4,,,,Black,PASS,UHS SDR50/DDR50,
      AM62X,SK-AM62B-P1,SanDisk,8,,I,C4,,,,Black,PASS,UHS SDR50/DDR50,
      AM62X,SK-AM62B-P1,SanDisk,16,,,C4,,,,Black,PASS,SD High Speed,
      AM62X,SK-AM62B-P1,SanDisk,16,Edge,I,C10,U1,A1,,Black,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,SanDisk,32,Edge,I,C10,U1,A1,,Black,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,SanDisk,8,Ultra Red,I,C10,,,,Red-grey,PASS,UHS SDR50/DDR50,
      AM62X,SK-AM62B-P1,SanDisk,16,Ultra Red,I,C10,,A1,,Red-grey,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,SanDisk,32,Ultra Red,I,C10,U1,A1,,Red-grey,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,SanDisk,16,Ultra White,I,C10,,,,White-grey,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,SanDisk,32,Ultra White,I,C10,,,,White-grey,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,SanDisk,32,Extreme,I,,U3,A1,V30,Red-gold,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,SanDisk,32,Max Endurance,I,C10,U3,,V30,White-gold,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,Lexar,32,,I,,U1,A1,V10,White-red,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,Gigastone,16,Camera Plus,I,C10,U1,,,Red-white,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,Kootion,16,,I,C10,U1,,,White-red,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,Kingston,8,,,C4,,,,Black,PASS,SD High Speed,
      AM62X,SK-AM62B-P1,Kingston,32,Canvas Select Plus,I,,U1,A1,V10,Black-pink,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,Kingston,32,,I,C10,U3,,,Black-red,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,Micro Center,16,,I,C10,U1,,,Black,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,Micro Center,32,,I,C10,U1,,,Black,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,Patriot,16,,I,C10,U1,,,Black,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,Patriot,32,,I,C10,U1,,,Black,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,Transcend,8,,I,C4,,,,Black,PASS,UHS SDR50/DDR50,
      AM62X,SK-AM62B-P1,Transcend,8,Premium 400x,I,C10,U1,,,Red-black,MISMATCH,UHS SDR104 (u-boot) / ultra high speed SDR50 SDHC (kernel),
      AM62X,SK-AM62B-P1,Transcend,32,Premium,I,C10,U1,,,Red-black,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,Transcend,16,,I,C10,U1,,,Silver,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,Transcend,64,Ultra Performance,I,,U3,A2,V30,Silver-black,PASS,UHS SDR104,
      AM62X,SK-AM62A-LP,Strontium,32,Nitro,I,C10,U1,,,Black,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,Kexin,8,,,C10,,,,Green-black,PASS,SD High Speed,
      AM62X,SK-AM62B-P1,Kexin,16,,I,C10,U1,,,Green-black,MISMATCH,UHS SDR104 (u-boot) / high speed SDHC (kernel),
      AM62X,SK-AM62B-P1,PNY,16,,,C4,,,,Black,PASS,SD High Speed,
      AM62X,SK-AM62B-P1,PNY,16,Elite,I,,U1,,,Green-grey,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,PNY,32,Elite,I,,U1,,,Green-grey,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,PNY,64,Elite-X,I,,U3,A1,V30,Green-black,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,Samsung,32,EVO Select,I,,U1,,,White-green,PASS,UHS SDR104,
      AM62X,SK-AM62B-P1,,8,,,C4,,,,Black,PASS,UHS SDR50/DDR50,


.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   .. csv-table::
      :header: SoC,Board,Brand,Capacity (GB),Model,Bus Interface,Speed Class,UHS Speed Class,App Performance,Video Speed Class,Color,Pass/Fail,Speed Mode (U-Boot / Kernel),Notes

      AM62AX,SK-AM62A-LP,SanDisk,4,,I,C4,,,,Black,PASS,UHS SDR50/DDR50,
      AM62AX,SK-AM62A-LP,SanDisk,8,,I,C4,,,,Black,PASS,UHS SDR50/DDR50,
      AM62AX,SK-AM62A-LP,SanDisk,16,,,C4,,,,Black,PASS,SD High Speed,
      AM62AX,SK-AM62A-LP,SanDisk,16,Edge,I,C10,U1,A1,,Black,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,SanDisk,32,Edge,I,C10,U1,A1,,Black,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,SanDisk,8,Ultra Red,I,C10,,,,Red-grey,PASS,UHS SDR50/DDR50,
      AM62AX,SK-AM62A-LP,SanDisk,16,Ultra Red,I,C10,,A1,,Red-grey,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,SanDisk,32,Ultra Red,I,C10,U1,A1,,Red-grey,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,SanDisk,16,Ultra White,I,C10,,,,White-grey,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,SanDisk,32,Ultra White,I,C10,,,,White-grey,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,SanDisk,32,Extreme,I,,U3,A1,V30,Red-gold,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,SanDisk,32,Max Endurance,I,C10,U3,,V30,White-gold,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,Lexar,32,,I,,U1,A1,V10,White-red,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,Gigastone,16,Camera Plus,I,C10,U1,,,Red-white,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,Kootion,16,,I,C10,U1,,,White-red,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,Kingston,8,,,C4,,,,Black,PASS,SD High Speed,
      AM62AX,SK-AM62A-LP,Kingston,32,Canvas Select Plus,I,,U1,A1,V10,Black-pink,PASS,UHS SDR104,"1/6 of the ones we tested of this type failed to boot, giving this error:

      Trying to boot from MMC2
      Error reading cluster
      spl_load_image_fat: error reading image u-boot.img, err - -22
      SPL: failed to boot from all boot devices
      ### ERROR ### Please RESET the board ###"
      AM62AX,SK-AM62A-LP,Kingston,32,,I,C10,U3,,,Black-red,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,Micro Center,16,,I,C10,U1,,,Black,PASS,UHS SDR104,"3/7 of the ones we tested of this type failed to boot, giving this error:

      Trying to boot from MMC2
      Error reading cluster
      spl_load_image_fat: error reading image u-boot.img, err - -22
      SPL: failed to boot from all boot devices
      ### ERROR ### Please RESET the board ###"
      AM62AX,SK-AM62A-LP,Micro Center,32,,I,C10,U1,,,Black,FAIL,,"The 1 card we tested of this type failed to boot, giving this error:

      Trying to boot from MMC2
      Error reading cluster
      spl_load_image_fat: error reading image u-boot.img, err - -22
      SPL: failed to boot from all boot devices
      ### ERROR ### Please RESET the board ###"
      AM62AX,SK-AM62A-LP,Patriot,16,,I,C10,U1,,,Black,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,Patriot,32,,I,C10,U1,,,Black,PASS,UHS SDR104,"8/10 of the ones we tested of this type failed to boot, giving this error:

      Trying to boot from MMC2
      Error reading cluster
      spl_load_image_fat: error reading image u-boot.img, err - -22
      SPL: failed to boot from all boot devices
      ### ERROR ### Please RESET the board ###"
      AM62AX,SK-AM62A-LP,Transcend,8,,I,C4,,,,Black,PASS,UHS SDR50/DDR50,
      AM62AX,SK-AM62A-LP,Transcend,8,Premium 400x,I,C10,U1,,,Red-black,MISMATCH,UHS SDR104 (u-boot) / ultra high speed SDR50 SDHC (kernel),
      AM62AX,SK-AM62A-LP,Transcend,32,Premium,I,C10,U1,,,Red-black,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,Transcend,16,,I,C10,U1,,,Silver,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,Transcend,64,Ultra Performance,I,,U3,A2,V30,Silver-black,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,Strontium,32,Nitro,I,C10,U1,,,Black,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,Kexin,8,,,C10,,,,Green-black,PASS,SD High Speed,
      AM62AX,SK-AM62A-LP,Kexin,16,,I,C10,U1,,,Green-black,MISMATCH,UHS SDR104 (u-boot) / high speed SDHC (kernel),
      AM62AX,SK-AM62A-LP,PNY,16,,,C4,,,,Black,PASS,SD High Speed,
      AM62AX,SK-AM62A-LP,PNY,16,Elite,I,,U1,,,Green-grey,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,PNY,32,Elite,I,,U1,,,Green-grey,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,PNY,64,Elite-X,I,,U3,A1,V30,Green-black,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,Samsung,32,EVO Select,I,,U1,,,White-green,PASS,UHS SDR104,
      AM62AX,SK-AM62A-LP,,8,,,C4,,,,Black,PASS,UHS SDR50/DDR50,


.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   .. csv-table::
      :header: SoC,Board,Brand,Capacity (GB),Model,Bus Interface,Speed Class,UHS Speed Class,App Performance,Video Speed Class,Color,Pass/Fail,Speed Mode (U-Boot / Kernel),Notes

      AM62PX,SK-AM62P-LP,SanDisk,4,,I,C4,,,,Black,PASS,UHS SDR50/DDR50,
      AM62PX,SK-AM62P-LP,SanDisk,8,,I,C4,,,,Black,PASS,UHS SDR50/DDR50,
      AM62PX,SK-AM62P-LP,SanDisk,16,,,C4,,,,Black,PASS,SD High Speed,
      AM62PX,SK-AM62P-LP,SanDisk,16,Edge,I,C10,U1,A1,,Black,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,SanDisk,32,Edge,I,C10,U1,A1,,Black,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,SanDisk,8,Ultra Red,I,C10,,,,Red-grey,PASS,UHS SDR50/DDR50,
      AM62PX,SK-AM62P-LP,SanDisk,16,Ultra Red,I,C10,,A1,,Red-grey,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,SanDisk,32,Ultra Red,I,C10,U1,A1,,Red-grey,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,SanDisk,16,Ultra White,I,C10,,,,White-grey,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,SanDisk,32,Ultra White,I,C10,,,,White-grey,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,SanDisk,32,Extreme,I,,U3,A1,V30,Red-gold,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,SanDisk,32,Max Endurance,I,C10,U3,,V30,White-gold,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,Lexar,32,,I,,U1,A1,V10,White-red,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,Gigastone,16,Camera Plus,I,C10,U1,,,Red-white,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,Kootion,16,,I,C10,U1,,,White-red,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,Kingston,8,,,C4,,,,Black,PASS,SD High Speed,
      AM62PX,SK-AM62P-LP,Kingston,32,Canvas Select Plus,I,,U1,A1,V10,Black-pink,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,Kingston,32,,I,C10,U3,,,Black-red,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,Micro Center,16,,I,C10,U1,,,Black,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,Micro Center,32,,I,C10,U1,,,Black,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,Patriot,16,,I,C10,U1,,,Black,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,Patriot,32,,I,C10,U1,,,Black,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,Transcend,8,,I,C4,,,,Black,PASS,UHS SDR50/DDR50,
      AM62PX,SK-AM62P-LP,Transcend,8,Premium 400x,I,C10,U1,,,Red-black,MISMATCH,UHS SDR104 (u-boot) / ultra high speed SDR50 SDHC (kernel),
      AM62PX,SK-AM62P-LP,Transcend,32,Premium,I,C10,U1,,,Red-black,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,Transcend,16,,I,C10,U1,,,Silver,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,Transcend,64,Ultra Performance,I,,U3,A2,V30,Silver-black,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,Strontium,32,Nitro,I,C10,U1,,,Black,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,Kexin,8,,,C10,,,,Green-black,PASS,SD High Speed,
      AM62PX,SK-AM62P-LP,Kexin,16,,I,C10,U1,,,Green-black,MISMATCH,UHS SDR104 (u-boot) / high speed SDHC (kernel),
      AM62PX,SK-AM62P-LP,PNY,16,,,C4,,,,Black,PASS,SD High Speed,
      AM62PX,SK-AM62P-LP,PNY,16,Elite,I,,U1,,,Green-grey,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,PNY,32,Elite,I,,U1,,,Green-grey,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,PNY,64,Elite-X,I,,U3,A1,V30,Green-black,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,Samsung,32,EVO Select,I,,U1,,,White-green,PASS,UHS SDR104,
      AM62PX,SK-AM62P-LP,,8,,,C4,,,,Black,PASS,UHS SDR50/DDR50,


.. ifconfig:: CONFIG_part_variant in ('AM64X')

   .. note::

      The below table was tested on a TMDS64EVM without the solution described in Section "4.3 Issue 3 - uSD Card Boot Not Working" on page 61 of the
      AM64x EVM User's guide: https://www.ti.com/lit/pdf/SPRUJ63.

   .. csv-table::
      :header: SoC,Board,Brand,Capacity (GB),Model,Bus Interface,Speed Class,UHS Speed Class,App Performance,Video Speed Class,Color,Pass/Fail,Speed Mode (U-Boot / Kernel),Notes

      AM64X,TMDS64EVM,SanDisk,4,,I,C4,,,,Black,MISMATCH,SD High Speed (u-boot) / ultra high speed DDR50 SDHC (kernel),
      AM64X,TMDS64EVM,SanDisk,8,,I,C4,,,,Black,MISMATCH,SD High Speed (u-boot) / ultra high speed DDR50 SDHC (kernel),
      AM64X,TMDS64EVM,SanDisk,16,,,C4,,,,Black,PASS,SD High Speed,
      AM64X,TMDS64EVM,SanDisk,16,Edge,I,C10,U1,A1,,Black,MISMATCH,SD High Speed (u-boot) / ultra high speed SDR104 SDHC (kernel),
      AM64X,TMDS64EVM,SanDisk,32,Edge,I,C10,U1,A1,,Black,MISMATCH,SD High Speed (u-boot) / ultra high speed SDR104 SDHC (kernel),
      AM64X,TMDS64EVM,SanDisk,8,Ultra Red,I,C10,,,,Red-grey,MISMATCH,SD High Speed (u-boot) / ultra high speed DDR50 SDHC (kernel),
      AM64X,TMDS64EVM,SanDisk,16,Ultra Red,I,C10,,A1,,Red-grey,MISMATCH,SD High Speed (u-boot) / ultra high speed SDR104 SDHC (kernel),
      AM64X,TMDS64EVM,SanDisk,32,Ultra Red,I,C10,U1,A1,,Red-grey,FAIL,,"U-Boot SPL 2025.01-00527-gd2a72467939e (Jul 01 2025 - 21:23:47 +0000)
      Resetting on cold boot to workaround ErrataID:i2331
      Please resend tiboot3.bin in case of UART/DFU boot
      resetting ..."
      AM64X,TMDS64EVM,SanDisk,16,Ultra White,I,C10,,,,White-grey,MISMATCH,SD High Speed (u-boot) / ultra high speed SDR104 SDHC (kernel),
      AM64X,TMDS64EVM,SanDisk,32,Ultra White,I,C10,,,,White-grey,MISMATCH,SD High Speed (u-boot) / ultra high speed SDR104 SDHC (kernel),
      AM64X,TMDS64EVM,SanDisk,32,Extreme,I,,U3,A1,V30,Red-gold,MISMATCH,SD High Speed (u-boot) / ultra high speed SDR104 SDHC (kernel),
      AM64X,TMDS64EVM,SanDisk,32,Max Endurance,I,C10,U3,,V30,White-gold,MISMATCH,SD High Speed (u-boot) / ultra high speed SDR104 SDHC (kernel),
      AM64X,TMDS64EVM,Lexar,32,,I,,U1,A1,V10,White-red,MISMATCH,SD High Speed (u-boot) / ultra high speed SDR104 SDHC (kernel),
      AM64X,TMDS64EVM,Gigastone,16,Camera Plus,I,C10,U1,,,Red-white,MISMATCH,SD High Speed (u-boot) / ultra high speed SDR104 SDHC (kernel),
      AM64X,TMDS64EVM,Kootion,16,,I,C10,U1,,,White-red,PASS,UHS SDR104,
      AM64X,TMDS64EVM,Kingston,8,,,C4,,,,Black,PASS,SD High Speed,
      AM64X,TMDS64EVM,Kingston,32,Canvas Select Plus,I,,U1,A1,V10,Black-pink,PASS,UHS SDR104,
      AM64X,TMDS64EVM,Kingston,32,,I,C10,U3,,,Black-red,MISMATCH,SD High Speed (u-boot) / ultra high speed SDR104 SDHC (kernel),
      AM64X,TMDS64EVM,Micro Center,16,,I,C10,U1,,,Black,PASS,UHS SDR104,
      AM64X,TMDS64EVM,Micro Center,32,,I,C10,U1,,,Black,PASS,UHS SDR104,
      AM64X,TMDS64EVM,Patriot,16,,I,C10,U1,,,Black,PASS,UHS SDR104,
      AM64X,TMDS64EVM,Patriot,32,,I,C10,U1,,,Black,PASS,UHS SDR104,
      AM64X,TMDS64EVM,Transcend,8,,I,C4,,,,Black,MISMATCH,SD High Speed (u-boot) / ultra high speed DDR50 SDHC (kernel),
      AM64X,TMDS64EVM,Transcend,8,Premium 400x,I,C10,U1,,,Red-black,PASS,UHS SDR104,
      AM64X,TMDS64EVM,Transcend,32,Premium,I,C10,U1,,,Red-black,MISMATCH,SD High Speed (u-boot) / ultra high speed SDR104 SDHC (kernel),
      AM64X,TMDS64EVM,Transcend,16,,I,C10,U1,,,Silver,MISMATCH,SD High Speed (u-boot) / ultra high speed SDR104 SDHC (kernel),
      AM64X,TMDS64EVM,Transcend,64,Ultra Performance,I,,U3,A2,V30,Silver-black,MISMATCH,SD High Speed (u-boot) / ultra high speed SDR104 SDHC (kernel),
      AM64X,TMDS64EVM,Strontium,32,Nitro,I,C10,U1,,,Black,FAIL,,"U-Boot SPL 2025.01-00527-gd2a72467939e (Jul 01 2025 - 21:23:47 +0000)
      Resetting on cold boot to workaround ErrataID:i2331
      Please resend tiboot3.bin in case of UART/DFU boot
      resetting ..."
      AM64X,TMDS64EVM,Kexin,8,,,C10,,,,Green-black,PASS,SD High Speed,
      AM64X,TMDS64EVM,Kexin,16,,I,C10,U1,,,Green-black,MISMATCH,UHS SDR104 (u-boot) / high speed SDHC (kernel),
      AM64X,TMDS64EVM,PNY,16,,,C4,,,,Black,PASS,SD High Speed,
      AM64X,TMDS64EVM,PNY,16,Elite,I,,U1,,,Green-grey,MISMATCH,SD High Speed (u-boot) / ultra high speed SDR104 SDHC (kernel),
      AM64X,TMDS64EVM,PNY,32,Elite,I,,U1,,,Green-grey,PASS,UHS SDR104,
      AM64X,TMDS64EVM,PNY,64,Elite-X,I,,U3,A1,V30,Green-black,FAIL,,"U-Boot SPL 2025.01-00527-gd2a72467939e (Jul 01 2025 - 21:23:47 +0000)
      Resetting on cold boot to workaround ErrataID:i2331
      Please resend tiboot3.bin in case of UART/DFU boot
      resetting ..."
      AM64X,TMDS64EVM,Samsung,32,EVO Select,I,,U1,,,White-green,PASS,UHS SDR104,
      AM64X,TMDS64EVM,,8,,,C4,,,,Black,MISMATCH,SD High Speed (u-boot) / ultra high speed DDR50 SDHC (kernel),
