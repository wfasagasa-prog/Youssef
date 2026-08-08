[app]

# اسم التطبيق (يظهر تحت الأيقونة)
title = آلة حاسبة

# اسم الحزمة (يجب أن يكون إنجليزي بدون مسافات)
package.name = calculator
package.domain = org.youssef

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# المتطلبات (كافي لهذا التطبيق البسيط)
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# أيقونة (اختياري - ضع ملف icon.png في المجلد)
# icon.filename = %(source.dir)s/icon.png

# Android settings
android.permissions = INTERNET
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

# p4a
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
