#!/bin/sh
mount -o remount,rw /system

cp /boot/kernel-* /system/etc/kexec/kernel
cp /boot/boot-initramfs.gz /system/etc/kexec/ramdisk.img

mount -o remount,ro /system
