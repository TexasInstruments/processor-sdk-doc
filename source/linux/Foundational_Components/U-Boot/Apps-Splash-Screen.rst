.. http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_U-Boot_Splash_Screen
.. highlight:: c

U-Boot Splash Screen
==========================

.. rubric:: Adding a splash screen
   :name: adding-a-splash-screen

.. rubric:: AM335x
   :name: am335x

All the code below is based on Processor Linux SDK 03.02.00..05.

There is a frame buffer driver for am335x in the drivers/video directory
called am3355x-fb.c. It makes calls to routines in board.c to set up the
LCDC and frame buffer. To use it:

Either create a new defconfig in the configs directory or just add
SPLASH to CONFIG\_SYS\_EXTRA\_OPTIONS. In this example the
am335x\_evm\_defconfig is copied into a new one called
am335x\_evm\_splash\_defconfig.

.. code-block:: text

    CONFIG_TARGET_AM335X_EVM=y
    CONFIG_SPL_STACK_R_ADDR=0x82000000
    CONFIG_DEFAULT_DEVICE_TREE="am335x-evm"
    CONFIG_SPL=y
    CONFIG_SPL_STACK_R=y
    CONFIG_SYS_EXTRA_OPTIONS="NAND,SPLASH"
    CONFIG_HUSH_PARSER=y
    CONFIG_AUTOBOOT_KEYED=y

In include/configs/am335x\_evm.h, add support for the splash screen,
LCDC, and gzipped bitmaps.

::

    /* Splash scrren support */
    #ifdef CONFIG_SPLASH
    #define CONFIG_AM335X_LCD
    #define CONFIG_LCD
    #define CONFIG_LCD_NOSTDOUT
    #define CONFIG_SYS_WHITE_ON_BLACK
    #define LCD_BPP LCD_COLOR16

    #define CONFIG_VIDEO_BMP_GZIP
    #define CONFIG_SYS_VIDEO_LOGO_MAX_SIZE  (1366*767*4)
    #define CONFIG_CMD_UNZIP
    #define CONFIG_CMD_BMP
    #define CONFIG_BMP_16BPP
    #endif

In arch/arm/cpu/armv7/am33xx/clock\_am33xx.c enable the LCDC clocks.

::

                    &cmrtc->rtcclkctrl,
                    &cmper->usb0clkctrl,
                    &cmper->emiffwclkctrl,
                    &cmper->emifclkctrl,
                    &cmper->lcdclkctrl,
                    &cmper->lcdcclkstctrl,
                    &cmper->epwmss2clkctrl,
                    0

In board.c add includes for mmc, fat, lcd, and the frame buffer.

::

    #include <libfdt.h>
    #include <fdt_support.h>
    #include <mmc.h>
    #include <fat.h>
    #include <lcd.h>
    #include <../../../drivers/video/am335x-fb.h>

This example code is based on the AM335x Starter Kit. A GPIO controls
the backlight so use GPIO\_TO\_PIN to define the GPIO.

::

    #define GPIO_ETH1_MODE          GPIO_TO_PIN(1, 26)

    /* GPIO that controls backlight on EVM-SK */
    #define GPIO_BACKLIGHT_EN       GPIO_TO_PIN(3, 17)

In board\_late\_init call the splash screen routine.

::

    #if !defined(CONFIG_SPL_BUILD)
            splash_screen();
            /* try reading mac address from efuse */
            mac_lo = readl(&cdev->macid0l);
            mac_hi = readl(&cdev->macid0h);

The following routines enable the backlight, load the LCD timings (this
example is based on Starter Kit), power on the LCD and enable it, then
finally the splash screen code that registers a fat file system on mmc0.
The gzipped bitmap is named splash.bmp.gz and is displayed with
bmp\_display.

.. code-block:: text

    #if defined(CONFIG_LCD) && defined(CONFIG_AM335X_LCD) && \
                    !defined(CONFIG_SPL_BUILD)
    void lcdbacklight(int on)
    {
            gpio_request(GPIO_BACKLIGHT_EN, "backlight_en");
            if (on)
                    gpio_direction_output(GPIO_BACKLIGHT_EN, 0);
            else
                    gpio_direction_output(GPIO_BACKLIGHT_EN, 1);
    }

    int  load_lcdtiming(struct am335x_lcdpanel *panel)
    {
            struct am335x_lcdpanel pnltmp;

            pnltmp.hactive = 480;
            pnltmp.vactive = 272;
            pnltmp.bpp = 16;
            pnltmp.hfp = 8;
            pnltmp.hbp = 43;
            pnltmp.hsw = 4;
            pnltmp.vfp = 4;
            pnltmp.vbp = 12;
            pnltmp.vsw = 10;
            pnltmp.pxl_clk_div = 2;
            pnltmp.pol = 0;
            pnltmp.pup_delay = 1;
            pnltmp.pon_delay = 1;
            panel_info.vl_rot = 0;

            memcpy((void *)panel, (void *)&pnltmp, sizeof(struct am335x_lcdpanel));

            return 0;
    }

    void lcdpower(int on)
    {
            lcd_enable();
    }

    vidinfo_t       panel_info = {
                    .vl_col = 480,
                    .vl_row = 272,
                    .vl_bpix = 4,
                    .priv = 0
    };

    void lcd_ctrl_init(void *lcdbase)
    {
            struct am335x_lcdpanel lcd_panel;

            memset(&lcd_panel, 0, sizeof(struct am335x_lcdpanel));
            if (load_lcdtiming(&lcd_panel) != 0)
                    return;

            lcd_panel.panel_power_ctrl = &lcdpower;

            if (am335xfb_init(&lcd_panel) != 0)
                    printf("ERROR: failed to initialize video!");

            /* Modify panel into to real resolution */
            panel_info.vl_col = lcd_panel.hactive;
            panel_info.vl_row = lcd_panel.vactive;

    //      lcd_set_flush_dcache(1);
    }

    void lcd_enable(void)
    {
            lcdbacklight(1);
    }

    void splash_screen(void)
    {
            struct mmc      *mmc = NULL;
            int             err;

            mmc = find_mmc_device(0);
            if (!mmc)
                    printf("Error finding mmc device\n");

            mmc_init(mmc);

            err = fat_register_device(&mmc->block_dev,
                                            CONFIG_SYS_MMCSD_FS_BOOT_PARTITION);

            if (!err) {
                    err = file_fat_read("splash.bmp.gz", (void *)0x82000000, 0);
                    bmp_display(0x82000000, 0, 0);
            }
    }
    #endif

