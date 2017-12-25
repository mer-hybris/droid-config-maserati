# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device maserati
%define vendor motorola
%define vendor_pretty Motorola
%define device_pretty Droid 4
%define dcd_path ./
# Adjust this for your device
%define pixel_ratio 1.12
# We assume most devices will
%define have_modem 1
%define community_adaptation 1

Provides: connman-configs connman-configs-sailfish ofono-configs
%include droid-configs-device/droid-configs.inc
