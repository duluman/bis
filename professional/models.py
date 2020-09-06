from django.db import models

# Create your models here.


class ProfessionalDevelopment(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    body = models.TextField(default=None, blank=True)
    date = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='professional/', blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class ProfessionalBackground(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    SIZE_CHOICE = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    ]

    title_size = models.CharField(
        max_length=100,
        default="1",
        choices=SIZE_CHOICE,
        blank=True,
        null=True)

    COLOR_CHOICE = [
        ("white", "white"),
        ("black", "black"),
        ("cyan", "cyan"),
        ("indigo", "indigo"),
        ("blue", "blue"),
        ("red", "red"),
        ("green", "green"),
        ("amber", "amber"),
        ("pink", "pink")]

    title_color = models.CharField(
        max_length=100,
        choices=COLOR_CHOICE,
        default=None,
        blank=True,
        null=True
    )

    subtitle = models.CharField(max_length=455, default=None, blank=True)

    subtitle_size = models.CharField(
        max_length=100,
        default="5",
        choices=SIZE_CHOICE,
        blank=True,
        null=True)

    subtitle_color = models.CharField(
        max_length=100,
        choices=COLOR_CHOICE,
        default=None,
        blank=True,
        null=True
    )

    mask_overlay = models.CharField(max_length=255, default='rgba-white-light', blank=True, null=True)
    picture = models.ImageField(upload_to='professional/', blank=True, null=True)

    def __str__(self):
        return self.title


class BestFeatureCounterTitle(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)

    def __str__(self):
        return self.title


class BestFeatureCounter(models.Model):

    title = models.CharField(max_length=255, default=None)
    ICON_CHOICES = [
                    ("heart", "heart"),
                    ("bicycle", "bicycle"),
                    ("bug", "bug"),
                    ("bell", "bell"),
                    ("birthday-cake", "birthday-cake"),
                    ("gift", "gift"),
                    ("magic", "magic"),
                    ("award", "award"),
                    ("balance-scale", "balance-scale"),
                    ("battery-full", "battery-full"),
                    ("bible", "bible"),
                    ("book", "book"),
                    ("brain", "brain"),
                    ("camera-retro", "camera-retro"),
                    ("calendar-check", "calendar-check"),
                    ("charging-station", "charging-station"),
                    ("check-square", "check-square"),
                    ("code", "code"),
                    ("coffee", "coffee"),
                    ("dice-d20", "dice-d20"),
                    ("dna", "dna"),
                    ("dog", "dog"),
                    ("dove", "dove"),
                    ("dragon", "dragon"),
                    ("envelope-open-text", "envelope-open-text"),
                    ("eye", "eye"),
                    ("feather-alt", "feather-alt"),
                    ("fighter-jet", "fighter-jet"),
                    ("fire", "fire"),
                    ("fish", "fish"),
                    ("flag", "flag"),
                    ("gem", "gem"),
                    ("gifts", "gifts"),
                    ("globe", "globe"),
                    ("graduation-cap", "graduation-cap"),
                    ("smile face", "grin"),
                    ("grin-alt", "grin-alt"),
                    ("grin-stars", "grin-stars"),
                    ("grin-hearts", "grin-hearts"),
                    ("grin-wink", "grin-wink"),
                    ("grin-tears", "grin-tears"),
                    ("blog", "blog"),
                    ("guitar", "guitar"),
                    ("home", "home"),
                    ("handshake", "handshake"),
                    ("hat-wizard", "hat-wizard"),
                    ("heart music foto", "icons"),
                    ("hotel", "hotel"),
                    ("key", "key"),
                    ("leaf", "leaf"),
                    ("lock", "lock"),
                    ("map", "map"),
                    ("music", "music"),
                    ("pencil-alt", "pencil-alt"),
                    ("atom", "react"),
                    ("scroll", "scroll"),
                    ("adjust", "adjust"),
                    ("snowflake", "snowflake"),
                    ("spa", "spa"),
                    ("star", "star"),
                    ("store-alt", "store-alt"),
                    ("tools", "tools"),
                    ("trophy", "trophy"),
                    ("umbrella", "umbrella"),
                    ("umbrella-beach", "umbrella-beach"),
                    ("user", "user"),
                    ("user-check", "user-check"),
                    ("user-circle", "user-circle"),
                    ("user-clock", "user-clock"),
                    ("user-config", "user-cog"),
                    ("user-edit", "user-edit"),
                    ("user-friends", "user-friends"),
                    ("user-graduate", "user-graduate"),
                    ("user-plus", "user-plus"),
                    ("user-tie", "user-tie"),
                    ("user-tag", "user-tag"),
                    ("users", "users"),
                    ("wrench", "wrench"),
                    ("yin-yang", "yin-yang")
                                                ]

    icon = models.CharField(
        max_length=100,
        choices=ICON_CHOICES,
        default=None,
        blank=True
    )

    size = models.CharField(max_length=100, default="2x", blank=True, null=True)

    COLOR_CHOICES = [("cyan", "cyan"),
                     ("indigo", "indigo"),
                     ("blue", "blue"),
                     ("red", "red"),
                     ("green", "green"),
                     ("amber", "amber"),
                     ("pink", "pink"),
                     ("white", "white"),
                     ("black", "black")]

    color = models.CharField(
        max_length=100,
        choices=COLOR_CHOICES,
        default=None,
        blank=True,
        null=True
    )

    data_max = models.CharField(max_length=255, default='100', blank=True)
    data_time_speed = models.CharField(max_length=255, default='2000', blank=True)

    def __str__(self):
        return self.title