In mux.c define the LCDC pin mux.

::

    #ifdef CONFIG_AM335X_LCD
    static struct module_pin_mux lcd_pin_mux[] = {
            {OFFSET(lcd_data0), (MODE(0) | PULLUDDIS)},     /* LCD-Data(0) */
            {OFFSET(lcd_data1), (MODE(0) | PULLUDDIS)},     /* LCD-Data(1) */
            {OFFSET(lcd_data2), (MODE(0) | PULLUDDIS)},     /* LCD-Data(2) */
            {OFFSET(lcd_data3), (MODE(0) | PULLUDDIS)},     /* LCD-Data(3) */
            {OFFSET(lcd_data4), (MODE(0) | PULLUDDIS)},     /* LCD-Data(4) */
            {OFFSET(lcd_data5), (MODE(0) | PULLUDDIS)},     /* LCD-Data(5) */
            {OFFSET(lcd_data6), (MODE(0) | PULLUDDIS)},     /* LCD-Data(6) */
            {OFFSET(lcd_data7), (MODE(0) | PULLUDDIS)},     /* LCD-Data(7) */
            {OFFSET(lcd_data8), (MODE(0) | PULLUDDIS)},     /* LCD-Data(8) */
            {OFFSET(lcd_data9), (MODE(0) | PULLUDDIS)},     /* LCD-Data(9) */
            {OFFSET(lcd_data10), (MODE(0) | PULLUDDIS)},    /* LCD-Data(10) */
            {OFFSET(lcd_data11), (MODE(0) | PULLUDDIS)},    /* LCD-Data(11) */
            {OFFSET(lcd_data12), (MODE(0) | PULLUDDIS)},    /* LCD-Data(12) */
            {OFFSET(lcd_data13), (MODE(0) | PULLUDDIS)},    /* LCD-Data(13) */
            {OFFSET(lcd_data14), (MODE(0) | PULLUDDIS)},    /* LCD-Data(14) */
            {OFFSET(lcd_data15), (MODE(0) | PULLUDDIS)},    /* LCD-Data(15) */
            {OFFSET(gpmc_ad8), (MODE(1) | PULLUDDIS)},      /* LCD-Data(16) */
            {OFFSET(gpmc_ad9), (MODE(1) | PULLUDDIS)},      /* LCD-Data(17) */
            {OFFSET(gpmc_ad10), (MODE(1) | PULLUDDIS)},     /* LCD-Data(18) */
            {OFFSET(gpmc_ad11), (MODE(1) | PULLUDDIS)},     /* LCD-Data(19) */
            {OFFSET(gpmc_ad12), (MODE(1) | PULLUDDIS)},     /* LCD-Data(20) */
            {OFFSET(gpmc_ad13), (MODE(1) | PULLUDDIS)},     /* LCD-Data(21) */
            {OFFSET(gpmc_ad14), (MODE(1) | PULLUDDIS)},     /* LCD-Data(22) */
            {OFFSET(gpmc_ad15), (MODE(1) | PULLUDDIS)},     /* LCD-Data(23) */
            {OFFSET(lcd_vsync), (MODE(0) | PULLUDDIS)},     /* LCD-VSync */
            {OFFSET(lcd_hsync), (MODE(0) | PULLUDDIS)},     /* LCD-HSync */
            {OFFSET(lcd_ac_bias_en), (MODE(0) | PULLUDDIS)},/* LCD-DE */
            {OFFSET(lcd_pclk), (MODE(0) | PULLUDDIS)},      /* LCD-CLK */

            /* backlight */
            {OFFSET(mcasp0_ahclkr), (MODE(7) | PULLUDDIS)}, /* mcasp0_gpio */

            {-1},
    };
    #endif

And enable the LCD.

::

            } else if (board_is_evm_sk()) {
                    /* Starter Kit EVM */
                    configure_module_pin_mux(i2c1_pin_mux);
                    configure_module_pin_mux(gpio0_7_pin_mux);
                    configure_module_pin_mux(rgmii1_pin_mux);
                    configure_module_pin_mux(mmc0_pin_mux_sk_evm);
    #ifdef CONFIG_AM335X_LCD
                    configure_module_pin_mux(lcd_pin_mux);
    #endif
            } else if (board_is_bone_lt()) {

