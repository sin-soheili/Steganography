
# Steganography ( مخفی‌سازی اطلاعات در تصاویر )

این پروژه یک ابزار ساده است که متن‌ها را در تصاویر مخفی می‌کند و سپس از آن‌ها بازیابی می‌کند. این برنامه از **پایتون** و کتابخانه‌های `Pillow` (برای کار با تصاویر) و `numpy` (برای پردازش داده‌ها) استفاده می‌کند.

## ویژگی‌ها

- مخفی‌سازی متن در تصاویر PNG
- بازیابی متن مخفی‌شده از تصاویر
- امکان اضافه کردن پایان‌نامه برای شناسایی انتهای متن مخفی‌شده
- قابلیت استفاده در هر سیستم‌عاملی که از پایتون پشتیبانی می‌کند

## نحوه استفاده

### پیش‌نیازها

قبل از شروع به استفاده از این پروژه، باید کتابخانه‌های زیر را نصب کنید:

```bash
pip install pillow numpy
```

### مخفی کردن متن در تصویر

برای مخفی کردن یک متن در تصویر، کافی است دستور زیر را اجرا کنید:

```python
from steganography import hide_text

hide_text("input.png", "این یک پیام مخفی است!", "output.png")
```

در اینجا:
- `"input.png"` نام تصویر ورودی است.
- `"این یک پیام مخفی است!"` متنی است که می‌خواهید مخفی کنید.
- `"output.png"` تصویری است که متن مخفی‌شده در آن ذخیره می‌شود.

### بازیابی متن از تصویر

برای بازیابی متن مخفی‌شده از تصویر، از دستور زیر استفاده کنید:

```python
from steganography import extract_text

message = extract_text("output.png")
print("متن بازیابی شده:", message)
```

در اینجا:
- `"output.png"` همان تصویری است که متن در آن مخفی شده است.

### نحوه ساخت و اجرا

1. ابتدا تصویر ورودی (`input.png`) را آماده کنید.
2. کد بالا را برای مخفی‌سازی متن اجرا کنید.
3. برای بازیابی متن، کد `extract_text` را اجرا کنید.

## نکات امنیتی

این پروژه به‌طور ساده و برای مقاصد آموزشی طراحی شده است. به هیچ‌وجه از این تکنیک‌ها برای اهداف مخرب استفاده نکنید. استفاده از این پروژه در موارد غیرقانونی یا غیر اخلاقی می‌تواند تبعات قانونی به‌دنبال داشته باشد.

## الهام‌بخش

این پروژه از تکنیک‌های اولیه استگانورافی (Steganography) استفاده می‌کند که به‌طور سنتی برای پنهان کردن پیام‌ها در رسانه‌ها (مانند تصاویر) طراحی شده‌اند.

## ارتباط با ما

اگر سوالی دارید یا مشکلاتی در استفاده از این پروژه داشتید، می‌توانید به این پروژه بپردازید یا آن را بهبود ببخشید و درخواست‌هایتان را ارسال کنید.

- [گزارش مشکل یا ایجاد Issue](https://github.com/sin-soheili/Steganography/issues)
- [پروژه‌ها و ایده‌ها](https://github.com/sin-soheili)
